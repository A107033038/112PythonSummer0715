from stanfordkarel import *
import os

def go_upstair():
    turn_left()
    move()
    for i in range(3):  #重複三次向左轉，即向右轉
        turn_left()
    move()

def main():
    """ Karel code goes here! """
    while front_is_blocked():
        go_upstair()
        pick_beeper()
    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/myWorld'))