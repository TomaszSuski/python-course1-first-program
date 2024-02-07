# string w python jest tablicą znaków, wszystkie tablice są indeksowane od 0, więc stringi też
# można też używać indeksów ujemnych, wtedy liczymy od końca
#   p  y  t  h  o  n  g  e  e  k
#   0  1  2  3  4  5  6  7  8  9 - od lewej
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 - od prawej (od końca)

s = 'pythongeek'
print(s[0]) # p
print(s[-1]) # k
print(s[0:5]) # python
print(s[:5]) # python
print(s[6:]) # geek
print(s[-4:]) # geek
print(s[4:14]) # ongeek - nie ma błędu, jeśli indeks jest poza zakresem, to zwróci tyle znaków ile może
print(s[0:5:2]) # pto - co drugi znak
print(s[::2]) # ptoge - co drugi znak
print(s[4:-2]) # onge - od 4 do końca, bez dwóch ostatnich
print(s[::-1]) # keegnohtyp - od końca do początku, co jeden znak

# stringi w python nie są mutowalne, nie można zmieniać ich zawartości
# np. próba zmiany s[0] = "P" zwróci błąd
# można je za to zmieniać za pomocą operatorów
# np. s = "string"
# s = s + "s" - dodaje s na końcu
# s += "s" - dodaje s na końcu
# s = "s" + s - dodaje s na początku
# s = s * 3 - powiela s trzy razy
# s *= 3 - powiela s trzy razy
# s = s[:4] - skraca s do 4 znaków
# s = s[4:] - skraca s do 4 znaków
# s = s[:4] + s[5:] - usuwa 5 znak
# s = s.replace("i", "y") - zamienia i na y

# w konsoli można utworzyć stan z istniejącej zmiennej
# s[:6]
# i użyć go za pomocą podkreślnika
# print(_ + " rocks!") # python rocks!
# w uruchamianym pliku to nie działa

# del s - usuwa zmienną