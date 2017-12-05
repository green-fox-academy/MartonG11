
# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

copy_from = open("copy_from.txt", "w")
copy_from.write("pig\n bacon, sausage\n candies\n lollypop, choco")
copy_from.close()
copy_to = open("copy_to.txt", "w")

def copy(copy_wherefrom, copy_whereto):
    copy_wherefrom = open(copy_wherefrom , "r")
    copy_whereto = open(copy_whereto , "w")
    copy_whereto.write(copy_wherefrom.read())

copy("copy_from.txt" , "copy_to.txt")