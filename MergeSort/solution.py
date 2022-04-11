"""

"""


def mergeLeftRight(arr, left, right):
    i = len(arr) - 1
    j = len(left) - 1
    k = len(right) - 1
    inversions = 0

    if i < 1 or j == -1 or k == -1:
        return 0


    while k >= 0:
        if right[k] < left[j]:
            left[j], right[k] = right[k], left[j]
            j -= 1
            inversions += 1
        else:
            arr[i] = right[k]
        k -= 1
        i -= 1

    leftMid = len(left) // 2
    leftSwaps = mergeLeftRight(left, left[:leftMid], left[leftMid:])
    newArray = left + right
    i = 0

    while i < len(arr):
        arr[i] = newArray[i]
        i += 1
    
    return inversions + leftSwaps
    

def mergeSort(arr):
    mid = len(arr)//2

    if mid == 0:
        return 0

    L = arr[:mid]
    R = arr[mid:]

    leftInversions = mergeSort(L)
    rightInversions = mergeSort(R)
    
    return leftInversions + rightInversions + mergeLeftRight(arr, L, R)


if __name__ == "__main__":
    arr = [1, 3, 5, 7]
    print(mergeSort(arr))
    print(arr)
