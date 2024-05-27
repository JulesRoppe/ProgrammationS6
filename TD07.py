""" TD07 """

import tkinter as tk
import random
import numpy as np

root = tk.Tk()

WIDTH = 500
HEIGHT = 500
can = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')

graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343, 98], [298, 326], [187, 475], [245, 407],
       [483, 212], [365, 216], [149, 198])

COLORS = ['white', 'antiquewhite', 'aqua', 'aquamarine', 'bisque', 'black', 'blueviolet', 'brown', 'burlywood',
          'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue',
          'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta',
          'darkolivegreen', 'blue', 'red', 'green']

col_index = [0, 1, 16, 3, 4, 5, -3, 6, -2, 10, 9, -1]


def draw(can, graph, pos, col_index):
    N = len(graph)
    for e in can.find_all():
        can.delete(e)
    for i in range(N):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for i in range(N):
        x, y = pos[i]
        can.create_oval(x - 6, y - 6, x + 6, y + 6, fill=COLORS[col_index[i]])
        can.create_text(x - 12, y, text=f"{i}")
    return


def min_local(i, graph, col_index):
    composante = col_index
    voisins = graph[i]
    voisins.append(i)

    for l in range(len(graph)):
        for m in graph[l]:
            if m == i:
                voisins.append(l)
                break

    min = voisins[0]
    for j in range(len(voisins) - 1):
        if min > voisins[j + 1]:
            min = voisins[j + 1]

    for k in range(len(graph[i])):
        composante[voisins[k]] = col_index[min]
        composante[i] = col_index[min]
    return composante


def complet(graph):
    composantes_connexes = col_index
    for i in range(len(graph)):
        composantes_connexes = min_local(i, graph, composantes_connexes)
    return composantes_connexes


sommet_x_max, sommet_y_max = int(HEIGHT / 24), int(WIDTH / 24)


def graph_cafe(p):
    graph_hasard = {(i, j): [] for i in range(sommet_x_max+1) for j in range(sommet_y_max+1)}
    pos = [[(i + 1) * 24, (j + 1) * 24] for i in range(sommet_x_max) for j in range(sommet_y_max)]
    for i in range(sommet_x_max+1):
        for j in range(sommet_y_max+1):
            proba = random.random()
            if 0 <= proba < p and i < sommet_x_max:
                graph_hasard[i, j].append((i + 1, j))
            proba = random.random()
            if 0 <= proba < p and j < sommet_y_max:
                graph_hasard[i, j].append((i, j + 1))
    print(graph_hasard)
    return graph_hasard, pos


def color_generator():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


def color_cafe(x_max, y_max):
    liste = []
    for i in range(x_max):
        for j in range(y_max):
            liste.append(color_generator())
    return liste


def draw_cafe(can, graph, pos):
    x_max, y_max = int(HEIGHT / 24), int(WIDTH / 24)
    color = color_cafe(x_max, y_max)
    graph_cle = list(graph.keys())
    for e in can.find_all():
        can.delete(e)
    for i in range(1, sommet_x_max+1):
        for j in range(1, sommet_y_max+1):
            graph_ij = graph[i, j]

            for k in range(len(graph_ij)):
                if graph_ij[k]:
                    can.create_line(i * 24, j * 24, graph_ij[k][0] * 24, graph_ij[k][1] * 24)
                    print(graph_ij[k])
    for i in range(len(pos)):
        x, y = pos[i][0], pos[i][1]
        can.create_oval(x - 6, y - 6, x + 6, y + 6, fill=color[i])
    return


(graph, pos) = graph_cafe(0.4)

min_local(6, graph, col_index)
composante_finale = complet(graph)


draw_cafe(can, composante_finale, pos)

can.grid(row=0, column=0)

root.mainloop()
