""" TD03 """

class Tree:
    def __init__(self, __label, *__children):
        self.__label = __label
        self.__children = __children

    def label(self):
        return str(self.__label)

    def children(self):
        return self.__children

    def nb_children(self):
        return len(self.children())

    def child(self, i: int):
        return self.__children[i]

    def is_leaf(self):
        if len(self.children()) == 0:
            return True
        else:
            return False

    def depth(self):
        rep = []
        if self.is_leaf():
            rep.append(0)
        else:
            for i in range(len(self.children())):
                rep.append(self.child(i).depth() + 1)
        return max(rep)

    def __str__(self):
        rep = self.label()
        if self.is_leaf():
            return rep
        else:
            rep += "("
            for i in range(len(self.children())):
                rep += f"{self.child(i).__str__()},"
            rep = rep[:len(rep)-1]
            rep += ")"
            return rep

    def __eq__(self, other: object):
        if len(self.children()) != len(other.children()):
            return False
        else:
            for i in range(len(self.children())):
                if not other.child(i).__str__().__eq__(self.child(i).__str__()):
                    return False
        return True

    def deriv(self, var: str):

        noeud = self.label()
        for i in range(len(self.children())):
            noeud = self.child(i)
            if self.child(i) == '+' or '*':
                noeud = self.child(i)
        return


if __name__ == '__main__':
    A = Tree('f', Tree('a', Tree('b', Tree('e')), Tree('c')), Tree('b'))
    B = Tree('f', Tree('a', Tree('b', Tree('e')), Tree('c')), Tree('b'))
    print(id(A), id(B))
    print(A.__str__())
    print(A.__eq__(B))
