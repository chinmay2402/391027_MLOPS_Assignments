try:
    result = 100 / 0
except ZeroDivisionError:
    result = "Cannot divide by zero"
print(result)  # Output: Cannot divide by zero

print("------------------------------------------------------------------------------------------")

index = 0
for fruit in ["Apple","Banana","Blackberry","Cherry","orange"]:
    if fruit.lower() == "orange":
        print(f"Index of 'orange': {index}")
        break
    index += 1
else:
    print("'Orange' is not in the list.")

print("-------------------------------------------------------------------------------------------")

def print_pyramid(height):
    for i in range(1, height + 1):
        print('*' * i)
        
try:
    pyramid_height = int(input("Enter the height of the pyramid: "))
    if pyramid_height > 0:
        print_pyramid(pyramid_height)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
