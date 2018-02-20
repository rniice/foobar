import copy as copy

#start: top left;   0, 0
#end: bottom right; (w-1, h-1)

def answer(maze):

    class Route:
        def __init__(self, history, last_pos):
            self.history    = history
            self.next_pos   = None
            self.last_pos   = last_pos
            self.solved     = False
            self.length     = len(self.history)

        def addNextPos(self, next_pos):
            self.history.append(next_pos)
            self.length+=1
            if(next_pos == self.last_pos):
                #print("route solved")
                self.solved = True

    class Maze:
        def __init__(self, design):
            self.design                 = design
            self.start                  = None
            self.end                    = None
            self.bounds                 = (len(self.design[0]) - 1, len(self.design) - 1)
            self.walls                  = self.identifyWalls()
            self.design_options         = self.generateMapOptions()
            self.routes                 = None
            self.max_route_index        = 0
            self.current_route          = 0
            self.shortest_route_index   = 0
            self.shortest_route_length  = 99999

        def getNextRoute(self):
            self.max_route_index = max(self.routes.keys())+1
            return self.max_route_index

        def resetOptionIterators(self ,shortest_length, start, end):
            self.start = start
            self.end = end
            self.routes = {0:Route([self.start],self.end)}
            self.max_route_index = 0
            self.current_route = 0
            self.shortest_route_index = 0
            self.shortest_route_length = shortest_length

        def removeWall(self, index):
            mod = copy.deepcopy(self.design)
            mod[index[1]][index[0]] = 0
            return mod

        def identifyWalls(self):
            wall_tuples = []
            for y, maze_row in enumerate(self.design):
                for x, val in enumerate(maze_row):
                    if(val==1):
                        wall_tuples.append((x,y))
            #make up a fake wall within range if no walls exist
            if(len(wall_tuples)==0 and len(self.design)>1):
                wall_tuples.append((0,1))
            else:
                wall_tuples.append((1,0))

            return wall_tuples

        def generateMapOptions(self):
            options = []
            for wall in self.walls:
                options.append(self.removeWall(wall))
            return options

        def identifyNextNode(self, index, history):
            option_map = self.design_options[index]
            pos = history[-1]
            next_pos = []

            #up, down, left, right
            allow     = [1, 1, 1, 1]
            map_next  = [(0,-1),(0,1),(-1,0),(1,0)]

            pos_x = pos[0]
            pos_y = pos[1]

            if(pos_x == 0): allow[2]=0
            #if(pos_x == self.end[0]): allow[3]=0
            if(pos_x == self.bounds[0]): allow[3]=0
            if (pos_y == 0): allow[0]=0
            #if (pos_y == self.end[1]): allow[1]=0
            if (pos_y == self.bounds[1]): allow[1]=0

            for index, val in enumerate(allow):
                if(val == 1):
                    pos_x_next = pos_x + map_next[index][0]
                    pos_y_next = pos_y + map_next[index][1]
                    next_tuple = (pos_x_next, pos_y_next)

                    if(option_map[pos_y_next][pos_x_next] == 0 and next_tuple not in history):
                        next_pos.append(next_tuple)

            return next_pos

        def recursiveSolve(self, index, reset, start, end, shortest_route_length):
            if(reset):
                self.resetOptionIterators(shortest_route_length, start, end)

            while ((self.current_route <= self.max_route_index) and (self.routes[self.current_route].length < self.shortest_route_length)):
                next_pos = self.identifyNextNode(index, self.routes[self.current_route].history)
                #print(next_pos)

                if(len(next_pos)>0 and (not self.routes[self.current_route].solved) ):
                    default = next_pos.pop(0)
                    self.routes[self.current_route].addNextPos(default)

                    for option in next_pos:
                        new_route_index = self.getNextRoute()
                        prior_history = copy.deepcopy(self.routes[self.current_route].history[0:-1])
                        self.routes[new_route_index] = Route(prior_history, self.end)
                        self.routes[new_route_index].addNextPos(option)

                else:
                    if(self.routes[self.current_route].solved and self.routes[self.current_route].length < self.shortest_route_length):
                        self.shortest_route_length = self.routes[self.current_route].length
                        self.shortest_route_index  = self.current_route
                        self.current_route += 1
                    else:
                        self.current_route+=1

            return {'len': self.shortest_route_length, 'history': self.routes[self.shortest_route_index].history}

    def printResults(maze, route):
        result_path = copy.deepcopy(maze)
        for y,row in enumerate(maze):
            for x,value in enumerate(row):
                #change the value to "*" if in the route
                if (x,y) in route:
                    result_path[y][x] = 8
        for line in result_path:
            print(line)

    def main(m):

        shortest_one_way_route = 9999999
        shortest_two_way_route = 9999999
        x = Maze(m)

        for index in range(0, len(x.walls)):

            #find the distance from start to the wall
            start = (0,0)
            end = x.walls[index]
            start2wall = x.recursiveSolve(index, True, start, end, shortest_one_way_route)
            #print("start to wall for wall: " + str(x.walls[index]))
            #printResults(x.design_options[index], start2wall['history'])

            start = (len(x.design[0]) - 1, len(x.design) - 1)
            end = x.walls[index]
            end2wall = x.recursiveSolve(index, True, start, end, shortest_one_way_route)
            #print("end to wall for wall: " + str(x.walls[index]))
            #printResults(x.design_options[index], end2wall['history'])

            #make sure both routes connect
            if(start2wall['history'][-1] == end2wall['history'][-1]):
                combined_route_length = start2wall['len'] + end2wall['len'] - 1
                if(combined_route_length < shortest_two_way_route ):
                    shortest_two_way_route = combined_route_length

        return shortest_two_way_route

    return main(maze)


result = answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print(result)