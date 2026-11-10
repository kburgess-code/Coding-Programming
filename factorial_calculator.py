"""
Filename: factorial_calculator.py
Author: <NAME>
Created: <DATE>
Instructor: Burgess
"""

def factorial():
    # Write your code here
    total = 0
    x = int(input("Enter a number: "))
    for i in range(x, 1,-1):
        #print("i:",i)
        #print("i-1:",i - 1)
        print("i*(i-1)",i*(i-1))
        total = total + (i*(i-1))
        print("\n")

    print("Total:",total)




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