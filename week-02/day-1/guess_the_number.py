num1 = 11
num2 = 0



while (num1-num2) != 0:
    
    num2 = int(input("Guess the number: "))
    
    if num1 > num2:
        print("The stored number is higher.")
    elif num1 < num2:
        print("The stored number is lower.")
    else:
        print("You found the number: 11")
        break
