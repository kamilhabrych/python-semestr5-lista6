l = []

for i in range(30+1):
    l.append(3**i-2**i)

l2 = []

for i in range(len(l)):
    l2.append(l[i] % 19)

print(l2)

print(10 in l2)
print(11 in l2)
print()

n = int(input('Podaj n (miedzy 0 a 18):'))

while n < 0 or n > 18:
    print('Wartość nieprawidłowa!')
    n = int(input('Podaj n (miedzy 0 a 18):'))

print()

if (n in l2) == False:
    print("Nie ma tej liczby w l2")
else:
    print("Ta liczba wystepuje w l2 tyle razy:",l2.count(n))