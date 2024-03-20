def get_factorial(input_num):
    if input_num <= 0:
        return 1
    else:
        return input_num * get_factorial(input_num - 1)


num_val = int(input("Type a number: "))

result = get_factorial(num_val)

print(result)
