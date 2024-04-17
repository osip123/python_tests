import sys

def binarserch(arr:int, ref:int) -> int:
    res:int = 1
    j = len(arr) // 2
    if arr[j] == ref:
        res = j
        print(res)
    if arr[j] < ref:
        for q in range(0, len(arr) // 2):
            if arr[q] == ref:
                res = q
                return res
    if arr[j] > ref:
        for q in range(len(arr) // 2, len(arr)):
            if arr[q] == ref:
                res = q
                return res
    else:
        print("ошибка выполнения" -1)
        sys.exit(-1)



def main() -> int:
    ref = 3
    arr = [1, 2, 3, 4, 5, 6]
    print(binarserch(arr, ref))
    return 0

main()