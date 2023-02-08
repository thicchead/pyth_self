def check_palindrome(number):
    number = str(number)

    if number == number[::-1]:
        return True
    else:
        return False


def main():
    num = int(input("Number: "))

    print(check_palindrome(num))


if __name__ == '__main__':
    main()
