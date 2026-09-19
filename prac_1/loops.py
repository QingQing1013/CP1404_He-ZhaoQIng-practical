"""Practise definite iteration with for loops and range."""

# Original: display odd numbers from 1 to 20.
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# a. Count in tens from 0 to 100.
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b. Count down from 20 to 1.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c. Print a user-selected number of stars on one line.
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# d. Print lines containing increasing numbers of stars.
number_of_lines = int(input("Number of lines: "))
for i in range(1, number_of_lines + 1):
    print("*" * i)
