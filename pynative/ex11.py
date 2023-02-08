def main():
    number = input("Number: ")
    number = number[::-1]

    for i in range(len(number)):
        print(number[i], end=" ")


if __name__ == '__main__':
    main()
