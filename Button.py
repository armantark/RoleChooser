from tkinter import Button
import time


class CustomButton():
    button = None
    counter = 0
    name = ""
    lastTimePressed = None

    def __init__(self, counter, root, name):
        self.counter = counter
        self.button = Button(root)
        self.name = name

    def buttonAction(self):
        self.lastTimePressed = time.localtime()
        self.counter += 1
        self.button.config(text= self.name + ": " + str(self.counter))

    @staticmethod
    def min(buttons: [Button]) -> str:
        counters = []
        for x in buttons:
            counters.append(x.counter)
        maxcounter = max(counters)
        indices = [index for index, val, in enumerate(counters) if val == maxcounter]
        if indices.size > 1:
            return
        else:
            return buttons[indices[0]].name

