""" TD03 """
import ctypes.macholib.dyld


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
        return self.nb_children() == 0

    def depth(self):
        rep = []
        if self.is_leaf():
            rep.append(0)
        else:
            for i in range(self.nb_children()):
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

    def __eq__(self, other):
        if len(self.children()) != len(other.children()):
            return False
        for i in range(len(self.children())):
            if not other.child(i).__str__().__eq__(self.child(i).__str__()):
                return False
        return True

    def deriv(self, variable: str):
        if self.depth() == 0:
            if self.label() != variable:
                return Tree(0)
            return Tree(1)
        if self.label() == '+':
            return Tree('+', self.child(0).deriv(variable), self.child(1).deriv(variable))
        if self.label() == '*':
            return Tree('+', Tree('*', Tree(self.child(0).deriv(variable)), Tree(self.child(1))),
                        Tree('*', Tree(self.child(0)), Tree(self.child(1).deriv(variable))))

    def substitute(self, t1, t2):
        """ non fini """
        if self == t1:
            return t2
        for i in range(self.nb_children()):
            if self.child(i) == t1:
                return Tree(self.label(), self.children())
            else:
                return self.child(i).substitute(t1, t2)
        return self.__str__()


if __name__ == '__main__':
    A = Tree('+', Tree('*', Tree(3), Tree('*', Tree('X'), Tree('X'))), Tree('*', Tree('2'), Tree('X')))
    B = Tree('*', Tree(5), Tree('X'))
    C = Tree('a')
    D = Tree('X')
    #print(id(A), id(B))
    print(B.__str__())
    print(B.depth())
    #print(A.__eq__(B))
    print(A.deriv('X'))
    print(Tree('+', Tree('a'), Tree('X')).deriv('X'))
    B.substitute(C, D)