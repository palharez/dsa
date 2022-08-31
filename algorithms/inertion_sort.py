def insertion_sort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > element:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = element

    return arr

if __name__ == '__main__':
    print(insertion_sort([4, 2, 3, 1]))  # 1, 2, 3, 4