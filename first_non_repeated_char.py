def findFirstNonRepeatedChar(word):
    word = word.lower()
    for i in word:
        if (word.count(i) == 1):
            return i
    else:
        return None

def findKthNonRepeatedChar(word, k):
    word = word.lower()
    counter = 0
    for i in word:
        if (word.count(i) == 1):
            counter += 1
            if (counter == k):
                return i
    else:
        return None

if __name__ == "__main__":
    word_list = ["scope",
                 "stellar",
                 "amazing",
                 "ganglia",
                 "eye",
                 "Momoa",
                 "Anna",
                 "a",
                 "non",
                 "noon",
             ]

    for word in word_list:
        unique_char = findFirstNonRepeatedChar(word)
        if unique_char:
            print("Word '%s's first non-repeating character is '%s'." %
                  (word, unique_char))
        else:
            print("Word '%s' only contains repeating characters." % (word, ))

    k_for_problem = 2
    for word in word_list:
        unique_char = findKthNonRepeatedChar(word, k_for_problem)
        if unique_char:
            print("Word '%s's %d non-repeating character is '%s'." %
                  (word, k_for_problem, unique_char))
        else:
            print("Word '%s' does not have %d non-repeating characters." %
                  (word, k_for_problem))
