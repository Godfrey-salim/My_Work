# A simple program to convert weight from pounds to kilograms and vice versa.
# user is prompted to enter their weight and the units they prefer, then the program will convert the weight to the desired units and print the result.
weight=int(input('what is your weight? '))
units = input('which units do you prefer ? (kg(k) or pounds(p)) ')
# 1 kilogram is equal to 0.45 pounds
# 1 pound is equal to 2.2 kilograms
if units.lower() == 'p':
    convert1 = (weight) / 0.45
    print(f'you are {convert1} pounds')
# the .lower() method is used to convert the input to lowercase, so that the program can accept both uppercase and lowercase letters for the units.
elif units.lower() == 'k':
    convert2 = (weight) * 2.2
    print(f'you are {convert2} kilograms')
else:
    print('invalid alphabetical letter used to represent your units')
    