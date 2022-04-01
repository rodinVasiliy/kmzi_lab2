from random import randint


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


if __name__ == '__main__':
    POLYNOM_SIZE = 8
    a = [0] * POLYNOM_SIZE
    FIRST_POLYNOM = a.copy()
    FIRST_POLYNOM[0] = FIRST_POLYNOM[1] = FIRST_POLYNOM[7] = 1
    FIRST_POLYNOM.reverse()
    SECOND_POLYNOM = a.copy()
    SECOND_POLYNOM[0] = SECOND_POLYNOM[3] = SECOND_POLYNOM[5] = SECOND_POLYNOM[7] = 1
    SECOND_POLYNOM.reverse()
    THIRD_POLYNOM = a.copy()
    THIRD_POLYNOM[0] = THIRD_POLYNOM[1] = THIRD_POLYNOM[5] = THIRD_POLYNOM[7] = 1
    THIRD_POLYNOM.reverse()
    SIZE = 10000
    condition = [randint(0, 1) for k in range(0, 8)]
    first_result = lfsr(condition, FIRST_POLYNOM, POLYNOM_SIZE, SIZE)
    second_result = lfsr(condition, SECOND_POLYNOM, POLYNOM_SIZE, SIZE)
    third_result = lfsr(condition, THIRD_POLYNOM, POLYNOM_SIZE, SIZE)
    print(first_result)
    # print(second_result)
    # print(third_result)
