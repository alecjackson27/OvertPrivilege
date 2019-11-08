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
    list = []
    for i in range(9):
        temp = word[0] + str(i)
        list.append([temp, word[1] + 1])
    return list

def add_digit_at_penultimate(word):
    list = []
    for i in range(9):
        temp = word[0][:len(word[0])-1] + str(i) + word[0][len(word[0])-1]
        list.append([temp, word[1] + 1])
    return list

def add_special_char_at_end(word):
    special_chars = ['!', '@', '#', '$', '%', '*', '&']
    list = []
    for i in special_chars:
        temp = word[0] + i
        list.append([temp, word[1] + 1])
    return list

def repeat_word(word):
    return word * 2

def repeat_word_thrice(word):
    return word * 3

dispatcher = {
    1: mirror,
    2: capitalize,
    3: replace_e_3,
    4: replace_i_exclamation,
    5: replace_s_5,
    6: replace_s_dollarSign,
    7: add_digit_at_end,
    8: add_special_char_at_end,
    9: replace_a_atSymbol,
    10: repeat_word,
    11: repeat_word_thrice
}

def create_list_of_passwords(words, edit_distance=2):
    list = []
    queue = []
    queue.append([words, 0])
    while len(queue) > 0:
        word = queue.pop(0)
        list.append(word)
        if word[1] > edit_distance:
            break
        for i in range(1, 12):
            queue_flag = True
            list_flag = True
            if i in {7, 8}:
                edit = dispatcher[i](word)
                for x in queue:
                    if x[0] == edit[len(edit) - 1]:
                        queue_flag = False
                        break
                for x in list:
                    if x[0] == edit[len(edit) - 1]:
                        list_flag = False
                        break
                if queue_flag and list_flag:
                    queue += edit
            else:
                edit = dispatcher[i](word[0])
                for x in queue:
                    if x[0] == edit:
                        queue_flag = False
                        break
                for x in list:
                    if x[0] == edit:
                        list_flag = False
                        break
                if queue_flag and list_flag:
                    queue.append([edit, word[1] + 1])
    return list
