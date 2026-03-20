def get_input():
    """
    Get input from user
    :return: integer value
    """
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def calculate_factorial(n):
    """
    Calculate the mathematical factorial of a given integer
    :param n: integer value
    :return: factorial value
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

def main():
    """
    Main function to handle program flow
    """
    num = get_input()
    result = calculate_factorial(num)
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()