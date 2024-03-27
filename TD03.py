""" TD03 """

class Tree:
    def __init__(self, label, *children):
        self.label = label
        self.children = children

    def __label__(self):
        return str(self.label)

    def __children__(self):
        return self.children

    def nb_children(self):
        return len(self.children)

    def child(self, i: int):
        return self.children[i]

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def depth(self):
        rep = []
        if self.is_leaf():
            rep.append(0)
        else:
            for i in range(len(self.children)):
                rep.append(self.child(i).depth() + 1)
        return max(rep)

    def __str__(self):
        rep = self.__label__()
        if self.is_leaf():
            return rep
        else:
            rep += "("
            for i in range(len(self.children)):
                rep += f"{self.child(i).__str__()},"
            rep = rep[:len(rep)-1]
            rep += ")"
            return rep

    def __eq__(self, other: object):
        if len(self.children) != len(other.children):
            return False
        else:
            for i in range(len(self.children)):
                if other.child(i).__str__().__eq__(self.child(i).__str__()) == False:
                    return False
        return True

if __name__ == '__main__':
    A = Tree('f', Tree('a', Tree('b', Tree('e')), Tree('c')), Tree('b'))
    B = Tree('f', Tree('a', Tree('b', Tree('e')), Tree('c')), Tree('b'))
    print(id(A), id(B))
    print(A.__str__())
    print(A.__eq__(B))
