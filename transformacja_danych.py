#first_example_TRANSFORMACJA_LISTY
''' Transformacja listy , czyli przetworzenie starej listy w nową
liczby = [ 1 , 2 , 3 , 4 , 5 , 6 ]
Na podstawie listy “liczby” chcemy stworzyć nową listę np. “potegiDwojki”, czyli
spotęgować każdy z tych elementów przy użyciu pętli for
potegiDwojki = []
for element in liczby:
potegiDwojki.append(element**2)
→ dla każdego elementu wewnątrz listy "liczby"
→ dodajemy do listy "potegiDwojki" przy pomocy funkcji append element , który będzie przy
każdym przejściu zmieniany na 1,2,3,4,5,6 w kolejności i podnoszony do potęgi drugiej
Na podstawie listy liczby możemy także wybrać np. liczby parzyste :
liczby = [ 1 , 2 , 3 , 4 , 5 , 6 ]
liczbyParzyste = []
for element in liczby:
if (element % 2 == 0):
liczbyParzyste.append(element)
W powyższym przykładzie wystąpił warunek . Warunek warunkuje na jakiej
podstawie wybieramy element.
Wyrażenie listowne (formuła) to wyrażenie, które zastępuje jakąś pętle, która działa na
listach. Przy tworzeniu wyrażenia listowego korzystamy z klamer [ ]
liczby = [ 1 , 2 , 3 , 4 , 5 , 6 ]
potegiDwojki2 = [ element**2
for element in liczby
]
element**2 - piszemy co ma zostać zrobione z każdym elementem
for element in liczby - piszemy czym są elementy i skąd je pobrać
Aby wybrać liczby parzyste
liczby = [ 1 , 2 , 3 , 4 , 5 , 6 ]
liczbyParzyste2 = [ element
for element in liczby
if (element % 2 == 0)
]
element - co robimy
for element in liczby - skąd wybieramy wartości
if (element % 2 == 0) - warunek, jakie dokładnie wybieramy wartości'''

#pierwsza_metoda
liczby = [1, 2, 3, 4, 5]
liczby.append(6)
potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

print(potegiDwojki)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

print(liczbyParzyste)

#inna_metoda_WYRAZENIE_LISTOWNE
#[co_zrobic_na_elemencie | for element in stara_lista | warunek_oaprty_na_elemencie]
potegiDwojki2 = [element**2 
                for element in liczby
                ]

print(potegiDwojki2)

liczbyParzyste2 = [element 
                  for element in liczby 
                  if element % 2 == 0
                  ]

print(liczbyParzyste2)

potegiDwojki3 = [element**2 
                for element in range(300, 400)
                ]

print(potegiDwojki3)

liczbyParzyste3 = [element 
                  for element in range(300, 400) 
                  if element%2 ==0]

print(liczbyParzyste3)

liczbyParzyste4 = [element 
                  for element in potegiDwojki3 
                  if element%2 == 0]

#second_example_WYRAZENIA_GENERUJACE
'''Generator - pozwala na generowanie, tworzenie, wyciąganie poszczególnych elementów na
bieżąco.
evenNumbersGenerator = (element
for element in range( 400 )
if (element % 2 == 0 )
● Aby dostać się do wygenerowanych elementów stosujemy:
for item in evenNumbersGenerator:
print( item )
W ten sposób wypisujemy elementy ale po zakończeniu, czyli otrzymaniu przez
generator elementu nie jest on zapisywany w pamięci.
● Przy pomocy import sys możemy sprawdzić jakiej wielkości jest nasz generator
print(sys.getsizeof(evenNumbersGenerator))
Wyrażenie generujące tworzymy za pomocą nawiasów okrągłych ( ) używamy go kiedy
dane z których pobieramy wartości są ogromne. Jest ich bardzo dużo i nie potrzebujemy
przechowywać danych w pamięci komputera, a także gdy potrzebujemy skorzystać z funkcji
list czyli np. dodawanie (sum), sortowanie.
evenNumbersGenerator = (element
for element in range( 4400 )
if (element % 2 == 0 )
)'''

#fourth_example_WYRAZENIA_SLOWNIKOWE
'''Wyrażenie słownikowe czyli formuły, wyrażenia które pozwalają przemienić np. zbiory,
słowniki czy też listy - w słownik.
Wyrażenie słownikowe jest czytelne i szybkie, tworzymy je za pomocą { }
Wykorzystamy je m.in.:
● gdy chcemy sprawdzić długość każdego imienia i wypisać wszystkie imiona
rozpoczynające się na literę A:
names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}
namesLength = {
name : len(name)
for name in names
if name.startswith("A")
}
{ } wyrażenie słownikowe
namesLength - wynik wyrażenia
name : len (name) - przesyłamy do słownika funkcje len, aby sprawdzić długość każdego
elementu
for name in names - dla każdego imienia w names
if name.startswith("A") - warunek, jeśli imie zaczyna się od litery A
startswith - funkcja, tłumaczenie z ang. “zaczyna się od… “ dzięki niej możemy w sposób
szybki przefiltrować kod, aby wybrać elementy które są nam potrzebne
len - funkcja, która liczy długość elementu
● gdy chcesz zmienić skale temperatur ze stopni Celcjusza do Fahrenheita zostawiając
klucze, a zmieniając wartości
fahrenheit = {
key: celcius * 1.8 + 32
for key, celcius in celcius. items()
if celcius > -5
if celcius < 20
}
fahrenheit - nasz pojemnik, wynik wyrażenia
key: celcius * 1.8 + 32 - klucz : Celsjusz * jednostka przeliczenia st. celsjusza na
fahrenheita
for key, celcius in celcius.items() - dla klucza
items() - funkcja, która zmieni nam każdy klucz i wartość w krotke.
if celcius > -5 - warunek jeżeli celsjusz jest powyżej -5
if celcius < 20 - warunek jeżeli celsjusz ponizej 20'''

#fourth_example_WYRAZENIA_ZBIORU
'''Wyrażenia zbioru - tworzymy za pomocą zakręconych klamer { } , w wyrażeniu zbioru
występują tylko wartości.
Przykład
Podnieśmy pierwsze litery imion w wyrażeniach zbioru :
names = {"arkadiusz", "Wioletta", "karol", "bartłomiej", "Jakub", "Ania"}
names = {
name.capitalize()
for name in names
}
names - nazwa zbioru
{ } - wyrażenie zbioru
podajemy co zrobić z danymi capitalize() - funkcja, która podnosi
pierwszą literę do góry
for name in names - piszemy skąd wziąć wartość'''

