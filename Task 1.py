#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

n=int(input("n: "))
u = []
d = []
v = []
s = []

for i in range(0, n):
  u.append(random.randint(5, 99))
  d.append(random.randint(15, 99))
  v.append(random.randint(10, 99))
  s.append( (u[i]+d[i]+v[i]) / 3 )

print('Утро:', end = "\n\t")
for i in range(0, n):
  print(u[i], end = "\t")

print('\nДень:', end = "\n\t")
for i in range(0, n):
  print(d[i], end = "\t")

print('\nВечер:', end = "\n\t")
for i in range(0, n):
  print(v[i], end = "\t")

print('\nСреднее:', end = "\n\t")
for i in range(0, n):
  print(f"{s[i]:0.2f}", end = "\t")