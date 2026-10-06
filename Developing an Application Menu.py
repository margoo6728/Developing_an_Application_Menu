from datetime import datetime

# Program outputs Student ID and name of application  
print("margoo6728's Excel Spreadsheet Automation Menu")


def main():
    
    while True:
        show_menu()
        # The next line retrieves the inputted option and  
        # stores into the variable called choice
        choice = input().strip()
        timestamp = get_formatted_timestamp()

        if choice == "1":
            print(f"\nYou selected 1 at {timestamp}")
            break
        elif choice == "2":
            print(f"\nYou selected 2 at {timestamp}")
            break
        elif choice == "3":
            print(f"\nYou selected 3 at {timestamp}")
            break
        else:
            print(f"\n{timestamp} Invalid selection. Please choose 1, 2, or 3.")
    
# Program presents the options, including the number
def show_menu():
    print("Choose a number from the following options ")
    print("1. Input Data")
    print("2. View Current Data")
    print("3. Generate Report")

# Program receive the current date and time
def get_formatted_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    main()


