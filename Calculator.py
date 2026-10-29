# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Variables

# Schritt 1: Formel als Text einlesen (z. B. "2 * 3 * 4")
equation = (input("Enter your equation with spaces (e.g. 2 * 3 * 4):"))

# Schritt 2: Den Eingabe-String in eine Liste namens "numbers" aus Zahlen und Operatoren aufteilen
# Beispiel: "2 * 3 * 4" wird zu [´2´, ´*´,´3´,´*´, ´4´]
numbers = equation.split()

# Schritt 3: Das Startergebnis auf die erste Zahl der Liste setzen
result = float(numbers[0])

# Schritt 4: Gehe in 2er-Schritten durch die restlichen Elemente
# Index 'i' greift auf die Operatoren (*, /, +, -) zu
# Index 'i + 1' greift auf die nächste Zahl nach dem Operator zu
for i in range(1,len(numbers),2):
    operator = numbers[i]
    next_num = float(numbers[i+1])

# Schritt 5: Führe die Berechnung basierend auf dem aktuellen Operator durch
    if operator == "*":
        result = result * next_num
    elif operator == "/":
        result = result / next_num
    elif operator == "+":
        result = result + next_num
    elif operator == "-":
        result = result- next_num

# 
print("Answer:", result)







