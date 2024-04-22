""" TD05 """

import tkinter as tk
from tkinter import ttk
from random import randint

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400, bg='red')


class Cible:
    def __init__(self, score_salve, nombre_tir):
        self.score = score_salve
        self.salve = nombre_tir

    def tir(self, event):
        if self.salve < 5:
            x, y = randint(0,400), randint(0,400)
            cercle(x, y, 15, "black")
            self.salve += 1
            self.score += score_tir(x,y)
            ttk.Label(root, text =f"score de {self.score} points", width=17+self.score//10).grid(row=1,column=1)
            #Je n'ai pas trouvé comment actualiser le Label... Cette technique fonctionne bie tout de même.
        return

#Effectue une rafale de 5-(le nombre de tirs déjà effectués grâce à "<f>"
    def rafale(self):
         event = 0 #Pour eviter l'erreur car "rafale" ne nécessite pas de key binding donc pas d'event
         for i in range(5):
             if self.salve <5:
                self.tir(event)
         return

#Comptabilise le score d'un tir:
def score_tir(x,y):
    score_balle = 0
    for i in range(0,6):
        r = 30 * (6 - i)
        if (r-30)**2 <= (x-200)**2 + (y-200)**2 <= r**2:
            score_balle = i+1
    return score_balle


def cercle(x,y,r,couleur):
    points = ((x-r, y-r), (x+r, y+r))
    canvas.create_oval(*points, outline='red', fill = couleur)
    return


#Création de la cible:
for i in range(0,6):
    x,y = 200,200
    r = 30*(6-i)
    if r == 30*2:
        cercle(x,y,r,"red")
        canvas.create_text(x, y-r+15, text=f"{i+1}", font = ('Times', '24', 'bold'), fill = 'ivory')
    else:
        cercle(x,y,r,"ivory")
        canvas.create_text(x,y-r+15, text=f"{i+1}", font = ('Times', '24', 'bold'), fill = 'red')

canvas.create_line(0,200,400,200,fill='red')
canvas.create_line(200,0,200,400,fill='red')
canvas.grid(row=0, column=0, columnspan=3)



Master = Cible(0, 0)

ttk.Label(root, text=f"score de 0 points", width=17).grid(row=1,column=1)

ttk.Button(root, text="Feu!", width=10, command=Master.rafale).grid(row=1,column=0,sticky=tk.W)
#On tire une rafale de 5 tirs d'affilé (je n'ai pas bine compris si c'était ce que l'énoncé entendait par "répéter 5 fois".

root.bind("<f>", Master.tir)
#On effectue un tir à la fois en appuyant sur "f"

ttk.Button(root, text="Quitter", width=10, command=root.destroy).grid(row=1,column=2, sticky = tk.E)


root.mainloop()
