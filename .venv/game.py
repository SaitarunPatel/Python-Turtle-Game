import random
from turtle import Turtle
import constants

class GameController:
    current_level = 0
    high_score = 0
    cars_list = []
    player = None
    scoreGraphic = None
    
    def __init__(self):
        self.current_level = 0
        self.makeTurtle()
        self.addCars()
        self.setUpScoreGraphic()
        self.writeScoreOnView()
        self.loadHighScore('read', None)

    def loadHighScore(self, fileMode, data):
        if fileMode == 'read':
            with open('high_score.txt', mode='r') as file:
                self.high_score = int(file.read())
        else:
            self.high_score = data
            with open('high_score.txt', mode='w') as file:
                file.write(str(data))

    def setUpScoreGraphic(self):
        self.scoreGraphic = Turtle()
        self.scoreGraphic.penup()
        self.scoreGraphic.hideturtle()
        self.scoreGraphic.goto(constants.LEVEL_TEXT_POSITION[0], constants.LEVEL_TEXT_POSITION[1])

    def writeScoreOnView(self):
        if self.current_level > self.high_score:
            self.loadHighScore('write', self.current_level)
        self.scoreGraphic.clear()
        self.scoreGraphic.write(f"SCORE: {self.current_level} HIGH SCORE: {self.high_score}", align="center", font=("Arial", 25, "normal"))

    def makeTurtle(self):
        self.player = Turtle(constants.PLAYER_TYPE)
        self.player.color(constants.PLAYER_COLOR)
        self.player.penup()
        self.player.goto(constants.PLAYER_START_LOCATION[0], constants.PLAYER_START_LOCATION[1])
        self.player.left(90)

    def resetTurtle(self):
        self.player.goto(constants.PLAYER_START_LOCATION[0], constants.PLAYER_START_LOCATION[1])

    def returnTurtleCoords(self):
        return self.player.xcor(), self.player.ycor()

    def moveTurtleUp(self):
        if self.player.ycor() + constants.PLAYER_SPEED <= 330:
            self.player.goto(0, self.player.ycor() + constants.PLAYER_SPEED)

    def moveTurtleDown(self):
        if self.player.ycor() - constants.PLAYER_SPEED >= -330:
            self.player.goto(0, self.player.ycor() - constants.PLAYER_SPEED)

    def incrementLevel(self):
        self.current_level += 1
        print('Level ', self.current_level)
        self.writeScoreOnView()
        self.resetTurtle()
        self.resetCars()
        self.addCars()

    def resetCars(self):
        for carObject in self.cars_list:
            carObject['graphic'].clear()
            carObject['graphic'].hideturtle()
        self.cars_list = []

    def addCars(self):
        self.cars_list = []
        for laneYCoord in constants.CARS_LANES_MAPPING:
            carColor = random.choice(constants.CARS_COLOR)
            tempCarGraphic = Turtle(constants.CAR_TYPE)
            tempCarGraphic.color(carColor)
            tempCarGraphic.penup()
            tempCarGraphic.goto(300, laneYCoord)
            tempCarObject = {
                'graphic': tempCarGraphic,
                'speed': random.choice(constants.CARS_SPEED_MAPPING),
                'color': carColor,
                'initialY': laneYCoord,
                'initialX': 300
            }
            self.cars_list.append(tempCarObject)

    def moveCars(self):
        # self.carObject['graphic'].goto(self.carObject['graphic'].xcor() - self.carObject['speed'], self.carObject['initialY'])
        for carObject in self.cars_list:
            gotoXcor = carObject['graphic'].xcor() - carObject['speed']
            gotoYcor = carObject['initialY']
            carObject['graphic'].goto(gotoXcor, gotoYcor)
            if gotoXcor <= -300:
                carObject['graphic'].goto(carObject['initialX'], 300)
                carObject['speed'] = random.choice(constants.CARS_SPEED_MAPPING)
                carColor = random.choice(constants.CARS_COLOR)
                carObject['color'] = carColor
                carObject['graphic'].color(carColor)
                carObject['initialX'] = 300

    def detectColission(self, x_cor, y_cor):
        for carObject in self.cars_list:
            if carObject['graphic'].distance(x_cor, y_cor) < 10:
                return True
        return False

    def checkCurrentStateOfPlay(self):
        x_cor, y_cor = self.returnTurtleCoords()
        if y_cor == 330:
            self.incrementLevel()
        elif self.detectColission(x_cor, y_cor):
            return True
        return False



