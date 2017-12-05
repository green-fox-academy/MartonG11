# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

new_file = "file1234.txt"


def print_lines(new_file):
    try:
        myfile = open(new_file , "r")
        print(myfile.read())
    except IOError:
        print("Unable to read the file.")

print_lines(new_file)