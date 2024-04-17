from sys import exit
from math import sqrt

def calcD(a, b, c) -> int:
    res = b**2 - (4*a*c)
    return res

def isValid(res:int) -> bool:
    if res < 0:
        return False
    return True

def calcEl(res:float, b:int) -> float:
    count = []
    x1 = -b - sqrt(res)
    x2 = b + sqrt(res)
    count.append(x1)
    count.append(x2)
    return count

def main() -> int:
    a = int(input())
    b = int(input())
    c = int(input())
    res = calcD(a, b, c)
    if not isValid(res):
        print("ошибка вычесления", res)
        exit(-3)
    print(calcEl(res, b))
    return 0

main() 