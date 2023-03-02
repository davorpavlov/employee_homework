# numbers = []

# for i in range(100):
#     numbers.append(i)
    
numbers = list(range(100))

first_element = numbers[0]
last_element = numbers[-1]


print()
print(numbers)
print()
print(first_element)
print(last_element)
print()

new_list = []
for i in range(10,21):
    new_list.append(numbers[i])

print(new_list)

new_list = numbers[10:21:2]
print(new_list)
