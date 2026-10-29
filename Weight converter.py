# is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
weight = input("Weight:")
type = input ("'(K)g or (L)bs:")

if type == "l":
   weight =  float (weight)* 2.20462
   print("Weight in pounds:" + str(weight))
elif type== "k":
    weight= float (weight)/2.20462
    print("Weight in kilograms:" + str(weight))


