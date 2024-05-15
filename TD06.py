""" TD06 """

import tkinter as tk
import random
import numpy as np

root = tk.Tk()

WIDTH = 500
HEIGHT = 500
can = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')

graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6],
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

pos = np.array([(random.random()*WIDTH, random.random()*HEIGHT) for i in range(len(graph))])
vit = np.array([((random.random() - 0.5), (random.random() - 0.5)) for i in range(len(graph))])

class Unknown:
    def __init__(self, pos, vit):
        self.pos = pos
        self.vit = vit

    def ressort(self, event):
        can.delete("all")
        self.vit = self.vit + np.array([(somme_forces(i)[0]*tau, somme_forces(i)[1]*tau) for i in range(len(graph))])
        self.pos = self.pos + tau * vit
        draw(can, graph, self.pos)

def draw(can, graph, pos):
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="black")
    return

draw(can, graph, pos)

k = 0.2
l0 = 100
tau = 0.1
def force(i, j):
    l = np.sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)+0.001
    F = k*(l - l0)
    vect_u = ((pos[j][0] - pos[i][0])/l, (pos[j][1] - pos[i][1])/l)
    return (F, vect_u)

def somme_forces(i):
    somme_f = [0,0]
    for j in range(len(graph[i])):

        somme_f[0] += (force(i, j)[0]*force(i, j)[1][0])
        somme_f[1] += (force(i, j)[0]*force(i, j)[1][1])
        print(somme_f)
    return somme_f

Master = Unknown(pos, vit)
root.bind("<f>", Master.ressort)

can.grid(row=0, column=0)

root.mainloop()
