# Program for adding two numbers

print("This program will add two numbers")
print("Enter two numbers")
# try/catch block   -   error handling
# w pythonie nie ma bloku try/catch, jest try/except
# składnia jest taka, że po try wpisujemy ":" a w następnej linii wcięcie
# wcięcia definiują blok kodu, nie nawiasy jakiegokołwiek rodzaju
try: 
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    # poniżej kod po kolei
    # x = int(x)
    # y = int(y)
    # z = x + y
    # print("The sum of the two numbers is: ", z)
    # ale można to zrobić w jednej linii
    print("The sum of the two numbers is: ", int(x) + int(y))
except:
    print("Invalid input, please enter a number")
    
# można też zrobić tak, żeby program nie kończył się po błędzie
# try:
#     x = input("Enter first number: ")
#     y = input("Enter second number: ")
#     print("The sum of the two numbers is: ", int(x) + int(y))
# except:
#     print("Invalid input, please enter a number")
# finally:
#     print("The program has ended")
# finally wykona się zawsze, niezależnie od tego czy był błąd czy nie
# można też zrobić tak, żeby finally wykonało się tylko jeśli nie było błędu
# try:
#     x = input("Enter first number: ")
#     y = input("Enter second number: ")
#     print("The sum of the two numbers is: ", int(x) + int(y))
# except:
#     print("Invalid input, please enter a number")
# else:
#     print("The program has ended")
# finally:
#     print("The program has ended")
# else wykona się tylko jeśli nie było błędu
# finally wykona się zawsze, niezależnie od tego czy był błąd czy nie

#mozna też wykorzystac blok try/except/else do sprawdzenia wartości przed wykonaniem kodu
# try:
#     x = input("Enter first number: ")
#     y = input("Enter second number: ")
#     x = int(x)
#     y = int(y)
# except:
#     print("Invalid input, please enter a number")
# else:
#     print("The sum of the two numbers is: ", x + y)
# finally:
#     print("The program has ended")