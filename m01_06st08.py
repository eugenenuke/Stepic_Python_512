#!/usr/bin/env python3

class ExtendedStack(list):
    def sum(self):
        #
        self.append(self.pop() + self.pop())

    def sub(self):
        #
        self.append(self.pop() - self.pop())

    def mul(self):
        #
        self.append(self.pop() * self.pop())

    def div(self):
        #
        self.append(self.pop() // self.pop())

x = ExtendedStack()
x.append(1)
x.append(2)
print(x)
x.sum()
print(x)

