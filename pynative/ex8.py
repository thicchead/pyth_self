def main():
    length = int(input("Length triangle: "))

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


if __name__ == '__main__':
    main()
