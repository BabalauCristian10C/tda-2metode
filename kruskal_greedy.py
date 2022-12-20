"""
Considerăm un graf neorientat ponderat (cu costuri) conex G.
Se numește arbore parțial un graf parțial al lui G care este arbore. Se numește arbore parțial de cost minim un arbore parțial pentru care suma costurilor muchiilor este minimă.

Dacă graful nu este conex, vorbim despre o pădure parțială de cost minim.

Să se determine unu arbore parțial de cost minim (APM) într-un graf ponderat cu N noduri.
"""

class graf:
    def __init__(self, vertices):
        self.V = vertices
        self.graful = []
    def adauga_margine(self, u, v, w):
        self.graful.append([u, v, w])
    def gaseste(self, parental, i):
        if parental[i] != i:
            parental[i] = self.gaseste(parental, parental[i])
        return parental[i]
    def union(self, parental, grad, x, y):
        if grad[x] < grad[y]:
            parental[x] = y
        elif grad[x] > grad[y]:
            parental[y] = x
        else:
            parental[y] = x
            grad[x] += 1
    def GreedyAPM(self):
        rezultat,i,e = [],0,0
        self.graful = sorted(self.graful,key=lambda item: item[2])
        parental = []
        grad = []
        for node in range(self.V):
            parental.append(node)
            grad.append(0)
        while e < self.V - 1:
            u, v, w = self.graful[i]
            i = i + 1
            x = self.gaseste(parental, u)
            y = self.gaseste(parental, v)
            if x != y:
                e = e + 1
                rezultat.append([u, v, w])
                self.union(parental, grad, x, y)
        minim = 0
        print("Nodurile din APM-ul construit:")
        for u, v, pret in rezultat:
            minim += pret
            print("%d -- %d == %d" % (u, v, pret))
        print("Arborele parțial de cost minim (APM):", minim)

tabel = graf(4)
tabel.adauga_margine(0, 1, 10)
tabel.adauga_margine(0, 2, 6)
tabel.adauga_margine(0, 3, 5)
tabel.adauga_margine(1, 3, 15)
tabel.adauga_margine(2, 3, 4)
tabel.GreedyAPM()