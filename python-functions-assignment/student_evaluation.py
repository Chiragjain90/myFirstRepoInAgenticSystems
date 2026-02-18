def greeting(name):
    return f"Hello, {name}"


def calculate_average(scores):
    subjects = len(scores)
    average = sum(scores) / subjects
    return subjects, average


def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    name = input("Enter student name: ")

    scores = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        scores.append(mark)

    greet_msg = greeting(name)
    subjects, avg = calculate_average(scores)
    result = evaluate_result(avg)

    print("\n--- Student Report ---")
    print(greet_msg)
    print("Subjects:", subjects)
    print("Average Score:", avg)
    print("Result:", result)


if __name__ == "__main__":
    main()