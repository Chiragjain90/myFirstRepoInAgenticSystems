def check_even_odd(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"


# main code
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result)