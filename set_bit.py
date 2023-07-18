def set_bit(num1: int, num2: int) -> int:
    z = 0
    z ^= 1 << num1
    if num1 != num2:
        z ^= 1 << num2
    return z


try:
    number1 = int(input("Enter an integer : "))
    number2 = int(input("Enter an integer : "))
    print("The decimal is : ", set_bit(number1, number2))
except ValueError:
    print("Invalid input. Please enter only integers")
