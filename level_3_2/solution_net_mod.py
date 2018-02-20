from collections import deque

def shortest_path(pos_x, pos_y, maze):
    w, h = (len(maze[0]), len(maze))
    board = [[None for i in range(w)] for i in range(h)]
    board[pos_x][pos_y] = 1
    routes = deque([(pos_x, pos_y)])
    while routes:
        route_x, route_y = routes.popleft()
        neighbor_deltas = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        for i in neighbor_deltas:
            next_x, next_y = route_x + i[0], route_y + i[1]
            #travel through each passable point and log distance each maze wall
            if 0 <= next_x < h and 0 <= next_y < w and not board[next_x][next_y]:
                board[next_x][next_y] = board[route_x][route_y] + 1
                if not maze[next_x][next_y]: routes.append((next_x, next_y))
    return board

def answer(maze):
    w, h = (len(maze[0]), len(maze))
    top2wall = shortest_path(0, 0, maze)
    bot2wall = shortest_path(h - 1, w - 1, maze)
    tot_path = 9999
    #for each point in the maze where the top2wall and bot2wall routes exist, find and return min total distance
    for i in range(h):
        for j in range(w):
            if top2wall[i][j] and bot2wall[i][j]: tot_path = min(top2wall[i][j] + bot2wall[i][j] - 1, tot_path)
    return tot_path