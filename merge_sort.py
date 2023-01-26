print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]

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
        