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
"""
def create_list_of_passwords(words,numbers):
    random.seed(a=None,version=2)
    list = []

    for i in range(30):
        num = numbers[random.randint(0,(len(numbers)-1))]
        wor = words[random.randint(0,(len(words)-1))]
        order = random.randint(0,5)
        extra = random.randint(0,10)

        if extra in {1,2,3}:
            wor = wor.capitalize()
        if extra == 5:
            wor = wor.capitalize()
            wor = wor.swapcase()
        if extra == 6:
            wor = wor.upper()

        word = ''
        if order != 0:
            word = wor+num
        else:
            word = num+wor

        list.append(word)

        replacement = word
        for i in range(4):
            replacement = dispatcher[i](replacement)

        if word != replacement:
            list.append(replacement)

    random.shuffle(list)
    return list
"""
def create_list_of_passwords(input, num_passwords):
    list = []
    queue = []
    print(input)
    for i in input:
        queue.append([i, 0])
    while len(queue) > 0:
        word = queue.pop(0)
        list.append(word)
        if word[1] > 3:
            break
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
                queue.append([edit, word[1] + 1])
    return list