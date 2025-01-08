list = [24,12,13,15]
res = [i for i in list if i < 4]
print(res)
res = [i for i in list if i % 2 == 0]
print(res)

list = ["apple","bannana","kiwi","pine apple"]
a = [i for i in list if "e" in i]
print(a)