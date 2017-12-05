# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"


myfile1 = open("my-file1.txt", "w")
myfile1.write("Marton Gabor")
myfile1.close()

def write_file(file1):
    try:
        myfile1 = open("my-file1.txt", "r")   
        myfile1.write("Marton Gabor likes puppies")
        myfile1.close()
    except IOError:
        print("Unable to write file: my-file1.txt")

write_file(myfile1)