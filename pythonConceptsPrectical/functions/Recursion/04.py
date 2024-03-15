def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

result = sum_of_digits(123)
print(result)
