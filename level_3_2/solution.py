import copy as copy

#start: top left;   0, 0
#end: bottom right; (w-1, h-1)

def answer(map):

    class Maze:
        def __init__(self, design):
            self.design         = design
            self.size           = (len(self.design[1])-1,len(self.design[0])-1)
            self.walls          = self.identifyWalls()
            self.design_options = self.generateMapOptions()
            self.max_nodes      = None

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


        def solve(self, index, min_len):
            #later need to make history a list of lists to try different nested options, dead ends get purged.
            start   = (0,0)
            end     = self.size
            solved  = False

            history = [start]

            while(not solved):
                next_pos = self.identifyNextNode(index, history)

                if(len(next_pos)==1):
                    history.append(next_pos[0])
                elif(len(next_pos)>1):
                    print("multiple options, need to branch")
                    return 9999
                elif(len(history) > min_len):
                    print("exceeded previous solution")
                    return 9999
                else:
                    print("this path has dead ended")
                    return 9999

                if(end in next_pos):
                    print(history)
                    solved = True

            return len(history)
            #solve for the specific alteration at hand


    def main(m):
        shortest_route = 99999

        x = Maze(m)
        #for each item in x.design_options; solve it
        for index in range(0, len(x.design_options)):
            print("solving for map index: " + str(index))
            route_length = x.solve(index,shortest_route)

            if(route_length < shortest_route):
                shortest_route = route_length

            #print(maze_option)

        return shortest_route

    return main(map)


result = answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print(result)