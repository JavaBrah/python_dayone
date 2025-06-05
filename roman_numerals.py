def to_roman(number: int):
    num_converted_to_roman = ""
    roman_dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    for key in roman_dict.keys():
        count = number // key
        number -= count * key
        num_converted_to_roman += roman_dict[key] * count
        
    return num_converted_to_roman

print(to_roman(1094))