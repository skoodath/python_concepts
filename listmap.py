myList = [2, 3, 4, 5, 6, 7, 8]


def list_map(list_input, callback):
    result = []
    for i in range(len(list_input)):
        result.append(callback(list_input[i], i, list_input))
    return result


def make_dictionary(val, index, list_input):
    my_dict = {index: val}
    return my_dict


print(list_map(myList, make_dictionary))
