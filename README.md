# Lista 6 - Języki programowania wysokiego poziomu

**Python (6) - Listy II**

(1) Niech s=’Ala ma kota’. Przekształć s w listę ls za pomocą konwersji
lz = list(s). Wyświetl lz.
Chcemy teraz wyświetlić w pętli każdy element listy na dwa sposoby. Funckją len uzyskujemy długość listy: len(lz). Dokończ polecenie:
for i in range(len(lz)): .....
Drugi sposób jest taki, że i jest równe kolejnym elementom listy. Dokończ:
for i in lz: ......

(2) Zachowujemy lz z (1). Metoda count zwraca ilość występowania danego elementu w liście. Przykładowa składnia: ile=lista.count(element).
Zlicz ilość ’a’ w liście lz.
Napisz teraz program gdzie wprowadzone jest zdanie s. Następnie s jest
zmienione na listę ls i wyświetlona jest ilość literek a w s.

(3) Niech i będzie liczbą całkowitą. Np. i = 321. Spróbuj zamienić i na
listę (jaki jest błąd?). Aby uzyskać listę cyfr i, najpierw zamieniamy i na
ciąg znaków, s = str(i). Potem tworzymy listę jak w poprzednich zadaniach.
Sprawdź że f actorial wgrana z math (from math import factorial) jest silnią
(np. przetestuj dla 4, 5, 6).
Niech n = 1000!. Zrób z n listę i za pomocą count oblicz ile jest cyfr 9 w n.
Wreszczie zrób to samo dla wszystkich cyfr od 0 do 9. Co można zauważyć?
Zmień 1000! na 2000! i sprawdź ilość każdej z cyfr jeszcze raz.

(4) Niech lz = list(
0Alamakota0
). Wyświetl lz.index(
0a
0
), lz.index(
0m0
),
oraz lz.index(
0k
0
) i zinterpretuj uzyskane wartości. (co jest zwracane jeśli
element występuje wiele razy?)
Przetesuj lz.index(
0
s
0
), skąd błąd?
Zamiast l = l + [element] można stosować l.append(element).
Stwórz listę l składającą się z liczb postaci 3n−2
n dla n od 0 do 30. Wyświetl
na jakiej pozycji znajduje się liczba 1161737179. Potwierdź to obliczając i
wyświetlając 3n − 2
n dla odpowiedniego n.

(5) Widzieliśmy że index generuje błąd jeśli elementu nie ma w liście. Aby
tego uniknąć, możemy sprawdzić czy element jest w liście za pomocą in.
Niech l będzie listą z (4). Stwórz za pomocą pętli listę l2 z elementami:
reszty z dzielenia przez 19 elementów z l.
Wyświetl 10 in l2 oraz 11 in l2. Co uzyskujemy?
Użytkownik wpowadza liczbę n (między 0 a 18). Następnie ma być wyświetlone:
nie ma tej liczby w l2 (lub) ta liczba występuje w l2 (tyle) razy.

(6) Stwórz listę l składającą się z ułamków 1, 1/2, 1/3...,1/100. Wyświetl i
zinterpretuj sum(l), min(l), max(l).
Stwórz listę lz cyfr 1000! jak w (3). Zrób z niej listę liczb całkowitych (konwersję int(...) należy zastosować na każdym elemencie z osobna). Wreszcie
oblicz sumę cyfr 1000!

(7) Znajdź wszystkie pary cyfr występujące w 1000! Przedstaw wynik jako:
00 - występuje ... razy
01 - występuje ... razy
...
99 - występuje ... razy
