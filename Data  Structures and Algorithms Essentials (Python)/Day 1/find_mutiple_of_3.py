try:
    print(" ".join([number for number in input("Enter the numbers seperatad by spaces: ").split() if int(number) % 3 == 0]))
except ValueError:
    print("Please enter valid numbers")
