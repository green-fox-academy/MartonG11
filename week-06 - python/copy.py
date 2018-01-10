import sys


def copyfile():
    if len(sys.argv) == 1:
        print("copy [source] [destination]")
    elif len(sys.argv) == 2:
        print("No destination provided")
    elif len(sys.argv) == 3:
        try:
            with open(sys.argv[1], 'r') as copy_from, open(sys.argv[2], 'w') as copy_to:
                content =  copy_from.read()
                copy_to.write(content)
        except FileNotFoundError:
            print("No such file")
    else: 
        print("RTFM")

        
        
copyfile()