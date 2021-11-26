'''
A collection of Unit Tests for the sorting algorithms located within this directory.
Will test for correctness of the sorting algorithms.
'''
from sys import argv
from random import randint
from selection_sort import selection_sort
from numpy import bincount

def main(number_sorts = 100, list_length = 1000):
    ascending_list = []
    for x in range(0, list_length):
        ascending_list.append(x)
    
    random_lists = []
    sorted_lists = []
    for x in range(0, number_sorts):
        random_list = []
        sorted_list = []
        for i in range(0, list_length):
            random_list.append(randint(0, list_length))
        random_lists.append(random_list)

        bncount = bincount(random_list)
        for x in range(0, len(bncount)):
            for y in range(0, bncount[x]):
                sorted_list.append(x)
        sorted_lists.append(sorted_list)
    
    test_count = 0
    for test_sort in random_lists:
        assert selection_sort(test_sort) == sorted_lists[test_count], "Test " + str(test_count) + " failed"
        print(test_sort)
        test_count += 1


if __name__ == "__main__":
    main(int(argv[1]), int(argv[2]))