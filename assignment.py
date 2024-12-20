# Simple Calculator Program

def main():
    print("Welcome to the Simple Calculator!")

    # Prompt user for inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ").strip()

        # Perform the calculation based on the operation
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for numbers.")

if __name__ == "__main__":
    main()

# List Manipulation Example

def list_operations():
    # Create an empty list
    my_list = []

    # Append elements to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    # Insert 15 at the second position
    my_list.insert(1, 15)

    # Extend the list with [50, 60, 70]
    my_list.extend([50, 60, 70])

    # Remove the last element
    my_list.pop()

    # Sort the list in ascending order
    my_list.sort()

    # Find and print the index of the value 30
    index_of_30 = my_list.index(30)
    print(f"The index of 30 in my_list is: {index_of_30}")

if __name__ == "__main__":
    list_operations()

# Discount Calculation Example

def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

if __name__ == "__main__":
    try:
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)

        if discount_percentage >= 20:
            print(f"The final price after applying the discount is: {final_price}")
        else:
            print(f"No discount applied. The original price is: {original_price}")

    except ValueError:
        print("Error: Please enter valid numeric values for price and discount percentage.")
