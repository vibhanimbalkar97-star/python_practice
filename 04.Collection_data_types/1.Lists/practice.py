numbers = [1,2,3,4]
numbers.append(4)
print(numbers, numbers[0]) #[1, 2, 3, 4, 4] 1


numbers[0] = 100 
print(numbers, numbers[0]) #[100, 2, 3, 4, 4] 100

# print(numbers[5]) # index error if not present
