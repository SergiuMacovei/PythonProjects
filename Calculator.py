# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Variables

# Step 1: Ask the user for a space-separated mathematical equation
equation = (input("Enter your equation with spaces (e.g. 2 * 3 * 4):"))

# Step 2: Split the input string into a list "numbers" of individual numbers and operators
# Example: "2 * 3 * 4" becomes [´2´, ´*´,´3´,´*´, ´4´]
numbers = equation.split()

# Step 3: Initialize the running result with the first number in the list
result = float(numbers[0])

# Step 4: Travel through the remaining items in steps of 2
# Index 'i' targets operators (*, /, +, -)
# Index 'i + 1' targets the next number right after the operator
for i in range(1,len(numbers),2):
    operator = numbers[i]
    next_num = float(numbers[i+1])

# Step 5: Perform the calculation based on the current operator
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







