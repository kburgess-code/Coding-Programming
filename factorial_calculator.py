"""
Filename: factorial_calculator.py
Author: <NAME>
Created: <DATE>
Instructor: Burgess
"""

def factorial():
    # Write your code here
    total = 1
    x = int(input("Enter a number: "))
    if x == 0:
        print("!0 = 1")

    else:
        print(f"{x}! = ", end="")

        for i in range(x, 0,-1):
            if i > 1:
                print(f"{i} * ", end="")
            else:
                print(f"{i}", end="")
            total *= i

        print(" = ",total)




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