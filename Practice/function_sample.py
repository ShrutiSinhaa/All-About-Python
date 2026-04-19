def get_input():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    return a, b


def operation(a, b):
    total = a + b
    diff = a - b
    product = a * b
    return total, diff, product


def print_result(total, diff, product):
    print(f"The sum is: {total}")
    print(f"The difference is: {diff}")
    print(f"The product is: {product}")


# Main program
a, b = get_input()
total, diff, product = operation(a, b)
print_result(total, diff, product)