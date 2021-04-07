from bigO import BigO
from bigO import utils

# @utils.isSorted
def bubbleSort(arr):
    n  = len(arr)
    while True:
        swap = False
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
        if swap == False:
            break
    return arr

if __name__ == '__main__':
    lib = BigO()
    # complexity = lib.test(bubbleSort, 'random')
    # complexity = lib.test(bubbleSort, 'ksorted')
    bubbleSort(BigO.genRandomArray(100))
    print(bubbleSort(BigO.genRandomArray(100)))




