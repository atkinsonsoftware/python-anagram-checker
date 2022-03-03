import re

def are_xs_equal_to_os(input_string):
    '''Returns True if # of X's equals # of O's; False otherwise'''
    # Null case; string is empty, so 0=0
    if (len(input_string) == 0):
        return True

    x_count = len(re.findall("[Xx]", input_string))
    o_count = len(re.findall("[Oo]", input_string))

    return x_count == o_count

if __name__ == "__main__":
    tests = [
        "2p138y47098ysdfhoivx;h98y0ioshfjuy", #2 o's, 1 x
        "", #0 o's, 0 x's
        "xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo", #equal
        "xox", #1 o, 2x's
        "oxo", #2 o's, 1x
        "supperisgoingtobelaterbecausei'mnotontheexpresstrain", #more o's
        "neveranyletter" #0 o's, 0x's
    ]
    for test in tests:
        print("String %s has an equal number of x's and o's? %s" %
              (test, are_xs_equal_to_os(test)))
