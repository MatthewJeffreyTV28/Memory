from PyUI.Window import Window
from PyUI.Examples.TestScreen import tScreen

window = Window("Example App", (0,255,0))

t = tScreen(window)

screen = t

while True:

    window.checkForInput(screen)
    window.update(screen)
