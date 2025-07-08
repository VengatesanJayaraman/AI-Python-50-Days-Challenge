def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

while True:
    user_input = input("\nEnter a number or list of numbers (comma separated), or type 'exit' to quit: ")

    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    try:
        # Check if multiple numbers are entered
        if ',' in user_input:
            numbers = [int(num.strip()) for num in user_input.split(',')]
            for num in numbers:
                print(check_even_odd(num))
        else:
            number = int(user_input.strip())
            print(check_even_odd(number))

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
