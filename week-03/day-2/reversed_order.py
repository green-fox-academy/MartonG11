# Create a method that decrypts reversed-order.txt


def decrypt(file_name):
    reversed_order = open(file_name, "r")
    to_list = [reversed_order.read()]
    to_list.reverse()
    for i in to_list:
        print(i[::-1])

decrypt("reversed-order.txt")