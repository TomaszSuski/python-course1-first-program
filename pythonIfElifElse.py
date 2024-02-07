# struktury kontrolne if-else w pythonie
# jak wszystkie struktury w pythonie, if-else nie ma nawiasów, a bloki kodu są definiowane przez wcięcia

# if
# if warunek:
#     kod
# elif
# elif warunek:
#     kod
# else
# else:
#     kod


# print("This program will compare two numbers. Provide two integers.")
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
# except:
#     print("Invalid input, please enter a integer")
# else:
#     if num1 > num2:
#         print(f"First number ({num1}) is greater than second number ({num2})")
#     elif num1 < num2:
#         print(f"First number ({num1}) is less than second number ({num2})")
#     else:
#         print(f"First number ({num1}) is equal to second number ({num2})")
# finally:
#     print("The program has ended")

# zadanie
# Problem Statement for Python IF-ELIF-ELSE
# ================================================================================
# Take four numbers as input from user - 1, 2, 3, 4
# If user inputs them correctly then print them in words like-
# One for 1, Two for 2, Three for 3 and 4 for Four
# But if input is none of them say - "number is out of scope"

print("This program will convert numbers to words. Provide four integers form range 1 to 4.")
try:
    num1 = int(input("Enter first number: ") or 0) # or 0 to avoid ValueError if input is empty
    num2 = int(input("Enter second number: ") or 0)
    num3 = int(input("Enter third number: ") or 0)
    num4 = int(input("Enter fourth number: ") or 0)
except:
    print("Invalid input, please enter a integer")
else:
    rng = range(1, 5)
    if num1 not in rng:
        print("First number is out of scope")
    else:
        if num1 == 1:
            print("One")
        elif num1 == 2:
            print("Two")
        elif num1 == 3:
            print("Three")
        else:
            print("Four")
    if num2 not in rng:
        print("Second number is out of scope")
    else:
        if num2 == 1:
            print("One")
        elif num2 == 2:
            print("Two")
        elif num2 == 3:
            print("Three")
        else:
            print("Four")
    if num3 not in rng:
        print("Third number is out of scope")
    else:
        if num3 == 1:
            print("One")
        elif num3 == 2:
            print("Two")
        elif num3 == 3:
            print("Three")
        else:
            print("Four")
    if num4 not in rng:
        print("Fourth number is out of scope")
    else:
        if num4 == 1:
            print("One")
        elif num4 == 2:
            print("Two")
        elif num4 == 3:
            print("Three")
        else:
            print("Four")
finally:
    print("The program has ended")