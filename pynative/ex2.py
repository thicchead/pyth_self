def main():
# WRONG
# First previous number is -1, should be 0. Sum is sum of this and last digit, not total sum
    # num_sum = 0
    print("Printing current and previous number sum in a range(10)")
    previous_num = 0
    for i in range(10):
        # num_sum += i
        print("Current number: " + str(i) + " Previous number: " + str(previous_num) + " Sum: " + str(previous_num + i))
        previous_num = i


if __name__ == '__main__':
    main()
