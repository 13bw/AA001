def check_perfect_number(number):
    sum_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i

    if sum_divisors == number:
        return True
    else:
        return False


def find_perfect_numbers(up_to_number):
    perfect_numbers = []

    for i in range(2, up_to_number + 1):
        if check_perfect_number(i):
            perfect_numbers.append(i)

    return perfect_numbers


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    perfect_numbers_up_to_input = find_perfect_numbers(number)

    print(perfect_numbers_up_to_input)
