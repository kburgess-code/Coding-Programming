"""
Filename: fibonacci.py
Author: <Mr. Burgess>
Created: <11/19/26>
Instructor: Burgess
"""

def n_fibonacci():
    # Write your code here
    a = 0
    b = 1

    n = int(input("Enter a non-negative whole number: "))


    for _ in range(n):
        print(a)
        temp = a+b
        a = b
        b = temp


# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("\nPrint another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()