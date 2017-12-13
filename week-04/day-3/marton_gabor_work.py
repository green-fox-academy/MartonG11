

class Tests():

    def get_apple(self):
        return "apple"

    def sum_elements(self, numbers):
        summs = 0
        for i in numbers:
            summs += i
        return summs

    def anagram_checker(self, a, b):
        string1 = sorted(a)
        string2 = sorted(b)
        if string1 == string2:
            return True
        else:
            return False