def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input())
print("Number:", num)
print("Factorial:", factorial(num))