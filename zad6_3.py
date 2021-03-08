from math import factorial

n = 1000

silnia = factorial(n)

ln = list(str(silnia))

for i in range(10):
    print(i, '->', ln.count(str(i)))