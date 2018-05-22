import tkinter as tk

import time


class CustomButton:
    button = None
    counter = 0
    name = ""
    lastTimePressed = time.gmtime(0)
    instructions = None

    def __init__(self, counter, root, name):
        self.counter = counter
        self.button = tk.Button(root)
        self.name = name
        self.instructions = instructions

    def buttonAction(self):
        self.lastTimePressed = time.localtime()
        self.counter += 1
        self.button.config(text=self.name + ": " + str(self.counter))
        self.updateLabel()

    @staticmethod
    def updateLabel():
        instructions.config(text="Primary: "
                                 + CustomButton.min([topButton, jgButton, midButton, botButton, suppButton])
                                 + "\nSecondary: "
                                 + CustomButton.secondmin([topButton, jgButton, midButton, botButton, suppButton]))

    @staticmethod
    def min(buttons: []) -> str:
        counters = []
        for x in buttons:
            counters.append(x.counter)
        maxcounter = min(counters)
        indices = [index for index, val in enumerate(counters) if val == maxcounter]
        if len(indices) > 1:
            times = []
            for x in indices:
                times.append(buttons[x].lastTimePressed)
            earliest = min(times)
            indices = [indices[index] for index, val in enumerate(times) if val == earliest]
            return buttons[indices[0]].name
        else:
            return buttons[indices[0]].name

    @staticmethod
    def secondmin(buttons: []) -> str:
        minimum = CustomButton.min(buttons)
        for x in buttons:
            if minimum == x.name:
                buttons.remove(x)
        return CustomButton.min(buttons)


def center(root):
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))


def close_window():
    root.destroy()


role1, role2 = "", ""
topcounter, jgcounter, midcounter, botcounter, suppcounter = 0, 0, 0, 0, 0
root = tk.Tk()
root.title("RoleChooser")
root.geometry("200x200")
instructions = tk.Label(root,
                        text="Primary: " + role1 + ", Secondary: " + role2,
                        font="default 20")

instructions.pack()

suppButton = CustomButton(suppcounter, root, "Support")
suppButton.button.config(command=suppButton.buttonAction, text="Support: " + str(suppButton.counter))
suppButton.button.pack(side="bottom", fill='both')

botButton = CustomButton(botcounter, root, "Bottom")
botButton.button.config(command=botButton.buttonAction, text="Bottom: " + str(botButton.counter))
botButton.button.pack(side="bottom", fill='both')

midButton = CustomButton(midcounter, root, "Middle")
midButton.button.config(command=midButton.buttonAction, text="Middle: " + str(midButton.counter))
midButton.button.pack(side="bottom", fill='both')

jgButton = CustomButton(jgcounter, root, "Jungle")
jgButton.button.config(command=jgButton.buttonAction, text="Jungle: " + str(jgButton.counter))
jgButton.button.pack(side="bottom", fill='both')

topButton = CustomButton(topcounter, root, "Top")
topButton.button.config(command=topButton.buttonAction, text="Top: " + str(topButton.counter))
topButton.button.pack(side="bottom", fill='both')

CustomButton.updateLabel()

root.configure()
center(root)
root.mainloop()
