import unittest
from marton_gabor_work import Tests


class Test_All(unittest.TestCase):
    
    def test_apples(self):
        apple = Tests()
        self.assertEqual(apple.get_apple(), "apple")

    def test_summa(self):
        list_of_numbers = Tests()
        self.assertEqual(list_of_numbers.sum_elements([]), 0)
        self.assertEqual(list_of_numbers.sum_elements([8]), 8)
        self.assertEqual(list_of_numbers.sum_elements([11, 13, 16]), 40)
        self.assertEqual(list_of_numbers.sum_elements([0]), 0)

    def test_anagram(self):
        anagram = Tests()
        self.assertEqual(anagram.anagram_checker("szabad lexikon", "szexi lakodban"), True or False)

if __name__ == '__main__':
    unittest.main()

