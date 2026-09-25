def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

num = int(input())
print("Number:", num)
print("Divisors:", get_divisors(num))