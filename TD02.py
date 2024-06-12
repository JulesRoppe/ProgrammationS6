""" TD02 de Programmation et Structure de Données S6 """
import math


""" Cours 02"""

class counter:
    def __init__(self):
        self.value = 0

if __name__ == '__main__':
    c = counter()
    # print(c.value)

a = 5
# print(f"my value is {c.value}")


""" Exercice 1 """

class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        num = self.num * other.denom + self.denom * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __mul__(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def simplify(self):
        pgcd = math.gcd(self.num, self.denom)
        num = self.num // pgcd
        denom = self.denom // pgcd
        return Fraction(num, denom)

if __name__ == '__main__':
    frac = Fraction(5,3)
    print(frac)
    f1 = Fraction(10, 2)
    f2 = Fraction(10, 2)
    g = f1.__add__(f2)
    print(g)
    print(f1.simplify(), "\n")


""" Exercice 3 """

def H(n):
    """ Calcule la somme des inverses de 1 à n """
    harmonique = Fraction(1, 1)
    for i in range(2, n + 1):
        harmonique = harmonique.__add__(Fraction(1, i))
        harmonique = harmonique.simplify()
    return harmonique

print(H(5))


""" Exercice 4 """


def Liebnitz(n):
    """
    Fonction qui calcule la somme de Liebnitz jusqu'à n
    :param n: limite de la somme
    :return: valeur de la somme
    """
    lieb = Fraction(1, 1)
    for i in range(1, n + 1):
        lieb = lieb.__add__(Fraction((-1)**i, 2*i+1))
        lieb = lieb.simplify()
    return lieb

print(Liebnitz(7), "\n")


""" Exercice 5 """


class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __str__(self):
        coef = self.coef
        polynom = ""
        for i in range(1, len(coef)):
            polynom += f"{coef[len(coef) - i]}*X**{len(coef) - i} + "
        polynom += f"{coef[0]}"
        return polynom

    def __add__(self, other):
        """ On somme les coefficients jusqu'à atteindre le degré max du polynôme de degré minimal puis on concatène
         le reste """
        self_coef = self.coef
        other_coef = other.coef
        coef = list()
        len1 = len(self_coef)
        len2 = len(other_coef)
        for i in range(min(len1, len2)):
            coef.append(self_coef[i] + other_coef[i])
        if len1 > len2:
            coef = coef + self_coef[len2:]
        else:
            coef = coef + other_coef[len1:]
        return Polynomial(coef)


    def deriv(self):
        """
        Fonction qui dérive un polynôme
        :param self: polynôme à dériver
        :return: polynôme dérivé
        """
        coef = self.coef
        deriv_coef = []
        for i in range(1, len(coef)):
            deriv_coef.append(i*coef[i])
        return Polynomial(deriv_coef)


    def integrate(self, const):
        """
        Fonction qui intègre un polynôme
        :param self: polynôme à intégrer
        :param const: constante d'intégration
        :return: polynôme intégré
        """
        coef = self.coef
        integ_coef = [const]
        for i in range(1, len(coef)+1):
            integ_coef.append(coef[i-1]/i)
        return Polynomial(integ_coef)


if __name__ == '__main__':
    P1 = Polynomial([2,4,4])
    P2 = Polynomial([2,1,2,2,6,2,21])
    print(P1)
    print(P1.deriv())
    print(P1.integrate(1))








