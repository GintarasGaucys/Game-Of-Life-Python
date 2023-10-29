from game_of_life import *
from time import sleep
height = int(input("Height: "))
width = int(input("Width: "))
seconds = int(input("Seconds to wait after each generation: "))
state = random_state(width, height)
while(True):
    render(state)
    print()
    state = next_board_state(state)
    sleep(seconds)