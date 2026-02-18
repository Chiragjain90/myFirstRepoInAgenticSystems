def greet(name):
    return f"Hello, {name}!"


# main code
person_name = input("Enter your name: ")
message = greet(person_name)
print(message)