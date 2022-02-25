def flatten(list_to_flatten):
    flat_list = []
    list_to_flatten_len = len(list_to_flatten)

    while(any(type(item) == list for item in list_to_flatten)):
        for item in list_to_flatten[:]:
            if type(item) == list:
                for subitem in item:
                    if type(subitem) == list:
                        list_to_flatten.append(subitem)
                    else:
                        flat_list.append(subitem)
                list_to_flatten.remove(item)
            else:
                flat_list.append(item)
                list_to_flatten.remove(item)

    print(flat_list)
    return flat_list

if __name__ == "__main__":
    bumpy_list = [1, 2, 3, ['a', 'b', ['ac'], 'c'], 4]
    print(bumpy_list)
    print(flatten(bumpy_list))
