import argparse

def swapValues(first, second):
    return(second, first)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("first", type=float)
    parser.add_argument("second", type=float)

    args = parser.parse_args()
    first = args.first
    print("First %d" % first)
    second = args.second
    print("Second %d" % second)
    second += first
    first = second - first
    second = second - first
    print("First %d" % first)
    print("Second %d" % second)

    if first == args.second and second == args.first:
        print("Successfully swapped numbers")

    # Use swapValues method now, instead
    first = args.first
    second = args.second
    print("About to use function. first: %d second %d" % (first, second))
    print("Now: first: %d second %d" % swapValues(first, second))

    # swap strings
    str1 = "first_string"
    str2 = "second_string"
    print(str1)
    print(str2)
    # Concatenate, place in second var
    str2 += str1
    # Update first string by grabbing chars up to first strings length
    str1 = str2[:(len(str1) + 1):]
    # Update second string by grabbing chars starting at first strings length
    str2 = str2[len(str1):]
    print(str1)
    print(str2)
