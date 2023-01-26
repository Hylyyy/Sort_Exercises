print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

numbers = [51, 30, 69, 100, 46, 63, 41, 19, 98, 49]
print("============= ARRAY VALUES ==============")
print(numbers)
print()
print("=========================================\n")

def insertion_sort(numbers):
    for h in range(1, len(numbers)):
        j = h
        while numbers[j - 1] > numbers[j] and j > 0:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            j -= 1
            print(numbers)

insertion_sort(numbers)
print("\n============= SORTED ARRAYS =============\n")
print(numbers)