""" Test Jules Roppé 12/06/2024 """
import copy

""" Question 1 """

# On peut représenter le labyrinthe par une liste de liste ou l'indice i de la liste (le carrefour i) contient la liste
# des carrefours accessibles. Les indices des listes de liste correspondent au numéro de la porte. C'est un graphe!

exemple_7_carrefour = [[2, 1, 3], [0], [4, 0, 3], [5, 0, 2], [6, 2], [6, 3], [4, 5]]

""" Question 2 """


def chemin_labyrinthe(labyrinthe, start, chemin):
    """ Retourne la sortie du labyrinthe """
    carrefour_occupied = start  # le carrefour occupé actuellement!
    for i in range(len(chemin)):
        door_choice = chemin[i]
        if door_choice <= len(labyrinthe[carrefour_occupied]):  # Cette condition if s'assure que la porte "choix_porte"
            # est bien accessible depuis le carrefour i. Sinon, on reste sur place.
            carrefour_occupied = labyrinthe[carrefour_occupied][door_choice]
    return carrefour_occupied


print(chemin_labyrinthe(exemple_7_carrefour, 2, [2, 0, 0]))

""" Question 3 """


def nbe_carrefour_doublon(labyrinthe, start, chemin):
    """
    Compte le nombre de carrefours visités deux fois
    :param labyrinthe: graphe, liste de liste
    :param start: integer
    :param chemin: list
    :return: integer
    """
    nbe_doublon = []
    for i in range(len(labyrinthe)):
        nbe_doublon.append(0)
    carrefour_occupied = start
    nbe_doublon[carrefour_occupied] += 1  # Le départ compte comme une visite. Si arrivée = départ, il sera compté comme
    # un doublon

    for i in range(len(chemin)):
        door_choice = chemin[i]
        if door_choice <= len(labyrinthe[carrefour_occupied]):  # Même condition qu'en question 2
            carrefour_occupied = labyrinthe[carrefour_occupied][door_choice]
            nbe_doublon[carrefour_occupied] += 1

    counter_doublon = 0  # Compte le nombre de carrefour visité deux fois.
    for i in range(len(nbe_doublon)):
        if nbe_doublon[i] >= 2:
            counter_doublon += 1
    return counter_doublon


print(chemin_labyrinthe(exemple_7_carrefour, 2, [1, 1, 0, 1, 0, 1, 2]))

""" Question 4 """


def toutes_portes(labyrinthe, start, chemin):
    nbe_passage = []  # L'indice i correspond au carrefour i, la valeur son nombre de visite.
    for i in range(len(labyrinthe)):
        nbe_passage.append(0)
    carrefour_occupied = start
    nbe_passage[carrefour_occupied] += 1

    for i in range(len(chemin)):
        door_choice = chemin[i]
        if door_choice <= len(labyrinthe[carrefour_occupied]):
            carrefour_occupied = labyrinthe[carrefour_occupied][door_choice]
            nbe_passage[carrefour_occupied] += 1

    for i in range(len(nbe_passage)):
        if nbe_passage[i] == 0:
            return False
    return True


print(toutes_portes(exemple_7_carrefour, 1, [0, 2, 0, 0, 0, 1, 1]))

""" Question 5 """

# Une boucle se caractérise par le nombre de visite des carrefours. En effet, si deux carrefours forment une boucle,
# leur seconde visite se fera l'une après l'autre. Il faut donc identifier les boucles en regardant si certaines
# deuxièmes visites se font les unes après les autres. Je n'ai pas eu le temps de finir, l'idée étaient de supprimer
# les passages du chemin l'orsque l'on observait des deuxièmes visites qui se suivent.

def simplifie_chemin(labyrinthe, start, chemin):
    nbe_passage = []

    nouveau_chemin = copy.deepcopy(chemin)

    for i in range(len(chemin)):
        nbe_passage.append(0)
    carrefour_occupied = start
    nbe_passage[carrefour_occupied] += 1

    for i in range(len(start)):
        door_choice = chemin[i]
        if door_choice <= len(labyrinthe[carrefour_occupied]):
            carrefour_precedent = carrefour_occupied
            carrefour_occupied = labyrinthe[carrefour_occupied][door_choice]
            nbe_passage[carrefour_occupied] += 1

            if (nbe_passage[carrefour_occupied] or nbe_passage[carrefour_precedent]) <= 2:
                nouveau_chemin.append(door_choice)


