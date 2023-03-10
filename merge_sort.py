print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]
print("============= ARRAY VALUES ==============")
print(numbers)
print()
print("=========================================\n")

def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        #recusion
        merge_sort(left_array)
        merge_sort(right_array)

        #merge
        h = 0 #left_array 
        j = 0 #right_array
        l = 0 #merged array
        while h < len(left_array) and j < len(right_array):
            if left_array[h] < right_array[j]:
                array[l] = left_array[h]
                h += 1
            else:
                array[l] = right_array[j]
                j += 1
            l += 1

        while h < len(left_array):
            array[l] = left_array[h]
            h += 1
            l += 1
        
        while j < len(right_array):
            array[l] = right_array[j]
            j += 1
            l += 1
    print(array)

merge_sort(numbers)
print("\n============= SORTED ARRAYS =============\n")
print(numbers)