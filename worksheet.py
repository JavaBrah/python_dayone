# from functools import reduce


# def armstrong_func(number):
#     split_number_list = [x for x in str(number)]
#     exponent = len(split_number_list)
#     armstrong_sum = sum([int(x) ** exponent for x in split_number_list])
#     if number == armstrong_sum:
#        return armstrong_sum

# def check_armstrong_func(range_num):
#     armstrong_list = [x for x in range(1, range_num) if armstrong_func(x)]
#     return armstrong_list

# print(check_armstrong_func(999))




# def anagramI_func(word, another_word):
#     word = sorted([x.lower() for x in word])
#     another_word = sorted([x.lower() for x in another_word])

#     if word == another_word:

#         return True
#     return False

# print(anagramI_func("W2o3rd", '3dr2ow'))


def sum_pairs_func(num_list: list, target: int) -> list:
    sum_pairs_list = []
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                sum_pairs_list.append([num_list[i], num_list[j]])
    return sum_pairs_list

print(sum_pairs_func([1,2,3,4,5,1], 3))


