"""
Să se scrie un program care determină toate secventele binare de lungime n,
fiecare din ele conținînd nu mai puțin de k cifre de 1.
"""

n=int(input("Introduceti lungimea secventei binare: "))
k=int(input("Introduceti numarul cifrelor de 1: "))

def sol_pos(l):
    if list('{0:b}'.format(l)).count("1")>=k:return True
    else:return False
def prel_sol(x):print('{0:b}'.format(x))

for i in range(2**n):
    if sol_pos(i):
        prel_sol(i)