import tkinter as tk
import Button


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


role1, role2 = "",""
topcounter, jgcounter, midcounter, botcounter, suppcounter = 0, 0, 0, 0, 0
root = tk.Tk()
root.title("RoleChooser")
root.geometry("800x550")
instructions = tk.Label(root,
                        text="Primary: " + role1 + ", Secondary: " + role2,
                        font="default 20")

instructions.pack()
topButton = Button.CustomButton(topcounter, root, "Top")
topButton.button.config(command=topButton.buttonAction, text="Top: " + str(topButton.counter))
topButton.button.pack(side="bottom", fill='both')
jgButton = Button.CustomButton(jgcounter, root, "Jungle")
jgButton.button.config(command=jgButton.buttonAction, text="Jungle: " + str(jgButton.counter))
jgButton.button.pack(side="bottom", fill='both')
midButton = Button.CustomButton(midcounter, root, "Middle")
midButton.button.config(command=midButton.buttonAction, text="Middle: " + str(midButton.counter))
midButton.button.pack(side="bottom", fill='both')
botButton = Button.CustomButton(botcounter, root, "Bottom")
botButton.button.config(command=botButton.buttonAction, text="Bottom: " + str(botButton.counter))
botButton.button.pack(side="bottom", fill='both')
suppButton = Button.CustomButton(suppcounter, root, "Support")
suppButton.button.config(command=suppButton.buttonAction, text="Support: " + str(suppButton.counter))
suppButton.button.pack(side="bottom", fill='both')

root.configure()
center(root)
root.mainloop()