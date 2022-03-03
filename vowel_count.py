import re

def count_vowels(word):
    '''Returns number of vowels in word'''
    try:
        results = re.findall("[aeiou]", word)
        return len(results)
    except:
        return 0

if __name__ == "__main__":
    for word in ["some", "a", "scriptaculous", "yellow", "pineapple", "octopus",
                 "how", "met", "aim", "lye", "mint", "beautiful-o", "k"]:
        print("Word %s contains: %d vowels" % (word, count_vowels(word)))
