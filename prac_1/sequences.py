"""Display number sequences selected from a menu."""

MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y
4. Exit the program"""

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(MENU)
choice = input(">>> ")
while choice != "4":
    if choice == "1":
        for number in range(x, y + 1):
            if number % 2 == 0:
                print(number, end=" ")
        print()
    elif choice == "2":
        for number in range(x, y + 1):
            if number % 2 == 1:
                print(number, end=" ")
        print()
    elif choice == "3":
        for number in range(x, y + 1):
            print(number ** 2, end=" ")
        print()
    else:
        print("Invalid choice")

    print(MENU)
    choice = input(">>> ")

print("Finished.")
