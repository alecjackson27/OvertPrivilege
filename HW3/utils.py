# can put any functions you feel the others may want to use here

# takes an array of string digits and returns an integer value
def sum_list(array):
    sum = 0
    for item in array:
        sum += int(item)
    return sum
