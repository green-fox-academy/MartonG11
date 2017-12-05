# Create a method that decrypts the duplicated-chars.txt



def decrypt(file2):
    duplicated = open(file2, "r")
    print(duplicated.read()[ : :2])

decrypt("duplicated-chars.txt")

