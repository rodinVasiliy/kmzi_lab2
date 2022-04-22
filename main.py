from random import randint
import numpy as np
from numpy import zeros
from Matrix import Matrix
from cumulative_sum import CumulativeSums
from random_excursions_test import RandomExcursions


def lfsr1(n):
    flag = 0
    period = 0
    cnt = 0
    start_state = 0b1101001
    state = 0b11101001
    lst = list()
    lst.append(state & 1)
    while (cnt < n):
        newbit = ((state >> 7) ^ (state >> 1) ^ state) & 1
        state = (state >> 1) | (newbit << 6)
        lst.append(state & 1)
        cnt += 1
        if start_state == state and flag == 0:
            flag = 1
            period = cnt
    string = "".join(map(str, lst))
    return lst, string, period


def lfsr2(n):
    flag = 0
    period = 0
    cnt = 0
    start_state = 0b11111111
    state = 0b11111111
    lst = list()
    lst.append(state & 1)
    while (cnt < n):
        newbit = ((state >> 7) ^ (state >> 5) ^ (state >> 3) ^ state) & 1
        state = (state >> 1) | (newbit << 6)
        lst.append(state & 1)
        cnt += 1
        if start_state == state and flag == 0:
            flag = 1
            period = cnt
    string = "".join(map(str, lst))
    return lst, string, period


def lfsr3(n):
    flag = 0
    period = 0
    cnt = 0
    start_state = 0b00101001
    state = 0b00101001
    lst = list()
    lst.append(state & 1)
    while (cnt < n):
        newbit = ((state >> 7) ^ (state >> 5) ^ (state >> 1) ^ state) & 1
        state = (state >> 1) | (newbit << 6)
        lst.append(state & 1)
        cnt += 1
        if start_state == state and flag == 0:
            flag = 1
            period = cnt
    string = "".join(map(str, lst))
    return lst, string, period


def sequence_period(sequence):
    period = []
    period.append(sequence[0])
    i = 0
    k = 0
    while k + len(period) <= len(sequence):
        tmp = sequence[i * len(period):(i + 1) * len(period)]
        if period != tmp:
            period.append(sequence[len(period)])
            i = 0
        else:
            i += 1
            k = len(period) * i
    sub = len(sequence) - k
    if sub < len(period):
        for i in range(0, sub):
            if period[i] != sequence[len(sequence) - sub + i]:
                return sequence
        return period
    else:
        return period


# def lfsr(condition, polynom, polynom_size, result_size):
#     result_array = []
#     new_condition = condition.copy()
#     for j in range(0, result_size):
#         xor = 0
#         for i in range(0, polynom_size):
#             if polynom[i] == 1:
#                 xor ^= new_condition[i]
#         new_condition.insert(0, xor)
#         result = new_condition.pop(-1)
#         result_array.insert(len(result_array), result)
#
#     return result_array


def select_generator(first, second, third):
    # result_array = []
    # for j in range(0, len(first)):
    #     if first[j] == 0:
    #         result_array.insert(0, second[j])
    #     else:
    #         result_array.insert(0, third[j])
    # return result_array
    lst = list()
    for j in range(0, len(first)):
        if first[j] == 0:
            lst.append(second[j])
        else:
            lst.append(third[j])
    string = "".join(map(str, lst))
    return string


if __name__ == '__main__':
    SIZE = 100000
    first, first_str, first_period = lfsr1(SIZE)
    second, second_str, second_period = lfsr2(SIZE)
    third, third_str, third_period = lfsr3(SIZE)
    result = select_generator(first, second, third)
    print(result)
    print(Matrix.binary_matrix_rank_text(result))
    print(CumulativeSums.cumulative_sums_test(result))
    random_excursions_test_result = RandomExcursions.random_excursions_test(result)
    print('Random Excursion Test:')
    print('\t\t STATE \t\t\t xObs \t\t\t\t P-Value \t\t\t Conclusion')
    for item in random_excursions_test_result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              (item[4] >= 0.01))
