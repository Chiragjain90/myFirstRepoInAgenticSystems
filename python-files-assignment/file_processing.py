# file_processing.py

def read_numbers(file_name):
    """Read numbers from file and return list of integers."""
    numbers = []

    with open(file_name, "r") as file:
        log_message("File opened successfully")

        for line in file:
            value = line.strip()   # remove whitespace
            if value:
                numbers.append(int(value))

    log_message(f"Read {len(numbers)} numbers")
    return numbers


def compute_data(numbers):
    """Compute total count, sum and average."""
    total_count = len(numbers)
    total_sum = sum(numbers)

    average_value = 0
    if total_count > 0:
        average_value = total_sum / total_count

    log_message("Computation completed")

    return total_count, total_sum, average_value


def log_message(message):
    """Write logs to results.log in append mode."""
    with open("results.log", "a") as log_file:
        log_file.write(message + "\n")


def main():
    file_name = "python-files-assignment/data/numbers.txt"

    numbers = read_numbers(file_name)

    total_count, total_sum, average_value = compute_data(numbers)

    log_message(f"Total numbers: {total_count}")
    log_message(f"Sum: {total_sum}")
    log_message(f"Average: {average_value}")
    log_message("Processing completed")


if __name__ == "__main__":
    main()
