from functools import reduce


def armstrong_func(number):
    split_number_list = [x for x in str(number)]
    exponent = len(split_number_list)
    armstrong_sum = sum([int(x) ** exponent for x in split_number_list])
    if number == armstrong_sum:
       return armstrong_sum

def check_armstrong_func(range_num):
    armstrong_list = [x for x in range(1, range_num) if armstrong_func(x)]
    return armstrong_list

def anagramI_func(word, another_word):
    word = sorted([x.lower() for x in word])
    another_word = sorted([x.lower() for x in another_word])
    if word == another_word:
        return True
    return False

def sum_pairs_func(num_list: list, target: int) -> list:
    sum_pairs_list = []
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                sum_pairs_list.append([num_list[i], num_list[j]])
    return sum_pairs_list

def credit_check(credit_card_number: str) -> bool:
    num_list = [int(x) for x in credit_card_number]
    adjusted_list = [digit if i % 2 == 1 else digit * 2 for i, digit in enumerate(num_list)]
    for i, n in enumerate(adjusted_list):
        if n >= 10:
            adjusted_list[i] = sum([int(x) for x in str(n)])
    if sum(adjusted_list) % 10 == 0:
        return "The number is valid!"
    return "The number is invalid!"

def char_count(string) -> list:
    char_dict = {}
    for c in string:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    char_count_list = sorted([[key, value] for key, value in char_dict.items()], key=lambda x : x[1], reverse=True)
    return char_count_list

def palindrome(string):
    if str(string).lower() == str(string).lower()[::-1]:
        return True
    return False

def calculate_mode(arf):
    dic = {}
    for x in arf:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    mode = max(dic.values())
    mode_list = [key for key in dic.keys() if dic[key] == mode]
    return mode_list
        
def pad_array(arr, length, pad=None):
    while len(arr) < length:
        arr.append(pad)
    return arr

def balanceParens(string):
    first_result = []
    final_result = []
    stack = 0
    for char in string:
        if char == '(':
            stack += 1
            first_result.append(char)
        elif char == ')':
            if stack > 0:
                stack -= 1
                first_result.append(char)
        else:
            first_result.append(char)
    stack = 0
    for char in reversed(first_result):
        if char == ')':
            stack += 1
            final_result.append(char)
        elif char == '(':
            if stack > 0:
                stack -= 1
                final_result.append(char)
        else:
            final_result.append(char)
    return ''.join(reversed(final_result))





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


