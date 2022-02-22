def findFirstNonRepeatedChar(word):
    word = word.lower()
    for i in word:
        if (word.count(i) == 1):
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
                                                                     
