print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]

def sort(numbers):

    for h in range(5):
        mainpos = h
        for j in range(h,6):
            if numbers[j] < numbers[mainpos]:
                mainpos = j
        
        temp = numbers[h]
        numbers[h] = numbers[mainpos]
        numbers[mainpos] = temp