def main():
    str = input("String: ")
    print("Original string is " + str)

    print("Printing only even index chars: ")

# Pynative tests if the index is even in the range function, starting from 0 to the end,
# it jumps up 2 numbers. I just went through every index, testing if its even in an if
# statement. Can also use list slicing ([0::2])

    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i])


if __name__ == '__main__':
    main()
