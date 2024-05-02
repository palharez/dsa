def binarysearch(arr, target):

    lo = 0
    hi = len(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        v = arr[mid]

        if v == target:
            return mid
        elif v > target:
            hi = mid + 1
        else:
            lo = mid

    return -1


if __name__ == '__main__':
    print(binarysearch([i for i in range(100000)], 10), 10)
