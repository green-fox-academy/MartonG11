# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

my_file = open("my_file.txt", "w")
my_file.write("Apple\n Pear\n Grape\n Pineapple\n Beer")
my_file.close()

def contain_line(file):
    try:
        my_file = open("my_file.txt", "r")
        with open("my_file.txt") as counting:
            print(sum(1 for line in counting))
    except IOError:
        print(0)

contain_line(my_file)




        my_file = open(filename, 'r')
        with open(filename) as counting:
            return(sum(1 for letter in counting))