from functools import reduce
import math

def vector_add(*v_list):
    """多個向量相加"""
    return tuple(sum(i) for i in zip(*v_list))


def scalar_multiply(times, vector):
    """向量乘數"""
    return tuple(times * v for v in vector)


def vector_subtract(*v_list):
    """多個向量相減"""
    return vector_add(v_list[0], reduce(vector_add, (scalar_multiply(-1, v) for v in v_list[1:])))


def product(*v_list):
    """多個向量相乘"""
    return reduce(lambda x, y: x*y, v_list)


def dot(*v_list):
    """多個向量點積"""
    return reduce(lambda x,y: x+y, (product(*i) for i in zip(*v_list)))


def vector_mean(vector):
    """向量平均"""
    return(scalar_multiply(len(vector) ** -1, vector))


def sum_of_squares(vector):
    """向量平方和"""
    return dot(vector, vector)


def magnitude(vector):
    """向量長度"""
    return math.sqrt(sum_of_squares(vector))


def distance(vector1, vector2):
    """兩個向量間的距離"""
    return math.sqrt(sum_of_squares(vector_subtract(vector1, vector2)))
