print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]
print("\t\tARRAY VALUES")
print(numbers)
print()
print("=========================================\n")

def sort(numbers):
    for h in range(len(numbers)-1,0,-1):
        for j in range(h):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

sort(numbers)

print(numbers)