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


# def sum_pairs_func(num_list: list, target: int) -> list:
#     sum_pairs_list = []
#     for i in range(len(num_list)):
#         for j in range(i+1, len(num_list)):
#             if num_list[i] + num_list[j] == target:
#                 sum_pairs_list.append([num_list[i], num_list[j]])
#     return sum_pairs_list

# print(sum_pairs_func([1,2,3,4,5,1], 3))


# def credit_check(credit_card_number: str) -> bool:
#     num_list = [int(x) for x in credit_card_number]
#     adjusted_list = [digit if i % 2 == 1 else digit * 2 for i, digit in enumerate(num_list)]
#     for i, n in enumerate(adjusted_list):
#         if n >= 10:
#             adjusted_list[i] = sum([int(x) for x in str(n)])
#     if sum(adjusted_list) % 10 == 0:
#         return "The number is valid!"
#     return "The number is invalid!"

# print(credit_check(5541808923795240))

# def char_count(string) -> list:
#     char_dict = {}
#     for c in string:
#         if c not in char_dict:
#             char_dict[c] = 1
#         else:
#             char_dict[c] += 1
#     char_count_list = sorted([[key, value] for key, value in char_dict.items()], key=lambda x : x[1], reverse=True)
    
#     return char_count_list

# print(char_count("aabbbcdddd"))

# def palindrome(string):
#     if str(string).lower() == str(string).lower()[::-1]:
#         return True
#     return False

# print(palindrome('Noon'))







# /*What is the cipher
# a rot(1) b
# a rot(2) c
# a rot(3) d
 
# 'abc' <=1=> 'bcd' <=3=> 'efg' <=19=> 'xyz'
# */
 
# // Problem
# // Write a function that given a list of strings, returns groups of strings 
# that decode to the same message
# Example :
# bde <=1=> cef
# input: ['abc', 'bcd', 'bde', 'cef']
# output: [['abc', 'bcd'], ['bdf', 'ceg']]

import string

def find_the_cipher(strings: list) -> tuple:
    alphabet_dict = {v: i for i, v in enumerate(list(string.ascii_lowercase))}
    string_dict = {}
    for w in strings:
        string_dict[w] = []
        for c in w:
            string_dict[w].append(alphabet_dict[c])
    
    return string_dict   

print(find_the_cipher(['abc', 'bcd', 'bde', 'cef']))


