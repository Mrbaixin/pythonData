#--*utf-8*--
import math
# #用来调用其他文件函数
# from a1 import trim
# print(trim("hello   "))
#
#空函数
def novalue():
    pass
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 求解二元一次方程的解
def quadratic(a, b, c):
    # 改进(考虑要全面！！！)：  if not isinstance(a, (int, float)) or isinstance(b, (int, float)) or isinstance(c, (int, float)) :
    # raise TypeError('bad operand type')
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError("bad operand type")
    if a!=0:
        if b*b-4*a*c>=0:
            return (-b+math.sqrt(b*b-4*a*c))/2*a,(-b-math.sqrt(b*b-4*a*c))/2*a
        else:return "函数无实数解"
    elif b!=0:
        return -c/b;
    else: return "不是方程"
# def sum( numbers=[]):
def sum(*numbers):
    sum=0;
    for i in numbers:
        sum+=i
    return sum;
def person(name,age,**kk):
    print('name:', name,'age:',age, 'other:',kk)

def product(a,*num):
    if len(num)==0:
        return a
    else:
        mul=a
        for i in num:
            mul*=i
        return mul;

def move(n,a,b,c):
    if n==1:
        print(a,'--->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

if __name__=="__main__":
    # my_abs('x')
    # print(my_abs(-10))
    # l=move(1,2,3,4)
    # print(move(1,2,3,4))
    # print(l)
    #
    # L=quadratic(1,1,1)
    # print(L)
    # s=sum([1,2,34,5,5,6,64,4])
    '''
    num=[1,2,3,4,5,6]
    s=sum(*num)
    print(s)
    person("zhangsan",20)
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person("zs",21,**extra)
    print(product(2,3))
    print(product(2,3,4,5)) '''
    move(3,'A','B','C')