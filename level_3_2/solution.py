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
                self.solved = True


    class Maze:
        def __init__(self, design):
            self.design                 = design
            self.end                    = (len(self.design[1])-1,len(self.design[0])-1)
            self.walls                  = self.identifyWalls()
            self.design_options         = self.generateMapOptions()
            self.routes                 = {0:Route([(0,0)],self.end)}
            self.max_route_index        = 0
            self.current_route          = 0
            self.shortest_route_index   = 0
            self.shortest_route_length  = 99999

        def getNextRoute(self):
            self.max_route_index = max(self.routes.keys())+1
            return self.max_route_index

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
            return wall_tuples

        def generateMapOptions(self):
            options = [copy.deepcopy(self.design)]
            for wall in self.walls:
                options.append(self.removeWall(wall))
            return options

        def identifyNextNode(self, index, history):
            option_map = self.design_options[index]
            pos = history[-1]
            next_pos = []

            #restrictions [up, down, left, right]
            allow     = [1, 1, 1, 1]
            map_next  = [(0,-1),(0,1),(-1,0),(1,0)]

            pos_x = pos[0]
            pos_y = pos[1]

            #test board conditions
            if(pos_x == 0): allow[2]=0
            if(pos_x == self.end[0]): allow[3]=0
            if (pos_y == 0): allow[0]=0
            if (pos_y == self.end[1]): allow[1]=0

            #filter out wall conditions
            for index, val in enumerate(allow):
                #print("allows: " + str(allow))
                if(val == 1):
                    pos_x_next = pos_x + map_next[index][0]
                    pos_y_next = pos_y + map_next[index][1]
                    next_tuple = (pos_x_next, pos_y_next)
                    #print("next_tuple before check: " + str(next_tuple))
                    #maze_val_next = option_map[pos_y_next][pos_x_next]
                    if(option_map[pos_y_next][pos_x_next] == 0 and next_tuple not in history):
                        #print("next_tuple after check: " + str(next_tuple))
                        next_pos.append(next_tuple)
                        #print("passable: " + str(next_tuple))

            #print(allow)
            return next_pos


        def recursiveSolve(self, index):
            #later need to make history a list of lists to try different nested options, dead ends get purged.
            solved  = False

            #while(not solved and (len(self.history_queue) != self.history_queue_route - 1)):
            while (not solved and self.current_route <= self.max_route_index):
                next_pos = self.identifyNextNode(index, self.routes[self.current_route].history)

                if(len(next_pos)>0):
                    default = next_pos.pop(0)
                    self.routes[self.current_route].addNextPos(default)

                    print("route iteration: " +str(self.current_route))
                    printResults(self.design_options[index], self.routes[self.current_route].history)
                    #for the remaining options, create new route alternates
                    for option in next_pos:
                        new_route_index   = self.getNextRoute()
                        self.routes[new_route_index] = Route(self.routes[self.current_route].history[0:-1], self.end)
                        self.routes[new_route_index].addNextPos(option)
                        #print("option: " +str(option))

                else:
                    print("either dead ended or exceeded prior path length, going to next item in queue")

                    #see if present route option is shortest
                    if(self.routes[self.current_route].solved and self.routes[self.current_route].length < self.shortest_route_length):
                        self.shortest_route_length = self.routes[self.current_route].length
                        self.shortest_route_index  = self.current_route
                        solved = True
                        self.current_route += 1
                    else:
                        #need to keep chugging along on another path option
                        self.current_route+=1

                    #self.history_queue_route +=1
                    #self.history_queue_lock = False

                #printResults(self.design_options[index], self.history_queue[self.history_queue_route])
                #default to solving the first in the self.history_queue


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
        shortest_route = 9999999

        x = Maze(m)

        for index in range(0, len(x.design_options)):
            print("solving for map index: " + str(index))

            results = x.recursiveSolve(index)
            print(results)
            printResults(x.design_options[index],results['history'])
            print(results['len'])
            if(results):
                if(results['len'] < shortest_route):
                    shortest_route = results['len']

        return shortest_route

    return main(maze)


result = answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
#result = answer([[0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])

#result = answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
print(result)