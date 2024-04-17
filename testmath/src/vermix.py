from itertools import product

def hendler(s:str, n:int) -> str:
    res = []
    for s in product(s, repeat=n):
        res.append(s)
    print(res)
    return res

def validator(s:str) -> int:
    mes = []
    bad = []
    for i in s:
        mes.append(i)

    for j in mes:
        if j[0] == j[1] or j[1] == j[2] or j[0] == j[2] or j[0] == j[1] and j[1] == j[2]:
            bad.append(j)
    result = len(s) - len(bad)
    return result

def main() -> int:
    s:str = "asdf"
    n:int = 3
    sw = hendler(s, n)
    res = validator(sw)
    print(res)
    return 0
    
main()