# python nie ma stałych!
# dla odróżnienia "stałych" od zmiennych używa się zmiennych z dużych liter

# python nie ma variables jako takich, są to obiekty, które są przypisane do zmiennych
# zmienna to tylko referencja do obiektu (object reference)
# zmienna nie ma typu, ma go obiekt
# zmienna nie ma wartości, ma ją obiekt
# zmienna nie jest deklarowana, jest przypisywana
# zmienna nie jest typowana, jest dynamicznie typowana
# zmienna nie jest mutowalna, jest niemutowalna
# zmienna nie jest usuwana, jest zwalniana
# zmienna nie jest kopiowana, jest referencjonowana
# zmienna nie jest zasięgowa, jest zasięgowa
# zmienna nie jest globalna, jest globalna

# typy zmiennych (danych) w pythonie:
# int - liczba całkowita, np.:
    # a = 5, lub a = int(5)
# float - liczba zmiennoprzecinkowa
    # b = 5.0, lub b = float(5)
# complex - liczba zespolona
    # c = 5 + 3j, lub c = complex(5, 3)
# str - string
    # d = "string", lub d = str("string")
# bool - boolean
    # e = True, lub e = bool(True)
    # mozna pobrać wartość liczbową za pomocą int(), np. int(True) = 1 lub int(False) = 0
# list - lista
    # f = [1, 2, 3], lub f = list((1, 2, 3))
    # może być różnych typów danych w jednej liście
    # np. g = [1, "string", 3.0]
    # dostęp do elementów listy odbywa się za pomocą indeksów, np. g[0] = 1
# tuple - tupla
    # h = (1, 2, 3), lub h = tuple([1, 2, 3])
    # może być różnych typów danych w jednej tupli
    # np. i = (1, "string", 3.0)
    # dostęp do elementów tupli odbywa się za pomocą indeksów, np. i[0] = 1
# set - zbiór
    # j = {1, 2, 3}, lub j = set([1, 2, 3])
    # nie ma indeksów, nie ma powtórzeń, nie ma kolejności
    # można dodać element za pomocą add(), np. j.add(4)
    # można usunąć element za pomocą remove(), np. j.remove(4)
    # można usunąć element za pomocą discard(), np. j.discard(4)
    # można usunąć ostatni element za pomocą pop(), np. j.pop()
    # można usunąć wszystkie elementy za pomocą clear(), np. j.clear()
    # można usunąć zbiór za pomocą del, np. del j
# frozenset - zbiór niemutowalny
    # k = frozenset([1, 2, 3])
    # nie ma indeksów, nie ma powtórzeń, nie ma kolejności
    # nie można np. dodać elementu za pomocą add(), np. k.add(4) - zwróci błąd
    # ani wykonać żadnej innej operacji, która zmienia zbiór
# dict - słownik (mapa - mapping type, zbiór par klucz-wartość)
    # myDict = {'name': 'John', 'age': 25}, lub myDict = dict(name='John', age=25)
    # dostęp do elementów słownika odbywa się za pomocą kluczy, np. myDict['name'] = 'John'
    # lub za pomocą get(), np. myDict.get('name') = 'John'
    # można dodać element za pomocą klucza, np. myDict['surname'] = 'Doe'
    # można usunąć element za pomocą klucza, np. del myDict['surname']
    # można usunąć wszystkie elementy za pomocą clear(), np. myDict.clear()
    # można usunąć słownik za pomocą del, np. del myDict
    # można skopiować słownik za pomocą copy(), np. myDict2 = myDict.copy()
    # można skopiować słownik za pomocą dict(), np. myDict2 = dict(myDict)
    # można skopiować słownik za pomocą słownika, np. myDict2 = {**myDict}
    # można skopiować słownik za pomocą update(), np. myDict2.update(myDict)
    # można pobrać klucze za pomocą keys(), np. myDict.keys()
    # można pobrać wartości za pomocą values(), np. myDict.values()
# range - zakres
    # rng = range(5, 10),
    # lub rng = range(5, 10, 2) - od 5 do 10 co 2, czyli 5, 7, 9
        # UWAGA! zakres od-do nie wlicza do, zakres od-do-co wlicza do
    # wywołać zakres można za pomocą list(), np. list(rng)
    # dostęp do elementów zakresu odbywa się za pomocą indeksów, np. rng[0] = 5

# funkcje zwracające typ zmiennych:
# type() - zwraca typ zmiennej
# isinstance() - zwraca True jeśli zmienna jest danego typu, False jeśli nie
# np. isinstance(5, int) - True
# isinstance(5, float) - False
# isinstance(5, (int, float)) - True
# isinstance(5, (float, str)) - False

# funkcja id() zwraca identyfikator obiektu
# identyfikator obiektu to adres w pamięci, w którym jest przechowywany obiekt
# identyfikator obiektu jest zwracany w postaci liczby w systemie dziesiętnym
# identyfikator obiektu jest unikalny dla każdego obiektu, a nie zmiennej!, np.:
# a = 5
# b = a
# id(a) == id(b) - True
# id samego obiektu przypisanego do zmiennej będzie takie samo jak id sprawdzane wg. zmiennej
# id(5) == id(a) - True
# przypisanie tego samego obiektu do nowej zmiennej nadal odwołuje się do tego samego id
# c = 5
# id(a) == id(c) - True