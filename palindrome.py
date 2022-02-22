import argparse
from anagram import cleanWords

def checkPalindrome(word):
    # Each word must be at least 3 characters in length
    if len(word) < 2:
        print("'%s' is not a palindrome. At least 2 letters are required." %
              (word, ))
        return False

    # Whitespace, special characters should be ignored
    # Lowercase vs Uppercase does not revoke a palindrome's status
    clean_word = cleanWords(word)

    # First half (+) of word must equal reverse of last half (+) of word
    word_length = len(clean_word)
    middle_index = int(word_length/2)
    first_half = list(clean_word[0:middle_index])
    second_half = list(clean_word[middle_index:])
    if (word_length %2 != 0):
        # Remove one from the second split
        second_half = second_half[1:]

    second_half.reverse()
    if (first_half == second_half):
        print("'%s' is a palindrome!" % (word,))
        return True
    else:
        print("'%s' is NOT a palindrome." % (word,))
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # At least one word must be entered
    parser.add_argument("words", nargs="+", type=str)

    args = parser.parse_args()
    words = args.words

    for word in words:
        checkPalindrome(word)
