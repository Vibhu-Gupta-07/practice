from functools import reduce 
a = [12,3,4,6,7,9,999,25,59,16,4,552,52,5,56,4,86,85,55]


def greater(a,b):
    if (a>b):
        return a
    return b



print(reduce(greater,a))