# Write a program that asks for an integer that is a distance in kilometers,
# then it converts that value to miles and prints it

km = float(input('Put a kilometer to convert to miles: '))
factor = 0.621371192
miles = km * factor
print("The distance in miles is: ", miles)