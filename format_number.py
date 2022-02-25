import re

def format_number(positive_num):
    '''Takes in non-negative number and must return pretty-printed string'''
    num_as_string = "%s" % positive_num
    pretty_string = ""
    num_digits = len(num_as_string)

    # Mod by 1000 and append string formatting
    result = int(positive_num)
    while int(result)  > 0:
        result_mod_1k = result % 1000
        if (len("%s" % result_mod_1k) == 3):
            pretty_string = ",%d" % result_mod_1k + pretty_string
        elif (len("%s" % result_mod_1k) == 2):
            pretty_string = ",0%d" % result_mod_1k + pretty_string
        else:
            pretty_string = ",00%d" % result_mod_1k + pretty_string
        result = int(result/1000)

    # Front-leading commas and zeroes should be removed.
    pretty_string = re.sub("^[,0]*", "", pretty_string)

    # Once a decimal point is reached, append decimal and all following digits
    contains_decimal = num_as_string.find(".")
    if (contains_decimal != -1):
        pretty_string += num_as_string[contains_decimal:]

    return pretty_string

if __name__ == "__main__":
    print(format_number(1000))
    print(format_number(55))
    print(format_number(88249239))
    print(format_number(55.66))
    print(format_number(123098.2352513515))
