from random import randint


def lfsr(condition, polynom, size):
    result_array = []
    new_condition = condition.copy()
    while True:
        xor = 0
        for i in range(0, size):
            if polynom[i] == 1:
                xor ^= new_condition[i]
        new_condition.insert(0, xor)
        result = new_condition.pop(-1)
        # print(f"condition {condition}")
        # print(f"polynom {polynom}")
        # print(f"new_condition {new_condition}")
        if condition == new_condition:
            return result_array
        else:
            result_array.insert(len(result_array), result)


def get_array(polynom, size):
    result_array = []
    condition = [randint(0, 1) for k in range(0, 8)]
    while len(result_array) < size:
        result_array.extend(lfsr(condition, polynom, 8))
    return result_array


if __name__ == '__main__':
    a = [0] * 8
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
    first_result = get_array(FIRST_POLYNOM, SIZE)
    second_result = get_array(SECOND_POLYNOM, SIZE)
    third_result = get_array(THIRD_POLYNOM, SIZE)
    print(first_result)
    # print(second_result)
    # print(third_result)
