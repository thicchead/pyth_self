def remove_chars(orig, n):
    return orig[n:]


def main():
    first_string = input("Original string = ")
    deleter = int(input("Remove ... characters: "))

    while deleter > len(first_string):
        print("Original string does not have enough characters!")
        deleter = int(input("Remove ... characters: "))

    print(remove_chars(first_string, deleter))

# WORKS perfectly, checks for length, and does it with input, not hardcoding it.


if __name__ == '__main__':
    main()
