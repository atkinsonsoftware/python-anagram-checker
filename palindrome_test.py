import unittest
import palindrome

class TestPalindromes(unittest.TestCase):

    def test_palindromes(self):
        self.assertTrue(palindrome.checkPalindrome("Anna"))
        self.assertTrue(palindrome.checkPalindrome(
            "Go hang a salami, I'm a lasagna hog"))
        self.assertTrue(palindrome.checkPalindrome("reviver"))
        self.assertTrue(palindrome.checkPalindrome("aabbaa"))
        self.assertTrue(palindrome.checkPalindrome("abcba"))
        self.assertTrue(palindrome.checkPalindrome("madam"))
        self.assertTrue(palindrome.checkPalindrome(
            "A nut for a jar of tuna."))
        self.assertTrue(palindrome.checkPalindrome(
            "Stressed desserts"))

        # Begin false test cases
        self.assertFalse(palindrome.checkPalindrome("Mike"))
        self.assertFalse(palindrome.checkPalindrome("aabbcc"))
        self.assertFalse(palindrome.checkPalindrome("aabbcbaa"))
        self.assertFalse(palindrome.checkPalindrome("Kalimazoo"))
        self.assertFalse(palindrome.checkPalindrome("Stupendous"))


if __name__ == "__main__":
    unittest.main()
