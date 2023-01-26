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