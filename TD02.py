""" TD02 de Programmation et Structure de Données S6 """
import math

class counter:
    """ Cours 02"""
    def __init__(self):
        self.value = 0

if __name__ == '__main__':
    c = counter()
    print(c.value)

a = 5
print(f"my value is {c.value}")


""" Exercice 1 """

class Fraction:
    def __init__(self, num, denom):
        self.value = f"{num}/{denom}"

if __name__ == '__main__':
    frac = Fraction(5,3)
    print(frac.value)


""" Exerice 2 """

class Fraction2:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def toString(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        num = self.num*other.denom + self.denom*other.num
        denom = self.denom*other.denom
        return Fraction2(num, denom)

    def __mul__(self, other):
        return f"{self.num*other.num}/{self.denom*other.denom}"

    def simplify(self):
        pgcd = math.gcd(self.num, self.denom)
        num = self.num//pgcd
        denom = self.denom//pgcd
        return Fraction2(num, denom)


if __name__ == '__main__':
    f1 = Fraction2(10,2)
    f2 = Fraction2(10,2)
    #g = f1.__add__(f2)
    #print(g.toString())
    #print(f1.simplify())


""" Exercice 3 """

def H(n):
    """ Calcule la somme des inverses de 1 à n """
    harmonique = Fraction2(1, 1)
    for i in range(2, n + 1):
        harmonique = harmonique.__add__(Fraction2(1, i))
        harmonique = harmonique.simplify()
    return harmonique.toString()

#print(H(5))


""" Exercice 4 """


def Liebnitz(n):
    """
    Fonction qui calcule la somme de Liebnitz jusqu'à n
    :param n: limite de la somme
    :return: valeur de la somme
    """
    lieb = Fraction2(1, 1)
    for i in range(1, n + 1):
        lieb = lieb.__add__(Fraction2((-1)**i, 2*i+1))
        lieb = lieb.simplify()
    return lieb.toString()

#print(Liebnitz(7))


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

if __name__ == '__main__':
    P = Polynomial([2,2,2])
    #print(P)


""" Exercice 6 """

class Polynomial2:
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
        return Polynomial2(coef)


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
    return Polynomial2(deriv_coef)


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
    return Polynomial2(integ_coef)


if __name__ == '__main__':
    P1 = Polynomial2([2,4,4])
    P2 = Polynomial2([2,1,2,2,6,2,21])
    #print(P1)
    #print(deriv(P1))
    #print(integrate(P1, 1))


