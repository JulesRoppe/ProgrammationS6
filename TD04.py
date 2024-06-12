""" TD04 """
import matplotlib.pyplot as plt
import os

print(os.listdir())
print([None for i in range(10)] + [None for i in range(10)])
with open("frenchssaccent.dic", 'r') as f:
    text = f.read()
lexique = text.split("\n")

class Hashtable:
    def __init__(self, hash, N):
        self.hash = hash
        self.table = []
        self.__length = N
        for i in range(N):
            self.table.append(None)

    def put(self, key, value):
        index = self.hash(key)%len(self.table)
        if self.table[index] == None:
            self.table[index] = [(key, value)]
        else:
            counter = 0
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)
                    counter = 1
            if counter == 0:
                self.table[index].append((key, value))
        return self

    def get(self, key):
        index = self.hash(key)%len(self.table)
        if self.table[index] == None:
            return None
        else:
            return self.table[index][0][1]

    def repartition(self):
        y = [0 for i in range(len(self.table))]
        N = len(y)
        x = range(N)
        for index in range(N):
            if self.table[index] != None:
                y[index] = len(self.table[index])
        print(y)
        width = 1 / 1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def resize2(self):
        new_table = Hashtable(self.hash, 2*len(self.table))
        for index in range(len(self.table)):
            if self.table[index] != None:
                for j in range(len(self.table[index])):
                    key = self.table[index][j][0]
                    new_table.put(key, self.hash(key))
        self.table = new_table.table
        return self


    def resize (self) :
        """double the length of the hashtable"""
        new_hashtable = [[] for i in range (self.__length * 2)]
        hash_function = self.hash
        length = self.__length * 2
        for index in range (len(self.table)):
            if self.table[index] != None:
                for couple in self.table[index]:
                    new_index = hash_function(couple[0])%length
                    Test = True
                    for i, item in enumerate(new_hashtable[new_index]):
                        if item[0] == couple[0]:
                            new_hashtable[new_index][i] = couple
                            Test = False
                    if Test :
                        new_hashtable[new_index].append(couple)
        self.__table = new_hashtable
        self.__length = length

def hash_naive(key):
    h = 0
    for i in key:
        h += ord(i)
    return h

def hash_better(key):
    return sum([ord(key[i]) * 33**i for i in range(len(key))])

if __name__ == '__main__':
    print(hash_naive('abc'))
    ht = Hashtable(hash_better, 320)
    nombre_element = 0
    for i in range(len(lexique)):
        mot = lexique[i]
        ht.put(mot, len(mot))
        if i > 1.2*len(ht.table):
            ht.resize()

    ht.repartition()



