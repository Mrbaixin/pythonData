# -*- coding: utf-8 -*-
L=[]
n=1
while n<99:
    L.append(n)
    n+=2
print(L)
print(len(L))

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print(L[-10:-3])
str='abcdefghijklmn'
print(str[::3])

#递归调用
def trim(s):
    if len(s)==0:
        return s
    elif s[-1]==' ':
        return trim(s[:-1])
    elif s[0]==' ':
        return trim(s[1:])
    else: return s

if __name__=="__main__":
    print(trim("    hello"))
    print(trim("hello    "))
    print(trim(" hello  "))
    print("   hello")
