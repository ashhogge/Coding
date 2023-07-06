numbers = []
number = -1
smallest_pos = None

print("Enter a list of numbers, type 0 when finished.")
while number != 0:
    number = float(input("Enter number: "))
    numbers.append(number)

    if number > 0 and (smallest_pos is None or number < smallest_pos):
        smallest_pos = number

total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
sorted_nums = sorted(numbers)

print("The sum is:", total)
print("The average is:", average)
print("The largest number is:", maximum)
print("The smallest positive number closest to zero is:", smallest_pos)
print("The sorted list of numbers is:", sorted_nums)