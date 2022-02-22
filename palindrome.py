import argparse
from anagram import cleanWords

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # At least one word must be entered
    parser.add_argument("words", nargs="+", type=str)

    args = parser.parse_args()
    words = args.words

    # Each word must be at least 3 characters in length
    for word in words:
        if len(word) < 2:
            print("'%s' is not a palindrome. At least 2 letters are required." %
                  (word, ))

    # Whitespace, special characters should be ignored
    # Lowercase vs Uppercase does not revoke a palindrome's status
    clean_words = cleanWords(words)

    # First half (+) of word must equal reverse of last half (+) of word
    for word in clean_words:
        word_length = len(word)
        middle_index = int(word_length/2)
        first_half = list(word[0:middle_index])
        second_half = list(word[middle_index:])
        if (word_length %2 != 0):
            # Remove one from the second split
            print("Word has odd length; don't compare middle char")
            second_half = second_half[1:]

        second_half.reverse()
        if (first_half == second_half):
            print("'%s' is a palindrome!" % (word,))
        else:
            print("'%s' is NOT a palindrome." % (word,))
