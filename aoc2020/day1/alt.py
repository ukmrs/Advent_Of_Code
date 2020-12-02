#!/usr/bin/env python3
"""amusing bruteforce"""
from itertools import combinations as cb
from math import prod as pd
tg, a = 2020, 3

with open("input.txt") as f:
    s = [pd(i) for i in cb([int(i) for i in f.readlines()], a) if sum(i) == tg]

print(s[0])
