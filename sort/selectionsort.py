def get_min(arr):
    min_val, pos = arr[0], 0

    for i, n in enumerate(arr):
        if n < min_val:
            min_val = n
            pos = i

    return min_val, pos


def selection_sort(arr):
    temp_arr = []
    total = len(arr)

    while len(temp_arr) != total:
        min_val, pos = get_min(arr)

        temp_arr.append(min_val)
        arr.pop(pos)

    return temp_arr


if __name__ == '__main__':
    print(selection_sort([4, 2, 1, 3]), [1, 2, 3, 4])
