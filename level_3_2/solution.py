import copy as copy

#start: top left;   0, 0
#end: bottom right; (w-1, h-1)

def answer(maze):

    class Maze:
        def __init__(self, design):
            self.design                 = design
            self.size                   = (len(self.design[1])-1,len(self.design[0])-1)
            self.walls                  = self.identifyWalls()
            self.design_options         = self.generateMapOptions()
            self.history                = [(0,0)]
            self.shortest_path          = 99999
            self.history_queue          = [[(0,0)]]
            self.history_queue_route    = 0
            self.history_queue_lock     = False

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
            if(pos_x == self.size[0]): allow[3]=0
            if (pos_y == 0): allow[0]=0
            if (pos_y == self.size[1]): allow[1]=0

            #filter out wall conditions
            for index, val in enumerate(allow):
                if(val == 1):
                    pos_x_next = pos_x + map_next[index][0]
                    pos_y_next = pos_y + map_next[index][1]
                    next_tuple = (pos_x_next, pos_y_next)

                    #maze_val_next = option_map[pos_y_next][pos_x_next]
                    if(option_map[pos_y_next][pos_x_next] == 0 and next_tuple not in history):
                        next_pos.append(next_tuple)
                        #print("passable: " + str(next_tuple))

            #print(allow)
            return next_pos


        def recursiveSolve(self, index):
            #later need to make history a list of lists to try different nested options, dead ends get purged.
            solved  = False

            while(not solved):
                next_pos     = self.identifyNextNode(index, self.history_queue[self.history_queue_route])
                route_length = len(self.history_queue[self.history_queue_route])

                if(len(next_pos)>0 and (route_length+1) < self.shortest_path):
                    #create new copies in the queue
                    for i in range(0, len(next_pos) - 1):
                        previous_route = copy.deepcopy(self.history_queue[self.history_queue_route])
                        self.history_queue.append(previous_route)

                    #do this only when the lengths are the same.
                    for i, option in enumerate(next_pos):
                        self.history_queue[self.history_queue_route+i].append(option)

                else:
                    print("either dead ended or exceeded prior path length, going to next item in queue")
                    print(self.history_queue)
                    self.history_queue_route +=1

                print(self.history_queue[self.history_queue_route])
                printResults(self.design_options[index], self.history_queue[self.history_queue_route])
                #default to solving the first in the self.history_queue

                if(self.size in next_pos):
                    print("solved!")
                    solved = True

            return {'len': len(self.history_queue[self.history_queue_route]), 'history': self.history_queue[self.history_queue_route]}


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
        #for each item in x.design_options; solve it
        #for index in range(0, len(x.design_options)):
        for index in range(1, 2):
            print("solving for map index: " + str(index))

            results = x.recursiveSolve(index)
            printResults(x.design_options[index],results['history'])

            if(results):
                if(results['len'] < shortest_route):
                    shortest_route = results['len']

        return shortest_route

    return main(maze)


result = answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
#result = answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
print(result)