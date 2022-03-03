import argparse
import re

def cleanWords(word_list):
    # Cleans up words. Strips whitespace, sends everything to lowercase
    if (type(word_list) == str):
        new_word = word_list.lower()
        new_word = re.sub("[^a-z]", "", new_word)
        return new_word
    else:
        clean_words = []
        for word in word_list:
            new_word = word.lower()
            new_word = re.sub("[^a-z]", "", new_word)
            clean_words.append(new_word)
        return clean_words

def checkAnagram(word_list):
    # There must be at least 2 items to compare
    num_words = len(word_list)
    if (num_words < 2):
        print("Must have at least 2 entries to check if they are anagrams")
        print("Entries given: %s" % (word_list, ))
        return False

    # 1 Clean up the words so their alphabetical chars can be compared
    clean_words = cleanWords(word_list)

    # 2 Anagrams must be of same length
    first_word = clean_words[0]
    length = len(first_word)
    if any(len(word) != length for word in clean_words[1:]):
        print("Anagrams must be of the same length as one another.")
        return False

    # 3 Anagrams should not be identical words!
    set_words = set(clean_words)
    if (len(set_words) != num_words):
        print("Identical words detected!")
        return False

    # 4 Anagrams must distinctly use same letters
    # Sort lists of each word; compare lists!!
    first_word_sorted = list(first_word)
    first_word_sorted.sort()
    if (any(sorted(list(word)) != first_word_sorted for word in clean_words[1:])):
        print("Characters are repeated differently in the words.")
        return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("words", nargs='+', type=str)

    args = parser.parse_args()
    words = args.words

    # Check words to see if they are anagrams of one another
    anagrams = checkAnagram(words)
    if (anagrams):
        print("Given words are anagrams!")
    else:
        print("Given words are not anagrams.")
