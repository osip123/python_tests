import math

def calcn(n: int) -> int:
    return math.factorial(n)

def calcA(k:int, n:int) -> int:
    res:int
    rn:int = calcn(n)
    res = n / math.factorial(n - k)
    return res

def main() -> int:
    print(calcA(5, 7))
    return 0

main()