def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)
input = 5
# factorial = 1
# for i in range(1,6):
#     factorial *= i
print(factorial(input))
