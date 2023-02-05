def check_numbers(lst):
    first_number = lst[0]
    last_number = lst[len(lst) - 1]
    # Can put -1 as the index

    if first_number == last_number:
        return True
    else:
        return False


def main():
    number_list = []

    list_size = int(input("Size of list: "))

    for i in range(list_size):
        num = int(input("Number: "))

        number_list.append(num)

    print("Given list: " + str(number_list))
    print("Result is " + str(check_numbers(number_list)))

# WORKS, but with input, not hardcoded. (looked up how to put input into a list https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/)


if __name__ == '__main__':
    main()
