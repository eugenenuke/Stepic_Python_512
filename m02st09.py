#!/usr/bin/env python3

objects = [1, 2 , 1, 2, 3, "str", [1, 2]]

uniqs = []
for i in objects:
    if i not in uniqs:
        uniqs.append(i)

print(len(uniqs))
