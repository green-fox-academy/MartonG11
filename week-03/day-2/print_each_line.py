# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"


my_file = open("myfile.txt" , "r")

def print_lines(file):
    try:
        print(file.read())
    except FileNotFoundError:
        print("Unable to read the file.")

print_lines(my_file)
