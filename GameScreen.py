from PyUI.PageElements import *
from PyUI.Screen import Screen
import random

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (200, 150, 255))
        self.cardImages = ['./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg','./imgs/cardCover.jpg']
        self.ducks = ['./imgs/brownChestDuck.jpg', './imgs/duck.jpg', './imgs/fakeDuck.jpg', './imgs/greenHeadDuck.jpg', './imgs/staringDuck.jpg', './imgs/talkingDuck.jpg', './imgs/walkingDuck.jpg', './imgs/yellowDuck.jpg']
        self.check = []
        self.matched = []

        self.cardImages.extend(self.cardImages)
        self.ducks.extend(self.ducks)
        random.shuffle(self.ducks)

        self.elements.append(Label((50, 5), 10, 2, "Click 2 images and try to match them"))

    def elementsToDisplay(self):

        for element in self.elements:
            if type(element) == Card:
                if element.state == 'matched':
                    pass
                else:
                    self.elements.remove(element)

        index = -1
        for x in range(4):
            xCord = 20 * x + 20
            for y in range(4):
                index += 1
                yCord = 20 * y + 25
                self.elements.append(Card((xCord, yCord), 10, 10, self.cardImages[index], index))
        

        if len(self.check) == 2:
            self.waitForNextFrame = 1
            for card in self.check:
                if card.state != 'matched':
                    self.cardImages[card.index] = './imgs/cardCover.jpg'
                    card.state = 'dormant'
            self.check = []

class Card(Image):
    def __init__(self, centerXY, width, height, image, index):
        super().__init__(centerXY, width, height, image)
        self.state = 'dormant'
        self.index = index
        
    def onClick(self, screen):
        screen.cardImages[self.index] = screen.ducks[self.index]
        self.state = 'active'
        screen.check.append(self)

        for card in screen.elements:
            if type(card) == Label:
                    pass
            elif card.state == 'active' and card != self:
                    if type(card) == Label:
                        pass
                    elif screen.ducks[card.index] == screen.ducks[self.index]:
                        card.state = 'matched'
                        self.state = 'matched'
                        screen.matched.append(card)
                        screen.matched.append(self)
        
        if len(screen.matched) >= 16:
             screen.elements = []
             screen.elements.append(Label((50, 5), 10, 2, "You win!"))
