my_list = [2,2,3,4,4,4,5,6,6,6,6,6,7,8]


def list_reduce(list_input, callback, initial_value):
    accumulator = initial_value
    for i in range(len(list_input)):
        if accumulator is None:
            accumulator = list_input[i]
        else:
            accumulator = callback(accumulator, list_input[i], i, list_input)

    return accumulator


def find_total(acc, curr, index, list_input):
    return acc + curr


print(list_reduce(my_list, find_total, 0))
