# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

num = float(input("Put your number here: "))

if(num % 2 == 0):
    print("even")
else: 
    print("odd")