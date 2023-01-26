print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]

def quicksort(array, left, right):
    if left < right:
        partition_position = partition(array, left, right)
        quicksort(array, left, partition_position - 1)
        quicksort(array, partition_position + 1, right)
                

def partition(array, left, right):
    h = left
    j = right - 1
    pivot = array[right]

    while h < j:
        while h < right and array[h] < pivot:
            h += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if h < j:
            array[h], array[j] = array[h], array[h]

    if array[h] > pivot:
        array[h], array[right] = array[right], array[h]

    return h

quicksort(array, 0, len(array) -1)

print(array)