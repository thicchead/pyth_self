def find_substring(str, to_find):
    str_list = str.split(" ")
    return str_list.count(to_find)


def main():
    x = input("String: ")
    find = input("What word to find? ")

    print("The substring " + find + " was found " + str(find_substring(x, find)) + " times.")


if __name__ == '__main__':
    main()
