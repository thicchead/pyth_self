def calculate_tax(total_income):
    if total_income <= 10000:
        return 0
    elif total_income <= 20000:
        return (total_income - 10000) * 0.1
    else:
        return 10000 * 0.1 + (total_income - 20000) * 0.2


def main():
    income = int(input("Income: "))
    print(calculate_tax(income))


if __name__ == '__main__':
    main()
