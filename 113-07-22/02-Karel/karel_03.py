from stanfordkarel import *
import os

def turn_right(): #定義右轉
    turn_left()
    turn_left()
    turn_left()

def turn_around():  #定義向後轉
    turn_left()
    turn_left()

def fill_pothole():  #定義"補洞"
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()

def main():
    """ Karel code goes here! """
    move()
    fill_pothole()
    move()
    move()
    move()
    fill_pothole()
    move()
    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_03'))