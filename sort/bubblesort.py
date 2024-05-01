def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

    return arr


if __name__ == '__main__':
    print(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])
