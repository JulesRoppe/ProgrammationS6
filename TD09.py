""" TD 09 """

import copy

class Polynom:
    def __init__(self, coef, n, q):
        for i in range(1, len(coef)):
            if len(coef) - i >= n:
                coef[len(coef) - n - i] += -coef[len(coef) - i]
                coef[len(coef) - i] = 0
        coef = coef[:n]
        for i in range(len(coef)):
            coef[i] = coef[i] % q
        self.coef = coef
        self.n = n
        self.q = q


    def __str__(self):
        coef = self.coef
        polynom = ""
        for i in range(1, len(coef)):
            polynom += f"{coef[len(coef) - i]}*X**{len(coef) - i} + "
        polynom += f"{coef[0]}"
        return polynom


    def __add__(self, other):
        assert self.n == other.n and self.q == other.q
        coef1 = self.coef
        coef2 = other.coef
        coef = []
        for i in range(len(coef1)):
            coef.append(coef1[i] + coef2[i])
        return Polynom(coef, self.n, self.q)


    def __mul__(self, other):
        assert self.n == other.n and self.q == other.q
        coef1 = self.coef
        coef2 = other.coef
        coef = [0 for i in range(len(coef1) + len(coef2))]
        for i in range(len(coef1)):
            for j in range(len(coef2)):
                coef[i + j] += coef1[i] * coef2[j]
        return Polynom(coef, self.n, self.q)


    def scalar(self, c):
        coef = self.coef
        for i in range(len(coef)):
            coef[i] = coef[i] * c
        return Polynom(coef, self.n, self.q)


    def rescale(self, r):
        coef = self.coef
        for i in range(len(coef)):
            coef[i] = coef[i] % r
        return Polynom(coef, self.n, self.q)


    def fscalar(self, r, c):
        coef = self.coef
        coef_Q = [0]*len(self.coef)
        for i in range(len(coef)):
            coef_Q[i] = int(coef[i] * c) % r
        return Polynom(coef_Q, self.n, self.q)


if __name__ == '__main__':
    """ Exercice 1 """
    # La méthode utilisée consiste à prendre un polynôme quelconque et à trouver sa forme dans Z_q[x]/(x^n+1)Z_q[x].
    # C'est le constructeur qui se charge de transformer le polynôme quelconque.
    P1 = Polynom([1, 0, 2, -4, 1], 2, 5)
    print("P1 =", f"{P1},", "coefficients:", P1.coef)


    """ Exercice 2 """
    # On peut vérifier par des exemples que __add__ fonctionne:
    P2 = Polynom([3, 3], 2, 5)
    print("P2 =", f"{P2},", "coefficients:", P2.coef, "\n")
    P_sum = P1.__add__(P2)
    print("P1 + P2 =", f"{P_sum},", "coefficients:", P_sum.coef, "\n")


    """ Exercice 3 """
    # On peut vérifier par des exemples que __mul__ fonctionne:
    P_mul = P1.__mul__(P2)
    print("P1 * P2 =", f"{P_mul},", "coefficients:", P_mul.coef, "\n")


    """ Exercice 4 """
    # De même, on peut vérifier par des exemples que les fonctions scalar, rescale et fscalar fonctionnent:
    c = 1.5
    P3 = copy.deepcopy(P1)
    P3 = P3.scalar(c)
    # Ici P1 vaut 4X d'où 6X par multiplication avec c=1.5 puis 1 par modulo q=5
    print("P1 * c =", f"{P3},", "coefficients:", P3.coef)

    r = 3
    P4 = copy.deepcopy(P1)
    P4 = P4.rescale(r)
    # Ici P1 vaut 4X d'où 1 par modulo r=3
    print("P1 dans Z_r[x]/(x^n+1)Z_r[x]:", f"{P4},", "coefficients:", P4.coef)

    P5 = copy.deepcopy(P1)
    P5 = P5.fscalar(r, c)
    # Ici P1 vaut 4X, d'ou 6X par multiplication avec c=1.5 puis 0 par modulo r=3
    print("P1 par fscalar(r,c):", f"{P5},", "coefficients:", P5.coef)