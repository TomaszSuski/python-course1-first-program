# esape character dla stringów to \
# np. "To jest \"string\""
# nowa linia w stringu to \n
# np. "To jest\nstring" = "To jest
# string"
# tabulator w stringu to \t
# np. "To jest\tstring" = "To jest    string"

# raw string to string, w którym znaki specjalne nie są interpretowane
# np. r"To jest\nstring" = "To jest\nstring"
# można też użyć raw stringów do tworzenia ścieżek
# np. r"C:\Users\user\Documents\file.txt"
# można też użyć raw stringów do tworzenia regexów
# np. r"^\d{3}-\d{3}-\d{4}$"
# można też użyć raw stringów do tworzenia stringów z dużą ilością znaków specjalnych
# np. r"\"\\\"\'\n\t"

# umieszczanie zmiennych w stringach
# a = 'gravity'
# b = '1966'
# print(f'The movie {a} was released in {b}')
# f-stringi są najnowszym sposobem formatowania stringów  

# konkatenacja stringów za pomocą +
# np. "To jest " + "string" = "To jest string"
# można też konkatenować stringi z innymi typami danych, ale trzeba je najpierw zamienić na stringi
# np. "To jest " + str(5) = "To jest 5"
# można też konkatenować stringi za pomocą przecinka
# np. print("To jest", "string") = "To jest string"
# przecinek dodaje spacje między stringami
# można też konkatenować stringi za pomocą formatowania
# np. "To jest {}".format("string") = "To jest string"
# można też konkatenować stringi za pomocą f-stringów
# np. f"To jest {'string'}" = "To jest string"
# f-stringi są najnowszym sposobem formatowania stringów
# można też konkatenować stringi za pomocą mnożenia
# np. "To jest " * 3 = "To jest To jest To jest "
# można też konkatenować stringi za pomocą join
# np. " ".join(["To", "jest", "string"]) = "To jest string"
# join działa na listach, a nie na stringach
# można też konkatenować stringi za pomocą operatora +=
# np. a = "To jest "; a += "string" = "To jest string"
# można też konkatenować stringi za pomocą operatora %
# np. "To jest %s" % "string" = "To jest string"
# %s oznacza, że w to miejsce wstawi się string
# %d oznacza, że w to miejsce wstawi się liczba
# %f oznacza, że w to miejsce wstawi się float
# można też konkatenować stringi za pomocą operatora .format
# np. "To jest {}".format("string") = "To jest string"
# można też konkatenować stringi za pomocą operatora .format z indeksami
# np. "To jest {0} {1}".format("string", "string") = "To jest string string"
# można też konkatenować stringi za pomocą operatora .format z nazwami
# np. "To jest {a} {b}".format(a="string", b="string") = "To jest string string"
# można też konkatenować stringi za pomocą operatora .format z indeksami i nazwami
# np. "To jest {0} {b}".format("string", b="string") = "To jest string string"
# można też konkatenować stringi za pomocą operatora .format z indeksami i nazwami w f-stringach
# np. f"To jest {0} {b}" = "To jest string string"
