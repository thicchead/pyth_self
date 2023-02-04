def mult_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return "The result is " + str(product)
    else:
        return "The result is " + str(num1 + num2)


def main():
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))

    print(mult_or_sum(number1, number2))

# WRONG:
# Make an extra function for the multiplication and if statement
    # if number1 * number2 <= 1000:
    #     print("The result is " + str(number1 * number2))
    # else:
    #     print("The result is " + str(number1 + number2))


if __name__ == '__main__':
    main()
