from PyUI.PageElements import *
from PyUI.Screen import Screen
import random

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (200, 150, 255))
        self.cardImages = ['./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg']
        self.ducks = ['./imgs/brownChestDuck.jpg', './imgs/duck.jpg', './imgs/fakeDuck.jpg', './imgs/greenHeadDuck.jpg', './imgs/staringDuck.jpg', './imgs/talkingDuck.jpg', './imgs/walkingDuck.jpg', './imgs/yellowDuck.jpg']
        self.cardStates = ['dormant', 'dormant', 'dormant', 'dormant', 'dormant', 'dormant', 'dormant', 'dormant']
        self.check = []
        self.matched = []
        self.run = True

        self.cardImages.extend(self.cardImages)
        self.ducks.extend(self.ducks)
        self.cardStates.extend(self.cardStates)
        random.shuffle(self.ducks)

    def elementsToDisplay(self):

        self.elements = []

        if self.run:
            index = -1
            for x in range(4):
                xCord = 20 * x + 20
                for y in range(4):
                    index += 1
                    yCord = 20 * y + 25
                    self.elements.append(Card((xCord, yCord), 10, 10, self.cardImages[index], index, self.cardStates[index]))
                    self.elements.append(Label((50, 5), 10, 2, "Click 2 images and try to match them"))

        if len(self.check) == 2:
            self.waitForNextFrame = 0.5
            for card in self.check:
                if self.cardStates[card.index] != 'matched':
                    self.cardImages[card.index] = './imgs/cardCover.jpg'
                    self.cardStates[card.index] = 'dormant'
            self.check = []
        
        if len(self.matched) >= 8:
             self.run = False
             self.elements = []
             self.elements.append(Label((50, 50), 50, 50, "You win!", 30))

class Card(Image):
    def __init__(self, centerXY, width, height, image, index, state):
        super().__init__(centerXY, width, height, image)
        self.state = state
        self.index = index
        
    def onClick(self, screen):
        screen.cardImages[self.index] = screen.ducks[self.index]
        screen.cardStates[self.index] = 'active'
        screen.check.append(self)

        for card in screen.elements:
            if type(card) != Label:
                if card.state == 'active' and card != self:
                    if screen.ducks[card.index] == screen.ducks[self.index]:
                        screen.cardStates[card.index] = 'matched'
                        screen.cardStates[self.index] = 'matched'
                        if self not in screen.matched:
                            screen.matched.append(self)
