def mid(incoming_string):
    '''Takes a string as a parameter. Returns middle letter. If none, ""'''
    len_str = len(incoming_string)
    if (len_str % 2) == 0:
        return ""
    else:
        return incoming_string[int(len_str / 2)]




def get_row_col(string):
    '''Incoming string formatted col letter A/B/C, row 1/2/3
    returns tuple corresponding with row and column indexes 0-2'''
    col_letter = string[0]
    row_number = int(string[1]) - 1
    if (col_letter == "A"):
        return (row_number, 0)
    elif (col_letter == "B"):
        return (row_number, 1)
    else:
        return (row_number, 2)
