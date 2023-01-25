print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]
print("\t\tARRAY VALUES")
print(numbers)
print()
print("=========================================\n")
def sort(numbers):

    for h in range(9):
        mainpos = h
        for j in range(h,10):
            if numbers[j] < numbers[mainpos]:
                mainpos = j
        
        temp = numbers[h]
        numbers[h] = numbers[mainpos]
        numbers[mainpos] = temp

sort(numbers)

print(numbers)
