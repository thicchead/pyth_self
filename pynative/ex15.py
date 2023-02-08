def exponent(base, exp):
    answer = base ** exp

    return answer


def main():
    b = int(input("Base: "))
    e = int(input("Exponent: "))

    print(str(b) + " raises to the power of " + str(e) + " is: " + str(exponent(b, e)))
    print("i.e. (" + (str(b) + " * ") * (e - 1) + str(b) + " = " + str(exponent(b, e)) + ")")


if __name__ == '__main__':
    main()
