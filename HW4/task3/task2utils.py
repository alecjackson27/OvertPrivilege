import random

def capitalize(word):
    return word.title()

def replace_e_3(word):
    return word.replace('e', '3').replace('E', '3')

def replace_a_atSymbol(word):
    return word.replace('a', '@').replace('A','@')

def replace_i_exclamation(word):
    return word.replace('i', '!').replace('I', '!')

def replace_s_dollarSign(word):
    return word.replace('s', '$').replace('S', '$')

def replace_s_5(word):
    return word.replace('s', '5').replace('S', '5')

def replace_s(word):
    if 's' in word:
        rand = random.randint(0,1)
        if rand:
            return word.replace('s', '$').replace('S', '$')
        else:
            return word.replace('s', '5').replace('S', '5')
    else:
        return word

def cap(word):
    return word.capitalize()

def swap_case(word):
    word = word.capitalize()
    return word.swapcase()

def to_upper(word):
    return word.upper()


dispatcher = {
    0: replace_e_3,
    1: replace_i_exclamation,
    2: replace_a_atSymbol,
    3: replace_s,
    4: cap,
    5: swap_case,
    6: to_upper
}

def create_list_of_passwords(words):
    list = []
    queue = []
    for i in words:
        queue.append(i)
    while len(queue) > 0:
        word = queue.pop(0)
        #print(word)
        list.append(word)
        #if word[1] > 3:
        #    break
        for i in range(1, 7):
            queue_flag = True
            list_flag = True
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
                queue.append([edit, word[1]])
    return list