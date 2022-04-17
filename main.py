from random import randint
import numpy as np

from Matrix import Matrix
from cumulative_sum import CumulativeSums

def lfsr1(n):
    flag = 0
    period = 0
    cnt = 0
    start_state = 0b1101001
    state = 0b11101001
    lst = list()
    lst.append(state & 1)
    while(cnt < n):
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
    while(cnt < n):
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
    while(cnt < n):
        newbit = ((state >> 7) ^ (state >> 5) ^ (state >> 1) ^ state) & 1
        state = (state >> 1) | (newbit << 6)
        lst.append(state & 1)
        cnt += 1
        if start_state == state and flag == 0:
            flag = 1
            period = cnt
    string = "".join(map(str, lst))
    return lst, string, period


def lfsr(condition, polynom, polynom_size, result_size):
    result_array = []
    new_condition = condition.copy()
    for j in range(0, result_size):
        xor = 0
        for i in range(0, polynom_size):
            if polynom[i] == 1:
                xor ^= new_condition[i]
        new_condition.insert(0, xor)
        result = new_condition.pop(-1)
        result_array.insert(len(result_array), result)

    return result_array


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

#тест бинарных матриц
def get_matrix_with_rank(sequence, rank):
    M = 32
    sequence_copy = sequence.copy()
    matrix_cont = list()
    rank_cont = 0
    res = 0
    while len(sequence_copy) > M ** 2:
        for i in range(M):
            matrix_cont.append(list())
            for j in range(M):
                matrix_cont[-1].append(sequence_copy.pop(0))

        matrix_cont = np.matrix(matrix_cont)
        rank_cont = np.linalg.matrix_rank(matrix_cont)
        if rank_cont == rank:
            res += 1
        matrix_cont = list()
    return res


def get_PR(R):
    Q = M = 32
    PR = 2.0 ** (R * (Q + M - R) - M * Q)
    mult = 1.0
    for i in range(R):
        mult *= (1.0 - 2.0 ** (i - Q)) * (1.0 - 2.0 ** (i - M)) / (1.0 - 2.0 ** (i - R))
    PR *= mult
    return PR

def bin_matrix_rank_test(sequence):
    M = 32
    chi = 0
    N = np.floor(len(sequence) / M ** 2)
    Pi = 0
    for i in range(1, M + 1):
        Pi = get_PR(i)
        chi += (get_matrix_with_rank(sequence, i) - N * Pi) ** 2 / (N * Pi)

    p = np.exp(-chi / 2)
    return p >= 0.01


if __name__ == '__main__':
    SIZE = 100000
    first, first_period = lfsr1(SIZE)
    second, second_period = lfsr2(SIZE)
    third, third_period = lfsr3(SIZE)
    result = select_generator(first, second, third)
    print(result)
    print(Matrix.binary_matrix_rank_text(result))
    print(CumulativeSums.cumulative_sums_test(result))
    # POLYNOM_SIZE = 8
    # a = [0] * POLYNOM_SIZE
    # FIRST_POLYNOM = a.copy()
    # FIRST_POLYNOM[0] = FIRST_POLYNOM[1] = FIRST_POLYNOM[7] = 1
    # FIRST_POLYNOM.reverse()
    # SECOND_POLYNOM = a.copy()
    # SECOND_POLYNOM[0] = SECOND_POLYNOM[3] = SECOND_POLYNOM[5] = SECOND_POLYNOM[7] = 1
    # SECOND_POLYNOM.reverse()
    # THIRD_POLYNOM = a.copy()
    # THIRD_POLYNOM[0] = THIRD_POLYNOM[1] = THIRD_POLYNOM[5] = THIRD_POLYNOM[7] = 1
    # THIRD_POLYNOM.reverse()
    # SIZE = 10000
    # condition = [randint(0, 1) for k in range(0, 8)]
    # first_result = lfsr(condition, FIRST_POLYNOM, POLYNOM_SIZE, SIZE)
    # second_result = lfsr(condition, SECOND_POLYNOM, POLYNOM_SIZE, SIZE)
    # third_result = lfsr(condition, THIRD_POLYNOM, POLYNOM_SIZE, SIZE)
    # # print(first_result)
    # # print(second_result)
    # # print(third_result)
    # result = select_generator(first_result, second_result, third_result)
    # np_result = np.array(result)
    # print(np_result)
    # result_of_bin_matrix_test = Matrix.binary_matrix_rank_text(result)
    # print(result_of_bin_matrix_test)

