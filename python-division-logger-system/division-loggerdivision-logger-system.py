from datetime import datetime

def division_logger():
  while True:
    num_input = input("\nEnter an integer (or type 0 to exit): ")

    if num_input == "0":
        print("Program exited.")
        break

    try:
        num = int(num_input)
        result = 100 / num
        print("Result:", result)

        log_message = f"{datetime.now()} | Number: {num} | Result: {result}\n"

    except ValueError:
        print("Invalid input!")
        log_message = f"{datetime.now()} | Invalid input\n"

    except ZeroDivisionError:
        print("Cannot divide by zero!")
        log_message = f"{datetime.now()} | Division by zero attempt\n"

    finally:
        with open("division_log.txt", "a") as file:
            file.write(log_message)
        print("Logged successfully.")
    
division_logger()

# Display log history
print("\n------ Log History ------")
try:
    with open("division_log.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No log file found.")
