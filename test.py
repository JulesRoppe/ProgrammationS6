""" Test 12/06/2024 Programmation et strucutres de données """


class A:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return f"({self.n}, {self.d})"

    def __eq__(self, other):
        return type(self) == type(other) and self.n == other.n

    def mul(self, c):
        self.d *= c
        A(self.n, self.d)

a = A(3, 4)
print(str(a))
b = A(3, 5)
print(a == b)
print(a)
class Tree:
    def __init__(self, symbol, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left == None and self.right == None

    def depth(self):
        if self.is_leaf():
            return 0
        else:
            g = 0 if self.left is None else self.left.depth()
            d = 0 if self.right is None else self.right.depth()
            return 1 + max(g, d)

    def leaves(self):
        g = "" if self.left is None else self.left.leaves()
        d = "" if self.right is None else self.right.leaves()
        return f"{g} {self.symbol} {d}"

def circuit(D, n):
    vus = set()
    avoir = [n]
    while avoir:
        m = avoir.pop()
        vus.add(m)
        for s in D[m]:
            if s == n:
                return True
            elif s not in vus:
                avoir.append(s)
    return False

class Hashtable:
    def __init__(self, size=16):
        self.nb_elem = 0
        self.capacity = size
        self.table = [None] * self.capacity

    def put(self, key, value):
        h = myhash(key) % self.capacity
        if self.table[h] == None:
            self.table[h] = [[key, value]]
        else:
            for p in self.table[h]:
                if p[0] == key:
                    p[1] = value
                    return self.table[h].append([key, value])

    def get(self, key):
        h = myhash(key) % self.capacity
        if self.table[h] == None: return None
        for k,v in self.table[h]:
            if k == key: return v
        return None
