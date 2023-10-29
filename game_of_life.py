from random import random
def dead_state(width, height):
    board = [[0 for i in range(width)] for j in range(height)]
    return board

def random_state(width, height):
    state = dead_state(width, height)

    for x in range(width):
        for y in range(height):
            random_number = random()
            if random_number > 0.8:
                cell_state = 1
            else:
                cell_state = 0
            state[y][x] = cell_state
    return state

def render(state):
    width = len(state[0])
    height = len(state)
    print('-' * (width * 2 + 3))
    for y in range(height):
        line = "|"
        for x in range(width):
            if (state[y][x] == 1):
                line += " O"
            else:
                line += " ."
        line += " |"
        print (line)
    print('-' * (width * 2 + 3))

def next_board_state(state):
    width = len(state[0])
    height = len(state)
    next_state = dead_state(width, height)
    for y in range(height):
        for x in range(width):
            next_state[y][x] = next_cell_value(state, x, y)
    return next_state


def next_cell_value(state, x, y):
    height = len(state)
    width = len(state[0])

    alive_neighbors = 0
    for x1 in range(x - 1, x + 2):
        if x1 < 0 or x1 >= width: continue
        for y1 in range(y - 1, y + 2):
            if y1 < 0 or y1 >= height: continue
            if (y1 == y and x1 == x): continue

            if state[y1][x1] == 1:
                alive_neighbors += 1
    if state[y][x] == 1:
        if (alive_neighbors <= 1 or  alive_neighbors > 3):
            return 0
        else:
            return 1
    else:
        if (alive_neighbors == 3):
            return 1
        else:
            return 0
            
