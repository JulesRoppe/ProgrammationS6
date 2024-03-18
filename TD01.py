""" TD01 programmation """
import string
import random

with open("frenchssaccent.dic", 'r') as f:
    text = f.read()
lexique = text.split("\n")

alphabet = list(string.ascii_lowercase)
n = 8
tirage = list()
for i in range(n):
    j = random.randint(0,25)
    tirage.append(alphabet[j])


""" Exercice 2 """
def mots_possibles(tirage):
    liste_mots_possibles = []
    for mot in lexique:
        copie_tirage = tirage.copy()
        compteur = 1

        for lettre in mot:
            if lettre not in copie_tirage:
                compteur = 0
            else:
                copie_tirage.remove(lettre)
        if compteur == 1:
            liste_mots_possibles.append(mot[0:len(mot)-1])
    return liste_mots_possibles


def solution():
    liste = mots_possibles(tirage)
    sol = liste[0]
    for i in range(len(liste) - 1):
        if len(sol) < len(liste[i+1]):
            sol = liste[i+1]
    return sol


""" Exercice 3 """

def score(mot):
    score_mot = 0
    l1 = ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
    l2 = ['d', 'g', 'm']
    l3 = ['b', 'c', 'p']
    l4 = ['f', 'h', 'v']
    l8 = ['j', 'q']
    l10 = ['k', 'w', 'x', 'y', 'z']
    for lettre in mot:
        if lettre in l1:
            score_mot += 1
        if lettre in l2:
            score_mot += 2
        if lettre in l3:
            score_mot += 3
        if lettre in l4:
            score_mot += 4
        if lettre in l8:
            score_mot += 8
        if lettre in l10:
            score_mot += 10
    return score_mot


def max_score(liste_mots_possibles):
    liste_score = list()
    for mot in liste_mots_possibles:
        liste_score.append(score(mot))
    score_max = max(liste_score)
    indice_mot_score_max = liste_score.index(score_max)
    return (liste_mots_possibles[indice_mot_score_max], score_max)


""" Exercice 4 """

alphabet_joker = list(string.ascii_lowercase) + ['?']
n = 8
tirage_joker = list()
compteur = 0
taille = 26
for i in range(n):
    j = random.randint(0,taille)
    tirage_joker.append(alphabet_joker[j])
    if j == 26:
        alphabet_joker.remove('?')
        taille -= 1


def mots_possibles_joker():
    """ On rajoute la possiblité du joker: il n'est disponible qu'une fois et permet de sauter la verification sur
     la lettre en question """
    liste_mots_possibles = []
    if '?' not in tirage_joker:
        return mots_possibles(tirage_joker)
    else:
        for mot in lexique:
            copie_tirage_joker = tirage_joker.copy()
            compteur = 1

            for lettre in mot:
                if lettre not in copie_tirage_joker:
                    if '?' in copie_tirage_joker:
                        compteur = 1
                        copie_tirage_joker.remove('?')
                    else:
                        compteur = 0
                else:
                    copie_tirage_joker.remove(lettre)
            if compteur == 1:
                liste_mots_possibles.append(mot[0:len(mot)-1])
        return liste_mots_possibles


def score_joker(mot):
    score_mot = 0
    copie_tirage_joker = tirage_joker.copy()
    if '?' in tirage_joker:
        copie_tirage_joker.remove('?')
    l1 = ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
    l2 = ['d', 'g', 'm']
    l3 = ['b', 'c', 'p']
    l4 = ['f', 'h', 'v']
    l8 = ['j', 'q']
    l10 = ['k', 'w', 'x', 'y', 'z']
    for lettre in mot:
        if lettre in copie_tirage_joker:
            if lettre in l1:
                score_mot += 1
            if lettre in l2:
                score_mot += 2
            if lettre in l3:
                score_mot += 3
            if lettre in l4:
                score_mot += 4
            if lettre in l8:
                score_mot += 8
            if lettre in l10:
                score_mot += 10
        else:
            score_mot += 1
    return score_mot


def max_score_joker(liste_mots_possibles):
    liste_score = []
    score_max_joker = 0
    for mot in liste_mots_possibles:
        liste_score.append(score_joker(mot))
    print(liste_score)
    score_max_joker = max(liste_score)
    indice_mot_score_max = liste_score.index(score_max_joker)
    return (liste_mots_possibles[indice_mot_score_max], score_max_joker)



print(mots_possibles_joker())
print(tirage_joker)
print(max_score_joker(mots_possibles_joker()))