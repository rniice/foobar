from collections import deque

def answer(maze):

    class Route:
        def __init__(self, history, last_pos):
            self.history    = deque(history)
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

        def addNewRoute(self, history):
            self.max_route_index+=1
            self.routes[self.max_route_index] = Route(history, self.end)

        def resetOptionIterators(self ,shortest_length, start, end):
            self.start = start
            self.end = end
            self.routes = {0:Route([self.start],self.end)}
            self.max_route_index = 0
            self.current_route = 0
            self.shortest_route_index = 0
            self.shortest_route_length = shortest_length

        def removeWall(self, index):
            mod = list()
            for i, item in enumerate(self.design):
                mod.append(list())
                for val in item:
                    mod[i].append(val)
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
            if(pos_x == self.bounds[0]): allow[3]=0
            if(pos_y == 0): allow[0]=0
            if(pos_y == self.bounds[1]): allow[1]=0

            for index, val in enumerate(allow):
                if(val):
                    pos_x_next = pos_x + map_next[index][0]
                    pos_y_next = pos_y + map_next[index][1]
                    next_tuple = (pos_x_next, pos_y_next)

                    if(not option_map[pos_y_next][pos_x_next] and next_tuple not in history):
                        next_pos.append(next_tuple)

            return next_pos

        def solvePathway(self, index, reset, start, end, shortest_route_length):
            if(reset):
                self.resetOptionIterators(shortest_route_length, start, end)

            while ((self.current_route <= self.max_route_index) and (self.routes[self.current_route].length < self.shortest_route_length)):
                previous_history = list(self.routes[self.current_route].history)
                next_pos = self.identifyNextNode(index, list(self.routes[self.current_route].history))

                if(next_pos and (not self.routes[self.current_route].solved) and self.routes[self.current_route].length < self.shortest_route_length ):
                    self.routes[self.current_route].addNextPos(next_pos.pop(0))
                    for option in next_pos:
                        self.addNewRoute(previous_history + [option])

                else:
                    if(self.routes[self.current_route].solved and self.routes[self.current_route].length < self.shortest_route_length):
                        self.shortest_route_length = self.routes[self.current_route].length
                        self.shortest_route_index  = self.current_route
                        self.current_route += 1

                    else:
                        self.current_route+=1

            return {'len': self.shortest_route_length, 'last': self.routes[self.shortest_route_index].history[-1]}
    def main(m):
        shortest_two_way_route = 9999999
        results                = dict()
        x = Maze(m)

        for index in range(0, len(x.walls)):
            start2wall = x.solvePathway(index, True, (0,0), x.walls[index], shortest_two_way_route)
            end2wall = x.solvePathway(index, True, (len(x.design[0]) - 1, len(x.design) - 1), x.walls[index], shortest_two_way_route)

            if(start2wall['last']==end2wall['last'] and x.walls[index]==start2wall['last']):
                results[index] = start2wall['len'] + end2wall['len'] - 1
                if(results[index] < shortest_two_way_route ):
                    shortest_two_way_route = results[index]

        return shortest_two_way_route

    return main(maze)