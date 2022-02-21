import unittest
import anagram

class TestCleanWords(unittest.TestCase):

    # Following tests check string cleaning
    def test_whitespace(self):
        self.assertEqual(anagram.cleanWords("   all whitespace\r\nclea red\t"),
                         "allwhitespacecleared")
        self.assertNotEqual(anagram.cleanWords(" allwhite\r\nspa\tce   "),
                            "   allwhite\r\nspa\tce   ")

    def test_numeric_chars(self):
        self.assertEqual(anagram.cleanWords("1234all567numbers98018.59cleared"),
                         "allnumberscleared")
        self.assertNotEqual(anagram.cleanWords("124all567.289numbers"),
                            "124all567.289numbers")

    def test_capitals(self):
        self.assertEqual(anagram.cleanWords("HasManyCapitalLETTERS"),
                         "hasmanycapitalletters")
        self.assertNotEqual(anagram.cleanWords("SuPerCapItalIzed"),
                            "SuPerCapItalIzed")

    # Following tests check cleaning of array of strings
    def test_whitespace_list(self):
        self.assertEqual(anagram.cleanWords([" all whitespace\r\ncleared\t   ",
                                             "item\t\t\n   2"]),
                         ["allwhitespacecleared", "item"])
        self.assertNotEqual(anagram.cleanWords([" all space\r\ncleared\t   "]),
                            [" all space\r\ncleared\t   "])

    def test_numeric_chars_list(self):
        self.assertEqual(anagram.cleanWords(["1.234numbers87cleare89d09","1ab"]),
                         ["numberscleared","ab"])
        self.assertNotEqual(anagram.cleanWords(["1.234number889s09","1ab4"]),
                         ["1.234numbers889s09","1ab4"])

    # Following tests check anagrams
    def test_anagrams(self):
        self.assertTrue(anagram.checkAnagram(["melon", "lemon"]))
        self.assertTrue(anagram.checkAnagram(["abcdef", "CBDAEF", "FEdcBA",
                                              "CABDEF", "cadbef"]))
        self.assertTrue(anagram.checkAnagram(["Tom Marvolo Riddle",
                                              "I am Lord Voldemort"]))
        self.assertTrue(anagram.checkAnagram(["Mike likes I", "I like Mikes"]))

        # Now to check ones that are not valid anagrams
        print("Testing Failure Cases.")
        self.assertFalse(anagram.checkAnagram(["only one entry"]))
        self.assertFalse(anagram.checkAnagram(["melon", "lemonn"]))
        self.assertFalse(anagram.checkAnagram(["says", "asyy"]))
        self.assertFalse(anagram.checkAnagram(["says", "syaa"]))
        self.assertFalse(anagram.checkAnagram(["I like Mike", "Mike likes"]))
        # Be sure to test that same word does not get counted as an anagram!
        self.assertFalse(anagram.checkAnagram(["Anna", "anna"]))

if __name__ == '__main__':
    unittest.main()
