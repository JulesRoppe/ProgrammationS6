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
graph2 = [[1, 2],[0],[0]]

pos = np.array([(random.random()*WIDTH, random.random()*HEIGHT) for i in range(len(graph))])
vit = np.array([((random.random() - 0.5), (random.random() - 0.5)) for i in range(len(graph))])

class Unknown:
    def __init__(self, pos, vit):
        self.pos = pos
        self.vit = vit

    def ressort(self, event):
        can.delete("all")
        self.vit = self.vit + np.array([(self.somme_forces(i)[0]*tau, self.somme_forces(i)[1]*tau) for i in range(len(graph))])
        self.pos = self.pos + tau * self.vit
        self.draw(can, graph, self.pos)

    def force(self, i, j):
        l = np.sqrt((self.pos[i][0] - self.pos[j][0]) ** 2 + (self.pos[i][1] - self.pos[j][1]) ** 2) + 0.001
        F = k * (l - l0)
        vect_u = ((self.pos[j][0] - self.pos[i][0]) / l, (self.pos[j][1] - self.pos[i][1]) / l)
        return (F, vect_u)

    def somme_forces(self, i):
        somme_f = [0, 0]
        for j in range(len(graph[i])):
            somme_f[0] += (self.force(i, j)[0] * self.force(i, j)[1][0])
            somme_f[1] += (self.force(i, j)[0] * self.force(i, j)[1][1])
        return somme_f

    def draw(self, can, graph, pos):
        can.create_rectangle(100, 100, 200, 200, fill="red")
        barycentre_x, barycentre_y = 0, 0
        for i in range(len(graph)):
            barycentre_x += self.pos[i][0]/len(graph)
            barycentre_y += self.pos[i][1]/len(graph)
            for j in graph[i]:
                can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for (x, y) in pos:
            can.create_oval(x-4,y-4,x+4,y+4,fill="black")
        can.move("all", -(barycentre_x-WIDTH/2), -(barycentre_y-HEIGHT/2))
        return


k = 0.2
l0 = 100
tau = 0.1
if __name__ == '__main__':
    Master = Unknown(pos, vit)
    Master.draw(can, graph, pos)

root.bind("<f>", Master.ressort)

can.grid(row=0, column=0)

root.mainloop()
