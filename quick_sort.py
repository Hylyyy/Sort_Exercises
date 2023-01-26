print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]

def quicksort(numbers, left, right):
    if left < right:
        partition_position = partition(numbers, left, right)
        quicksort(numbers, left, partition_position - 1)
        quicksort(numbers, partition_position + 1, right)
                

def partition(numbers, left, right):
    h = left
    j = right - 1
    pivot = numbers[right]

    while h < j:
        while h < right and numbers[h] < pivot:
            h += 1
        while j > left and numbers[j] >= pivot:
            j -= 1
        if h < j:
            numbers[h], numbers[j] = numbers[h], numbers[h]

    if numbers[h] > pivot:
        numbers[h], numbers[right] = numbers[right], numbers[h]

    return h

quicksort(numbers, 0, len(numbers) -1)

print(numbers)