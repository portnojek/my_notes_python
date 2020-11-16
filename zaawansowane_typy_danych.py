'''Lista - pojemnik do przechowywania elementów, która jest numerowana od 0
Przykład listy :
imiona = [ “Arkadiusz”, “Wioletta”, “Karol”, “Kuba”, “Adrian” ]
                0            1          2       3         4
imiona - nazwa listy
[ ] - klamra kwadratowa, która oznacza że tworzymy listę
“Arkadiusz”, “Wioletta”, “Karol”, “Kuba”, “Adrian” - elementy listy
0,1,2,3,4 - indeksy (numery) konkretnej pozycji elementu w liście
W liście możemy mieszać wartości. Do elementów listy możemy się szybko odwołać np.
a) aby wypisać wszystkie elementy z listy:
print(imiona)
b) aby wybrać dany element z listy
print(nazwa_listy[indeks_elementu_do_którego_chcemy_się_odwołać])
np. ostatni element:
print(imiona[ -1 ])
'''

'''Krotka - to pojemnik do przechowywania wartości. Zawartości krotki nie możemy później
zmienić.
Krotkę możemy tworzyć na dwa sposoby :
a) krotka = 1, 42, 12, -4 tj. bez nawiasów
b) krotka = (1,42,12,-4) przy pomocy okrągłych nawiasów
Z krotki korzystamy, gdy spodziewamy się wartości zmiennych, które będą niezmienialne do
końca działania programu. Krotka pozwala na zaoszczędzenie miejsca w pamięci, jak
również przyspieszenie sprawności programu. '''

''' dictionary - z ang. słownik
Słownik to pojemnik do przechowywania danych. Każdy element słownika składa się z
klucza i przypisanej mu wartości. Do klucza przypisywana jest jedna wartość. Klucze muszą
być unikalne (nie mogą się powtórzyć ich nazwy), natomiast wartość może się powtarzać.
Przykładowy słownik
pokoje = { 49 : 'Arkadiusz Włodarczyk' , 69 : 'Wioletta Włodarczyk' }
pokoje - nazwa słownika
{ } - klamry do utworzenia słownika
49, 69 - klucz
'Arkadiusz Włodarczyk' - wartość
● Aby pobrać wartość wpisujemy nazwę słownika, a po niej nazwę klucza w
kwadratowych nawiasach np.
pokoje[ 49 ] lub za pomocą funkcji get pokoje.get( 49 )
● Aby dodać wartość tworzymy nowy klucz i przypisujemy mu wartość lub za
pomocą funkcji update (z ang.aktualizuj) np.
pokoje.update({ 499 : 'Jasiu Kokoszka' })
● Aby usunąć wartość ze słownika
- za pomocą del (z ang. usunąć)
del (pokoje[ 499 ])
- za pomocą funkcji pop, która usuwa, ale zarazem zwraca wartość, która
została usunięta
pokoje.pop( 400 )
- funkcja popitem usuwa ostatni element i również go zwraca do użytku
pokoje.popitem()
● Aby sprawdzić ilość elementów w słowniku używamy :
len(pokoje)
● Aby wyczyścić słownik z elementów
pokoje.clear()'''

'''
Porównanie typów danych
⇣ ⇢
        Elementy
        unikalne
                            Kolejność
                                            Zmiana
                                            konkretnego
                                            elementu
                                                                Nowe
                                                                elementy
LISTY       NIE             TAK             TAK                 TAK
KROTKI      NIE             TAK             NIE                 NIE
SŁOWNIKI    TAK             NIE             TAK                 TAK
ZBIORY      TAK             NIE             NIE                 TAK

ZBIORY BONUS W POSTACI | - ^ &

Zbiór - pojemnik do przechowywania danych, tworzymy go za pomocą { } zbiory nie mają
kluczy, tylko wartości. W zbiorach elementy muszą być unikalne tzn. że nie mogą się
powtarzać. Dane pobierane z bazy danych w zbiorach zmieniają kolejność. Nie jesteśmy w
stanie zmienić konkretnego elementu, natomiast do zbioru można dodać element.
Przykładowy zbiór
A = { 1 , 4 , 20 , -4 , 6 }
Aby dodać element do zbioru:
add - (z ang.dodać)
A.add( 7 )
print(A)
Aby przetworzyć listę A = [1, 4, 20, -4, 20]
w zbiór o unikalnych wartościach i usunąć duplikaty używamy funkcji set
print(set(A))
Wykonywanie dodatkowych operacji na zbiorach:
A = { 1 , 4 , 20 , -4 , 6 }
B = { 2 , 1 , 25 , 40 , 20 }
● sprawdzanie wspólnych elementów w zbiorach (koniunkcja)
print(A&B)
● jakie są wszystkie elementy w obu zbiorach (suma)
print(A|B)
● zbiór elementów, które były w A, ale nie ma ich w B
print(A-B)
● alternatywa wykluczająca tzn. wyklucza wspólne wartości
print(A^B)
● discard - usunięcie elementu ze zbioru np. aby usunąć ze zbioru A element o
wartości: 20
A.discard(20)
print(A) '''


moja_lista = [1, 45, 'Bartek', 'krzesło', 34.54, 9.838327]
moja_krotka = (1, 45, 'Bartek', 'krzesło', 34.54, 9.838327)
moj_slownik = {'Ela': 39, 'Bartek': 36, 'Szymon': 7, 'Nina': 1}
pokoje = {49 : 'Arkadiusz Włodarczyk' , 69 : 'Wioletta Włodarczyk'}
moj_zbior = {23, 45, 666, 234, 12, 44, 5, 66, 89}
wartosc = pokoje.get(39)
wartosc2 = moj_slownik.get('Ela')
A = { 1 , 4 , 20 , -4 , 6 }
B = { 2 , 1 , 25 , 40 , 20 }
print(wartosc, wartosc2)
print(moj_slownik.get('Bartek'))
print(len(moja_lista))
moja_lista.append('santander')
print(len(moja_lista))
print(moja_lista)
moja_lista.extend('grawitacja')
print(moja_lista)
print(moja_krotka)
print(moj_zbior)
print(type(moj_zbior)) # zwraca informację o typie danych 
print(len(moj_zbior))
moj_zbior.add('storno') # dodawanie wartosci do zbioru
print(moj_zbior)
print(set(moja_krotka)) # zamiana krotki w zbiór
print(A&B) # wspólne wlementy w zbiorach
print(A|B) # jakie sa wszystkie elementy w obu zbiorach (suma)
print(A-B) # zbiór elementów które były w A a nie ma w B
print(A^B) # wyklucza wspólne wartości
A.discard(20) # usunięcie elementu ze zbioru 
print(A)
print(moja_lista.pop(1))
print(moja_lista)