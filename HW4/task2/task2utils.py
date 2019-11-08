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




dispatcher = {
    0: replace_e_3,
    1: replace_i_exclamation,
    2: replace_a_atSymbol,
    3: replace_s
}

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
