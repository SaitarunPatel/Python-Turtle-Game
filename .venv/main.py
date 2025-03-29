from turtle import Turtle, Screen
import time
import constants
from game import GameController

screen = Screen()
screen.setup(width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT)
screen.title("Turtle Cross the Road")
screen.bgcolor("white")
screen.tracer(0)
screen.update()

current_level = 1
game_is_on = True

# Start game
game = GameController()

def moveUp():
    print("Move up")
    game.moveTurtleUp()
def moveDown():
    print("Move down")
    game.moveTurtleDown()

screen.listen()
screen.onkey(moveUp, "Up")
screen.onkey(moveDown, "Down")

while game_is_on:
    game.moveCars()
    state_of_play = game.checkCurrentStateOfPlay()
    time.sleep(0.05)
    if state_of_play:
        game_is_on = False
    screen.update()

screen.exitonclick()
