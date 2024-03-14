"""
My goal is to create a program that generates trinomials that asks the user to factor them. 
The program will randomly select integers to represent solutions and display trinomials. 
The range of integers is determined by the difficulty of the trinomial. 
The trinomials will be presented in the form ax^2+bx+c and they should be factorable in the form (x+y)(x+z) or (ax+b)(cx+d). 
The values for y,z,a,b,c,d are all integers meaning that the user will input integers in their solutions. 
The user will select the level that they want to practice in.

Level "a" will allow the user to input the integers y and z to get comfortable identifying the values that are used to factor a trinomial. 
In level "a" the user will be given hints because many students factor incorrectly because they are missing a negative. 
Level "b" will allow the user to practice inputting their solution as (x+y)(x+z) so that they use their skills from level "a" to factor trinomials in level "b". 
Level "c" and level "b" both display the number of attempts the user takes to get the answer correct. 
Finally, level "c" will test the users ability to not only factor but factor by grouping.
"""

import random
import math


import random

def get_two_factors():
    """Returns two random numbers for y and z"""
    y = random.randint(-12, 12)
    z = random.randint(-12, 12)
    return y, z

def trinomials_a(factors):
    """Displays a trinomial for a user to factor where a = 1 in ax^2+bx+c."""
    y, z = factors
    print(f"x^2+{y+z}x+{y*z}")
    print("Factor the following in the form (x+y)(x+z).")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        user_input = input("Enter the values for 'y' and 'z' using ONLY ONE space: ").split()
        
        if len(user_input) != 2:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        
        try:
            y_guess, z_guess = map(int, user_input)
        except ValueError:
            print("Invalid input. Please enter two integers.")
            continue
        
        if y_guess + z_guess == y + z and y_guess * z_guess == y * z:
            print("You are correct!")
            break
        else:
            print("Incorrect. Try again.")
            attempts += 1
    else:
        print("Out of attempts. The correct answer is:", (y, z))

def trinomials_b():
    """Displays a trinomial for a user to factor in the form ax^2+bx+c where a = 1."""
    y, z = get_two_factors()
    print(f"x^2+{y+z}x+{y*z}")
    print("Factor the following in the form (x+y)(x+z).")

    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        user_input = input("Enter the values for 'y' and 'z' using ONLY ONE space: ").split()
        
        if len(user_input) != 2:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        
        try:
            y_guess, z_guess = map(int, user_input)
        except ValueError:
            print("Invalid input. Please enter two integers.")
            continue
        
        if (y_guess, z_guess) == (y, z):
            print("You are correct!")
            break
        else:
            print("Incorrect. Try again.")
            attempts += 1
    else:
        print("Out of attempts. The correct answer is:", (y, z))

def trinomials_c():
    """Displays a trinomial for a user to factor in the form ax^2+bx+c where a > 1."""
    a = random.randint(2, 5)
    b = random.randint(-5, 5)
    c = random.randint(2, 5)
    d = random.randint(-5, 5)
    
    print(f"{a}x^2 + {b}x + {c}x + {d}")
    print("Factor the following in the form (ax+b)(cx+d).")

    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        user_input = input("Enter the values for 'a', 'b', 'c', and 'd' separated by space: ").split()
        
        if len(user_input) != 4:
            print("Invalid input. Please enter four integers separated by spaces.")
            continue
        
        try:
            a_guess, b_guess, c_guess, d_guess = map(int, user_input)
        except ValueError:
            print("Invalid input. Please enter four integers.")
            continue
        
        if (a_guess, b_guess, c_guess, d_guess) == (a, b, c, d):
            print("You are correct!")
            break
        else:
            print("Incorrect. Try again.")
            attempts += 1
    else:
        print("Out of attempts. The correct answer is:", (a, b, c, d))

if __name__ == "__main__":
    user_entry = input("Which level would you like to practice in (a, b, or c)? ").lower()

    while user_entry not in ('a', 'b', 'c'):
        print("Invalid entry. Please type 'a', 'b', or 'c'.")
        user_entry = input("Which level would you like to practice in (a, b, or c)? ").lower()

    if user_entry == 'a':
        trinomials_a(get_two_factors())
    elif user_entry == 'b':
        trinomials_b()
    else:
        trinomials_c()

