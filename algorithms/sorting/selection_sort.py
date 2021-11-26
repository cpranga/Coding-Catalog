from random import randint
from sys import argv

def selection_sort(vals_list):
    vals = list(vals_list)
    for front_index in range(0, len(vals) - 1):
        for back_index in range(front_index + 1, len(vals)):
            if vals[back_index] < vals[front_index]:
                tmp = vals[back_index]
                vals[back_index] = vals[front_index]
                vals[front_index] = tmp
    return vals