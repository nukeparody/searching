import random
import time

process_time = time.process_time()

random_numbers = []
sorted_random_numbers = []

for i in range(1000):
    random_numbers.append(random.randint(999, 9999))

sorted_random_numbers = sorted(random_numbers)
target_number = int(input("enter a number: "))

def binary_search(given_number, given_list):
    lowest = 0
    highest = len(given_list)

    while lowest <= highest:
        middle = (lowest + highest) // 2

        if given_number > given_list[middle]:
            lowest = middle - 1

        elif given_number < given_list[middle]:
            highest = middle + 1

        else:
            return middle

    return -1

def linear_search(given_number, given_list):
    for j in range(len(given_list)):

        if given_list[j] == given_number:
            return j

    return -1

print(linear_search(target_number, random_numbers))
print(binary_search(target_number, sorted_random_numbers))
print(f"the search took {time.process_time() - process_time} to complete")
