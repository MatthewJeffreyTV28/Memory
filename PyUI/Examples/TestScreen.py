from PyUI.PageElements import *
from PyUI.Screen import Screen

class tScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255, 255, 255))

    def elementsToDisplay(self):
        self.elements = [
            Button((20, 80), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            
            Image((50, 80), 10, 10, "./hawk.jpeg"),

            Label((80, 20), 10, 10, "Welp")
        ]