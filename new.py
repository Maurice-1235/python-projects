def recursive_sum(curr, acc):
    if curr == 11:
        return acc
    else:
        return recursive_sum(curr + 1, acc + curr)


print(recursive_sum(1, 0))


def sumList_recursive(input_list):
    if input_list == []:
        return 0
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + sumList_recursive(smaller_list)


print(sumList_recursive([1, 2, 3, 4]))
