#!/usr/bin/env python3

# Напишите реализацию функции closest_mod_5, принимающую в качестве
# единственного аргумента целое число x и возвращающую самое маленькое
# целое число y, такое что:
# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    # if x%5 == 0:
    #     return x
    # return x-x%5+5
    return x%5 == 0 and x or x-x%5+5

print(closest_mod_5(6))
