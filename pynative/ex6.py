def check_divisible(lst, divis):
    for element in lst:
        if element % divis == 0:
            print(element)


def main():
    number_list = []
    divis_num = int(input("Should be divisible by: "))
    list_size = int(input("Size of list: "))

    for i in range(list_size):
        num = int(input("Number: "))
        number_list.append(num)

    print("Given list is " + str(number_list))
    print("Divisible by " + str(divis_num))
    check_divisible(number_list, divis_num)

# WORKS, put a little extra by not only dividing by 5, but for a number the user chooses


if __name__ == '__main__':
    main()
