#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    sum1 = 0
    for i in my_list:
        sum += i[1]
        mul = i[0] * i[1]
        sum1 += mul
    return sum1/sum
