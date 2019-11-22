import sys
import timeit
from itertools import repeat

def get_winning_player(m, n):

    #grid = [['E' for i in range(m+1)] for j in range(n+1)]

    # repeat avoids unnecessary i's being created
    grid = [['E' for i in repeat(None, m+1)] for j in repeat(None, n+1)]
    grid = set_grid_loses(grid, 0, 0, m, n) #(0,0) is a known state and can be set
    i = 0
    while i <= n:
        # quit once result is found -- Can delete if this is against the rules
        if grid[n][m] != 'E':
            return 1 if grid[n][m] == 'w' else 2
        #print_grid(grid)
        while 'E' in grid[i]:
            j = grid[i].index('E')
            if is_winning_state(grid, i, j):
                grid[i][j] = 'w'
            else:
                grid = set_grid_loses(grid, i, j, m, n)
        i+=1

    return 1 if grid[n][m] == 'w' else 2


# if there is a move in which you can make the other player lose you are in a winning state
def is_winning_state(grid, x, y):

    #  -- slower to do it the smarter way --
    # moves = get_possible_moves(grid, x, y)
    # return 'l' in moves

    # if 'l' in grid[x][:y]:
    #     return True
    # if 'l' in [grid[i][y] for i in range(x)]:
    #     return True
    # if 'l' in [grid[x-i-1][y-i-1] for i in range(min(x, y)-1)]:
    #     return True
    # return False
    if 'l' in grid[x][:y]:
        return True
    for i in range(x):
        if grid[i][y] == 'l':
            return True
    for i in range(min(x, y)-1):
        if grid[x-i-1][y-i-1] == 'l':
            return True
    return False


# def get_possible_moves(grid, x, y):
#     moves = grid[x][:y]
#     moves = moves + [grid[i][y] for i in range(x)]
#     moves = moves + [grid[x-i-1][y-i-1] for i in range(min(x, y)-1)]
#     return moves


def set_grid_loses(grid, x, y, m, n):
    # (0,0) is an exception to the rules as it is the final state
    grid[x] = ['w'] * len(grid[x])
    for i in range(n+1):
        grid[i][y] = 'w'
        if i <= m:
            grid[i][i] = 'w'
    grid[x][y] = 'w' if x == 0 and y == 0 else 'l'
    return grid


def print_grid(grid):
    for i in range(len(grid)):
        print('   '.join(grid[len(grid)-1-i]) + '\n')


def main():
    start = timeit.default_timer()
    m, n = int(sys.argv[1]), int(sys.argv[2])
    print("The winning player for game ({},{}) is: {}".format(m, n, get_winning_player(m,n)))
    stop = timeit.default_timer()
    print("Algo took: " + str(stop-start))

    #start = timeit.default_timer()
    for i in range(m):
        for j in range(n):
            start = timeit.default_timer()
            if get_winning_player(i,j) == 2:
                pass
                #print("Wow player 2 won: ({},{})".format(i,j))
            stop = timeit.default_timer()
            print("Finding win took for ({},{}): {}".format(i,j,str(stop-start)))

if __name__ == "__main__":
    main()
