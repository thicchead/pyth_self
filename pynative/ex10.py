def create_list(first_list, second_list):
    new_list = []
    for number in first_list:
        if number % 2 != 0:
            new_list.append(number)

    for number in second_list:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


def main():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]

    print("Result list: " + str(create_list(list1, list2)))


if __name__ == '__main__':
    main()
