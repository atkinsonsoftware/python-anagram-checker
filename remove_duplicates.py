import argparse

def removeDuplicates(items):
    '''Removes duplicates by building up dictionary and returning keys'''
    new_items = {}
    # No need to check if item is already a key in new_items; assignment faster
    for item in items:
        new_items[item] = True
    return list(new_items.keys())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("value", nargs='+')

    args = parser.parse_args()
    value = args.value

    print("Original list: %s" % value)
    print("After duplicates are removed: %s" % removeDuplicates(value))
