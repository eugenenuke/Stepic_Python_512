#!/usr/bin/env python3

objects = [1, 2 , 1, 2, 3, "str", [1, 2]]

print(len(set(map(id, objects))))    # = print(len(set(id(x) for x in objects)))
