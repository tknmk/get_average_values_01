# -*- coding: utf-8 -*-
import numpy as np


def main():

    lst = [1,2,3,4,5]
    
    lst_01 = get_average_by_sum(lst)
    print('by sum(): ')
    print(lst_01)


    lst_02 = get_average_by_numpy(lst)
    print('by numpy: ')
    print(lst_02)



# Using sum()
def get_average_by_sum(lst):

    average = sum(lst)/len(lst)
    return average


# Using numpy
def get_average_by_numpy(lst):
    return np.mean(lst)


if __name__ == '__main__':
    main()
