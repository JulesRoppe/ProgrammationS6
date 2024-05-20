""" TD06 """

import tkinter as tk
import random
import numpy as np

root = tk.Tk()

WIDTH = 500
HEIGHT = 500
can = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')

graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

graph2 = [[1, 2, 3, 4],[2],[3],[4],[1]]

pos = np.array([(random.random()*WIDTH, random.random()*HEIGHT) for i in range(len(graph))])
vit = np.array([((random.random() - 0.5), (random.random() - 0.5)) for i in range(len(graph))])

class Unknown:
    def __init__(self, pos, vit):
        self.pos = pos
        self.vit = vit


    def elastique(self, event):
        can.delete("all")
        self.vit = self.vit + np.array([(self.somme_forces_elastique(i)[0]*tau, self.somme_forces_elastique(i)[1]*tau)
                                        for i in range(len(graph))])
        self.pos = self.pos + tau * self.vit
        self.draw(can, graph, self.pos)
        return

    def elastique_frottements(self, event):
        can.delete("all")
        self.vit = self.vit + np.array([(self.somme_forces_elastique(i)[0]*tau, self.somme_forces_elastique(i)[1]*tau)
                                        for i in range(len(graph))])
        self.vit = self.vit - a*tau*(self.vit)
        for i in range(len(graph)):
            if self.vit[i][0] < 0.001:
                self.vit[i][0] = 0
            if self.vit[i][1] < 0.001:
                self.vit[i][1] = 0

        self.pos = self.pos + tau * self.vit
        self.draw(can, graph, self.pos)
        return

    def elastique_frottements_repulsion(self, event):
        can.delete("all")
        self.vit = self.vit + np.array([(self.somme_forces_elastique(i)[0]*tau, self.somme_forces_elastique(i)[1]*tau)
                                        for i in range(len(graph))]) \
                   + np.array([(self.somme_forces_repulsion(i)[0]*tau, self.somme_forces_repulsion(i)[1]*tau)
                                        for i in range(len(graph))])

        self.vit = self.vit - a * tau * (self.vit)
        for i in range(len(graph)):
            if self.vit[i][0] < 0.001:
                self.vit[i][0] = 0
            if self.vit[i][1] < 0.001:
                self.vit[i][1] = 0

        self.pos = self.pos + tau * self.vit
        self.draw(can, graph, self.pos)


    def elastique(self, i, j):
        l = np.sqrt((self.pos[i][0] - self.pos[j][0]) ** 2 + (self.pos[i][1] - self.pos[j][1]) ** 2) + 0.001
        F = k * (l - l0)
        vect_u = ((self.pos[j][0] - self.pos[i][0]) / l, (self.pos[j][1] - self.pos[i][1]) / l)
        return (F, vect_u)

    def somme_forces_elastique(self, i):
        somme_F = [0, 0]
        vect_unitaire_somme_F = [0, 0]
        for j in range(len(graph[i])):
            F, vect_unitaire_F = self.elastique(i, j)[0], self.elastique(i, j)[1]
            somme_F[0] += (F * vect_unitaire_F[0])
            somme_F[1] += (F * vect_unitaire_F[1])
        return somme_F

    def repulsion(self, i, j):
        r = np.sqrt((self.pos[i][0] - self.pos[j][0]) ** 2 + (self.pos[i][1] - self.pos[j][1]) ** 2) + 0.001
        F = - e * (1 / (r**1))
        vect_u = ((self.pos[j][0] - self.pos[i][0]) / r, (self.pos[j][1] - self.pos[i][1]) / r)
        return (F, vect_u)

    def somme_forces_repulsion(self, i):
        somme_F = [0, 0]
        vect_unitaire_somme_F = [0, 0]
        for j in range(len(graph)):
            F, vect_unitaire_F = self.repulsion(i, j)[0], self.repulsion(i, j)[1]
            somme_F[0] += (F * vect_unitaire_F[0])
            somme_F[1] += (F * vect_unitaire_F[1])
        return somme_F


    def draw(self, can, graph, pos):

        #témoin du déplacement du barycentre
        can.create_rectangle(WIDTH/2-20, HEIGHT/2-20, WIDTH/2+20, HEIGHT/2+20, fill="red")

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


k = 0.4
l0 = 100
tau = 0.1
a = 0.05
e = 1000
if __name__ == '__main__':
    Master = Unknown(pos, vit)
    Master.draw(can, graph, pos)

root.bind("<f>", Master.elastique_frottements_repulsion)

can.grid(row=0, column=0)

root.mainloop()
