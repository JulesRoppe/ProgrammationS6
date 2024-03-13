""" TD01 programmation """
import string
import random

with open("frenchssaccent.dic", 'r') as f:
    text = f.read()
lexique = text.split("\n")

l = list(string.ascii_lowercase)


n = 8
tirage = list()
for i in range(n):
    j = random.randint(0,25)
    tirage.append(l[j])

""" Exercice 2 """
def sac():
    mots_possibles = []
    for ligne in lexique:
        compteur = 1
        for letter in ligne:
            if letter not in tirage:
                compteur = 0
        if compteur == 1:
            mots_possibles.append(ligne[0:len(ligne)-1])
    return mots_possibles


def solution():
    liste = sac()
    sol = liste[0]
    for i in range(len(liste) - 1):
        if len(sol) < len(liste[i+1]):
            sol = liste[i+1]
    return sol

print(sac())
print(tirage)
print(solution())


""" Exercice 3 """
def all_solutions():
    sol = solution()
    liste_solutions = list()
    mots_possibles = sac()
    for mot in mots_possibles:
        if len(mot) == len(sol):
            liste_solutions.append(mot)
    return liste_solutions


def solution_score_maximal():
    liste_solutions = all_solutions()
    liste_score = list()
    l1 = ['a','e','i','l','n','o','r','s','t','u']
    l2 = ['d','g','m']
    l3 = ['b','c','p']
    l4 = ['f','h','v']
    l8 = ['j','q']
    l10 = ['k','w','x','y','z']
    for sol in liste_solutions:
        score = 0
        for letter in sol:
            if letter in l1:
                score +=1
            if letter in l2:
                score +=2
            if letter in l3:
                score +=3
            if letter in l4:
                score +=4
            if letter in l8:
                score +=8
            if letter in l10:
                score +=10
        liste_score.append(score)
    score_maximal = max(liste_score)
    solution_score_maximal = liste_solutions[liste_score.index(score_maximal)]
    return solution_score_maximal


print(solution_score_maximal())