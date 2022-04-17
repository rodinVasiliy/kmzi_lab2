from main import lfsr1, lfsr2
from random import randint


# x - 1 последовательность
# y - 2 последовательность
# k - размер матрицы
# N - размер выходной последовательности
def mc_laren_marsaglia_generator(x, y, k, N):
    z = []
    v = x[:k]
    print(v)
    for i in range(0, N):
        index_x = randint(0, len(x) - 1)
        X = x[index_x]
        index_y = randint(0, len(y) - 1)
        Y = y[index_y]
        m = k * Y
        z[i] = v[m]
        v[m] = X

    return z


if __name__ == '__main__':
    SIZE = 10000
    x, str_x, per_x = lfsr1(SIZE)
    y, str_y, per_y = lfsr2(SIZE)
    k = 128  # размер матрицы
    N = 20000
    result = mc_laren_marsaglia_generator(x, y, k, N)
    print(result)