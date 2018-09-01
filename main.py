from tkinter import *
from time import sleep
import random
tk = Tk()





canvas = Canvas(tk, width=400, height=400, bg="lightgray")
canvas.pack()
tk.title("Saper")
bomby = []


#c2.create_rectangle(0, 0, 35+8, 35+8)

lista = []
clicked = []
znaczniki = []
bomb = PhotoImage(file="/home/witek/Obrazy/icons/games/bomb.png")
explode = PhotoImage(file="/home/witek/Obrazy/icons/games/boom.png")
warning = PhotoImage(file="/home/witek/Obrazy/security2.png")
photo = PhotoImage(file="/home/witek/Obrazy/icons/games/zero.png")
background = PhotoImage(file="/home/witek/Obrazy/icons/games/Background.png")
numbers = {
    0 : PhotoImage(file="/home/witek/Obrazy/icons/games/zero.png"),
    1 : PhotoImage(file="/home/witek/Obrazy/icons/games/1.png"),
    2 : PhotoImage(file="/home/witek/Obrazy/icons/games/2.png"),
    3 : PhotoImage(file="/home/witek/Obrazy/icons/games/3.png"),
    4 : PhotoImage(file="/home/witek/Obrazy/icons/games/4.png"),
    5 : PhotoImage(file="/home/witek/Obrazy/icons/games/5.png"),
    6 : PhotoImage(file="/home/witek/Obrazy/icons/games/6.png"),
    7 : PhotoImage(file="/home/witek/Obrazy/icons/games/7.png"),
    8 : PhotoImage(file="/home/witek/Obrazy/icons/games/8.png")}

class App(Frame):
    def __init__(self, master):
        for i in range(8):
            for j in range(8):
                canvas.create_image(50*i+25, 50*j+25, image=background)

        self.kreator()
        canvas.bind("<Button-1>", self.generator)

    def znacznik(self, event):
        number = 0
        x, y = event.x // 50, event.y // 50
        for i in range(len(znaczniki)):
            if [x, y] in znaczniki[i]:
                for j in range(len(znaczniki)):
                    if znaczniki[i][1] == [x, y]:
                        canvas.delete(znaczniki[i][0])
                        del znaczniki[i]
                        for k in range(len(clicked)):
                            if clicked[k] == [x, y]:
                                del clicked[k]
                                return None
        if [x, y] not in clicked:
            a = canvas.create_image(x*50 +25, y*50 +25, image=warning)
            znaczniki.append([a, [x, y]])
            clicked.append([x, y])
        self.win()

    def boom(self, x, y):
        canvas.unbind("<Button-1>")
        canvas.unbind("<Button-3>")

        for i in range(len(bomby)):
            if bomby[i] == [x, y]:
                canvas.create_image(bomby[i][0] * 50 + 25, bomby[i][1] * 50 + 25, image=explode)
                continue
            canvas.create_image(bomby[i][0]*50 +25, bomby[i][1]*50+25, image=bomb)

        canvas.create_text(200, 160, font="Times 45 bold", fill="darkred", text="GAME OVER")

        canvas.create_text(200, 250, font="Times 20 bold", fill="green", text="Want to play again?")
        canvas.create_text(200, 290, font="Helvetica 30 italic bold", \
                           fill="green", activefill="blue", text="Click Here!")
        canvas.bind("<Button-1>", self.playagain)

    def kreator(self):
        for i in range(8):
            for j in range(8):
                lista.append([i, j])

    def click(self, event):
        x, y = event.x//50, event.y//50
        if [x, y] in clicked:
            return None
        clicked.append([x, y])
        number = 0
        for i in range(3):
            for j in range(3):
                if [x+(i-1), y+(j-1)] in bomby:
                    if i==1 and j==1:
                        self.boom(x, y)
                        return None
                    number += 1
        self.nothing(number, x, y)
        self.win()

    def win(self):
        if len(clicked)==64 and len(znaczniki) == 10:
            canvas.unbind("<Button-1>")
            canvas.unbind("<Button-3>")
            canvas.create_text(200, 100, font="Helvetica 50 bold", fill="yellow", text="YOU WIN")
            canvas.create_text(200, 250, font="Times 20 bold", fill="green", text="Want to play again?")
            canvas.create_text(200, 290, font="Helvetica 30 italic bold",\
                                   fill="green", activefill="blue", text="Click Here!")
            canvas.bind("<Button-1>", self.playagain)


    def nothing(self, number, x, y):
        canvas.create_image(x*50+25, y*50+25, image=numbers[number])

    def playagain(self, event):

        if event.x>90 and event.x<310 and event.y>270 and event.y<310:
            canvas.delete("all")
        canvas.unbind("<Button-1>")
        global lista
        global znaczniki
        global clicked
        global bomby
        lista = []
        znaczniki = []
        clicked = []
        bomby = []
        for i in range(8):
            for j in range(8):
                canvas.create_image(50*i+25, 50*j+25, image=background)

        self.kreator()
        canvas.bind("<Button-1>", self.generator)


    def generator(self, event):
        x, y = event.x//50, event.y//50
        canvas.unbind("<Button-1>")
        for i in range(10):
            z = random.randint(1, len(lista)-1)
            while lista[z] == [x, y]:
                z = random.randint(1, len(lista) - 1)
            bomby.append(lista[z])
        self.click(event)
        canvas.bind("<Button-1>", self.click)
        canvas.bind("<Button-3>", self.znacznik)




f = App(tk)


tk.mainloop()