"""
Filename: factorial_calculator.py
Author: <NAME>
Created: <DATE>
Instructor: Burgess
"""

def factorial():
    # Write your code here
    print("I'm inside factorial function...")


# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()