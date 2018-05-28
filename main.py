import time
import tkinter as tk

root = tk.Tk()

BGCOLOR = "#222232"
FGCOLOR = "#ccad70"


class CustomButton:
    button = None
    counter = 0
    name = ""
    lastTimePressed = time.gmtime(0)
    label = None
    frame = None
    innerIntVar = None

    def __init__(self, counter, name, time):
        self.frame = tk.Frame(root, bg=BGCOLOR
                              )
        self.counter = counter
        self.innerIntVar = tk.IntVar()
        self.innerIntVar.set(self.counter)
        self.button = tk.Spinbox(self.frame, width="5", textvariable=self.innerIntVar,
                                 from_=0, to=99999, highlightbackground=BGCOLOR
                                 , buttonbackground=BGCOLOR
                                 )
        self.button.pack(side="right")
        self.name = name
        self.lastTimePressed = time
        # self.label = tk.Label(self.frame, text=self.name + ":") maybe make it so it has a fixed width?
        photo = tk.PhotoImage(file="assets/" + name + ".gif")
        self.label = tk.Label(self.frame, image=photo, bg=BGCOLOR
                              )
        self.label.image = photo
        self.label.pack(side="left")
        self.frame.pack(side="bottom")

    # button = None
    # counter = 0
    # name = ""
    # lastTimePressed = time.gmtime(0)
    #
    # def __init__(self, counter, name, time):
    #     self.counter = counter
    #     self.button = tk.Button(root)
    #     self.name = name
    #     self.lastTimePressed = time

    def buttonAction(self):
        temp = self.counter
        self.counter = int(self.button.get())
        if self.counter > temp:
            self.lastTimePressed = time.localtime()
        # self.button.config(text=self.name + ": " + str(self.counter))
        self.updateLabel()
        saveButtonAction()

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

    def __str__(self):
        return self.name + " " + str(self.counter) + " " + time.strftime("%d%m%y%H:%M:%S", self.lastTimePressed)


# def center(root):
#     root.update_idletasks()
#     w = root.winfo_screenwidth()
#     h = root.winfo_screenheight()
#     size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
#     x = w / 2 - size[0] / 2
#     y = h / 2 - size[1] / 2
#     root.geometry("%dx%d+%d+%d" % (size + (x, y)))


def close_window():
    root.destroy()


role1, role2 = "", ""

counters = [0, 0, 0, 0, 0]
times = [time.gmtime(0), time.gmtime(0), time.gmtime(0), time.gmtime(0), time.gmtime(0)]
try:
    with open('savefile', 'r') as file:
        i = 0
        for line in file:
            parts = line.split(' ')
            counters[i] = int(parts[1])
            times[i] = time.strptime(parts[2], "%d%m%y%H:%M:%S")
            i += 1
except FileNotFoundError:
    print("No savefile, loading 0s")

root.title("RoleChooser")
root.geometry("200x250")
instructions = tk.Label(root,
                        text="Primary: " + role1 + ", Secondary: " + role2,
                        font="Gill\ Sans 20", bg=BGCOLOR, fg=FGCOLOR)

instructions.pack()


def saveButtonAction():
    with open('savefile', 'w') as file:
        for x in [topButton, jgButton, midButton, botButton, suppButton]:
            file.write(str(x) + " \n")


saveButton = tk.Button(root, text="Save", command=saveButtonAction, highlightbackground=BGCOLOR)
saveButton.pack()

suppButton = CustomButton(counters[4], "Support", times[4])
suppButton.button.config(command=suppButton.buttonAction, text="Support: " + str(suppButton.counter))
# suppButton.button.pack(side="bottom", fill='both')

botButton = CustomButton(counters[3], "Bottom", times[3])
botButton.button.config(command=botButton.buttonAction, text="Bottom: " + str(botButton.counter))
# botButton.button.pack(side="bottom", fill='both')

midButton = CustomButton(counters[2], "Middle", times[2])
midButton.button.config(command=midButton.buttonAction, text="Middle: " + str(midButton.counter))
# midButton.button.pack(side="bottom", fill='both')

jgButton = CustomButton(counters[1], "Jungle", times[1])
jgButton.button.config(command=jgButton.buttonAction, text="Jungle: " + str(jgButton.counter))
# jgButton.button.pack(side="bottom", fill='both')

topButton = CustomButton(counters[0], "Top", times[0])
topButton.button.config(command=topButton.buttonAction, text="Top: " + str(topButton.counter))
# topButton.button.pack(side="bottom", fill='both')

CustomButton.updateLabel()

root.configure(bg=BGCOLOR)
# center(root)
root.mainloop()
