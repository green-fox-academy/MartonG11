# Create a method that decrypts reversed-lines.txt


def decrypt(file_name):
    reversed = open(file_name, "r")
    print(reversed.read()[ : :-1])

decrypt("reversed-lines.txt")