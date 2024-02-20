def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(fibonacci_sequence(num))
