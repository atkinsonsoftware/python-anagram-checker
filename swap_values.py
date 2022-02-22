import argparse

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
