#!/usr/bin/env python3

# Сочетанием из n элементов по k называется подмножество этих n
# элементов размера k. Два сочетания называются различными, если одно
# из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний
# из n по k. Обозначим это число за C(n, k)
#
# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

def C(n,k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return C(n-1, k) + C(n-1, k-1)

n,k = map(int, input().split())
print(C(n,k))
