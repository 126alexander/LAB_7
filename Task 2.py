#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [1.25, -0.5, 6.482, 0.333, -5.25, 1.75]

print(sum(a[1::2]))

print(sum(a[min(map(a.index, map(lambda x: x if x < 0 else a[-1], a))) + 1: max(map(a.index, map(lambda x: x if x < 0 else a[0], a)))]))

a = [i if abs(i) > 1 else '0' for i in a]
for i in range(a.count('0')):
  a.remove('0')
  a.append(0)

print(*a)
