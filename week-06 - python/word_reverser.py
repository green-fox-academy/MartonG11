def reverse(text):
    reverseWord = " "
    make_list = text.split()
    for word in make_list:
        word = word[::-1]
        reverseWord = reverseWord + word + " "
    return reverseWord.strip()




print(reverse("lleW ,enod taht saw ton taht drah"))