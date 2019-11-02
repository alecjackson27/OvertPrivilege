import random

def mirror(word):
    return word[::-1]

def capitalize(word):
    return word.title()

def replace_e_3(word):
    return word.replace('e', '3').replace('E', '3')

def replace_a_atSymbol(word):
    return word.replace('a', '@')

def replace_i_exclamation(word):
    return word.replace('i', '!')

def replace_s_dollarSign(word):
    if 's' in word:
        return word.replace('s', '$').replace('S', '$')
    else:
        return word + 's'

def replace_s_5(word):
    if 's' in word:
        return word.replace('s', '5').replace('S', '5')
    else:
        return word + 'S'

def add_digit_at_end(word):
    digit = str(random.randint(1, 999))
    return word + digit

def add_special_char_at_end(word):
    special_chars = ['!', '@', '#', '$', '%', '*', '&']
    selected_char = special_chars[random.randint(0,6)]
    return word + selected_char

def repeat_word(word):
    ret = ''
    for i in range(random.randint(1,4)):
        ret += word
    return ret

dispatcher = {
    1: mirror,
    2: capitalize,
    3: replace_e_3,
    4: replace_i_exclamation,
    5: replace_s_5,
    6: replace_s_dollarSign,
    7: add_digit_at_end,
    8: add_special_char_at_end,
    9: repeat_word
}

def create_list_of_passwords(input, num_passwords):
    list = []
    for i in range(num_passwords):
        word = input
        options = [1,2,3,4,5,6,7,8,9]
        for j in range(3):
            random.shuffle(options)
            word = dispatcher[options[0]](word)
            del options[0]
        list.append(word)
    return list
