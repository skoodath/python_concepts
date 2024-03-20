myList = [2, 3, 4, 5, 6, 7, 8]


def list_map(list_input, callback):
    result = []
    for i in range(len(list_input)):
        callback_result = callback(list_input[i], i, list_input)
        if callback_result:
            result.append(list_input[i])
    return result


def is_even(val, index, list_input):
    return val % 2 == 0


print(list_map(myList, is_even))