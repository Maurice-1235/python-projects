def fibonacci(input):
    if input < 1:
        return 0
    elif input == 1 or input == 2:
        return 1
    else:
        return fibonacci(input-1)+ fibonacci(input-2)
print (fibonacci(6))
