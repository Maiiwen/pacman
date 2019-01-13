from tkinter import *

canvas = Canvas(window, width=500, height=800, background ='black')
class 
def clavier(event):

    touche = event.keysym

    if touche == "Up":

    elif touche == "Down":

    elif touche == "Right":

    elif touche == "Left":

    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

def pacAnim():
    while True:
        try:
            global photo
            global frame
            global label
            photo = PhotoImage(file = pac, format = "gif - {}".format(frame))
            label.configure(image = nextframe)
            frame = frame + 1
        except Exception:
            frame = 1
            break

# coordonnées initiales
coords = (0, 0)
# création du rectangle
rectangle = canvas.create_rectangle(0,0,15,15,fill="violet")

# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()
root.mainloop()
