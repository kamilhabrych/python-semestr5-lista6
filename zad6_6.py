from math import factorial

l = []

for i in range(1,100+1):
    l.append(1/i)

print('Suma:',sum(l))
print()
print('Wartość minimalna:',min(l))
print()
print('Wartość maksymalna:',max(l))

silnia = factorial(1000)

lz = list(str(silnia))
lz2 = []

for i in range(len(lz)):
    lz2.append(int(lz[i]))

print()
print('Suma cyfr 1000!:',sum(lz2))