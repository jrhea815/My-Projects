#TODO: Allow user limited amount of attempts
#TODO: Create an exercise where the user inputs (x+y)(x+z)
#TODO: Create a function that keeps track of user's score

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


def get_two_factors():
  """ Returns two random numbers for y and z"""
  y = random.randint(-12,12)
  z = random.randint(-12,12)
  return y,z

def get_four_integers():
  """Returns four random integers a, b, c, d"""

  a = random.randint(-5,5)
  b = random.randint(-5,5)
  c = random.randint(-5,5)
  d = random.randint(-5,5)

  excluded_nums = [0]

  if a in excluded_nums:
    a = random.randint(1,5)
  if b in excluded_nums:
    b = random.randint(-5,-1)
  if c in excluded_nums:
    c = random.randint(1,5)
  if d in excluded_nums:
    d = random.randint(-5,-1)

  return a,b,c,d
  
def get_trinomial_a(y: int, z: int) -> str: 
  """ Returns a trinomial in the form ax^2+bx+c where a = 1
  >>> get_trinomial_a(4 ,6)
  'x^2+10x+24'
  >>> get_trinomial_a(0, 0)
  'x^2+0x+0'
  >>> get_trinomial_a(-3, -6)
  'x^2-9x+18'
  >>> get_trinomial_a(-2,7)
  'x^2+5x-14'
  """
  #trinomials with the coefficent of x^2
  b = y+z
  c = y*z
  
  middle = f"+{b}" if b>=0 else b
  last = f"+{c}" if c>=0 else c
  
  return (f"x^2{middle}x{last}")

def get_trinomial_c(a: int, b: int, c: int, d: int):
  """ Takes a "factored trinomial" in the form (ax+b)(cx+d) and returns a trionmial in the form ax^2+bx+c.
  >>> get_trinomial_c(4, 5, 2, -6)
  '8x^2-14x-30'
  >>> get_trinomial_c(0, 0, 0, 0)
  '0x^2+0x+0'
  >>> get_trinomial_c(1, 1, 1, 1)
  'x^2+2x+1'
  """
  first = a * c
  second = (a * d) + (b * c)
  third = b * d

  first = "" if first == 1 else first
  middle = f"+{second}" if second>=0 else second
  last = f"+{third}" if third>=0 else third
  
  return f"{first}x^2{middle}x{last}"
  
def get_user_input_a() -> (int, int):
  """ Takes user input and returns two integers.
  >>> from fakeinput import FakeInput
  >>> with FakeInput("1 2"): get_user_input_a()
  (1, 2)
  >>> with FakeInput("0 -2"): get_user_input_a()
  (0, -2)
  """
  
  user_solution = input()

  solution_list = user_solution.split()
  if len(solution_list) >= 2:
    if len(solution_list[0]) > 1:
      item_1 = solution_list[0][1]
    else:
      item_1 = solution_list[0]
  
    if len(solution_list [1]) > 1:
      item_2 = solution_list[1][1]
    else:
      item_2 = solution_list[1]
    
  while len(solution_list) != 2 or not item_1.isdigit() or not item_2.isdigit() : #user must have two numbers to answer the question
    print("Invalid entry. Try Again!")
    solution_list = input().split()
    if len(solution_list) >= 2:
      if len(solution_list[0]) != 1:
        item_1 = solution_list[0][1]
      else:
        item_1 = solution_list[0]
      if len(solution_list [1]) > 1:
        item_2 = solution_list[1][1]
      else:
        item_2 = solution_list[1]

  solution_one, solution_two = solution_list
    
  sol_a = int(solution_one)
  sol_b = int(solution_two)

  return sol_a, sol_b

def extract_ints_b(string: str) -> list[int, int]:
  """ Returns integers y and z from the from (x+y)(x+z)
  >>> extract_ints_b('(x+2)(x+3)')
  [2, 3]
  >>> extract_ints_b('(x-2)(x-3)')
  [-2, -3]
  >>> extract_ints_b('(x+1)(x-1)')
  [1, -1]
  """
  
  string_list = []
  char_string = ""
  for char in string:
    if char.isdigit() or char in "-":
      char_string += char
    else:
      string_list.append(char_string)
      char_string = ''

  numlist = []    
  for item in string_list:
    if item not in '':
      numlist.append(int(item))
  
  return numlist

def extract_ints_c(string: str) -> list[int,int,int,int]:
  """ Returns the integers a,b,c,d from the form (ax+b)(cx+d)
  >>> extract_ints_c('(2x+13) (10x+5)')
  [2, 13, 10, 5]
  >>> extract_ints_c('(5x-4)(3x-6)')
  [5, -4, 3, -6]
  >>> extract_ints_c('(-2x+3)(4x-5)')
  [-2, 3, 4, -5]
  >>> extract_ints_c('(x-4)(-x+5)')
  [1, -4, -1, 5]
  >>> extract_ints_c('')
  []
  >>> extract_ints_c('(3x-2)')
  [3, -2]
  """
  string_list = []
  char_string = ""
  for char in string:
    if char.isdigit() or char in "-":
      char_string += char
    elif char == 'x' and len(char_string) <= 1: #for x with coeffcient of 1
      if char_string.isdigit():
        string_list.append(char_string)
        char_string = ''
      elif char_string == '-':
        string_list.append('-1')
        char_string = ''
      else:
        string_list.append('1')
    else:
      string_list.append(char_string)
      char_string = ''
      
  numlist = []    
  for item in string_list:
    if item not in '':
      numlist.append(int(item))
  
  return numlist
  
# Needs Testing
def trinomials_a(factors:tuple) -> str:
  """ Displays a trinomial for a user to factor where 
  a = 1 in ax^2+bx+c.
  >>> from fakeinput import FakeInput
  >>> with FakeInput("-5 4"): trinomials_a((-5,4))
  <BLANKLINE>
                        x^2-1x-20                      
  <BLANKLINE>
  Factor the following in the form (x+y)(x+z).     
  Enter the values for y and z using ONLY ONE space     
  to separate your solutions: 
  You are correct!
  >>> with FakeInput('4 7'): trinomials_a((-7,3))
  Incorrect
  """

  y,z = factors
  longest_line = "Enter the values for 'y' and 'z' using ONLY ONE space"
  
  print()
  print(f"{get_trinomial_a(y,z):^{len(longest_line)}}")
  print()
  print("Factor the following in the form (x+y)(x+z). \
    \nEnter the values for y and z using ONLY ONE space \
    \nto separate your solutions: ")
  sol_a, sol_b = get_user_input_a()
  
  
  while sol_a + sol_b != y + z or sol_a * sol_b != y*z:
    if (sol_a + sol_b == -1 * (y+z)):
      print(f"CLOSE! Does adding {sol_a} and {sol_b} give you the result of {y+z}?")
    elif (sol_a * sol_b == y*z) and (sol_b + sol_a != y+z):
      print(f"Check your addition {sol_a} + {sol_b}")
    elif (sol_a + sol_b == y+z) and (sol_b * sol_a != y*z):
      print(f"Check your multiplication ({sol_a} times {sol_b})")
    elif sol_a * sol_b == y+z:
      print("Are you multiplying to the correct number?")
    elif sol_a + sol_b == y*z:
      print("Are you adding to the correct number?")
    else:
      print("Try again!")
    sol_a, sol_b = get_user_input_a()
  
  return print("You are correct!")


# Needs Testing
def trinomials_b():
  """ Displays a trinomial for a user to factor in the form ax^2+bx+c where a=1.
  """

  y,z = get_two_factors()

  longest_line = "Factor the trinomial in the form (x+y)(x+z)."
  
  print()
  print(f"{get_trinomial_a(y,z):^{len(longest_line)}}")
  print()
  print("Factor the trinomial in the form (x+y)(x+z).")

  user_entry = extract_ints_b(input())
  attempts = 1

  while len(user_entry) != 2:
    attempts += 1
    print("Invalid entry. Try again!")
    user_entry = (extract_ints_b(input()))
  a,b = user_entry

  while len(user_entry) != 2 or get_trinomial_a(a,b) != get_trinomial_a(y,z):
    attempts += 1
    print("Try again!")
    user_entry = extract_ints_b(input())
    if len(user_entry) == 2:
      a,b = user_entry
    else:
      print("Invalid Entry. Try again!")
      user_entry = extract_ints_b(input())
      
  if attempts !=1:
    word = "attempts"
  else:
    word = "attempt"
  
  return print(f"You are correct! You answered it in {attempts} {word}.")


# Needs Testing
def trinomials_c():
  """Displays a trinomial for a user to factor in the form ax^2+bx+c where a>1.
  """

  string = "Factor the trinomial in the form (ax+b)(cx+d)."
  text_length = len(string)
  a,b,c,d = get_four_integers()
  
  print(f"{get_trinomial_c(a,b,c,d):^{text_length}}")
  print() #Blank Line
  print("Factor the trinomial in the form (ax+b)(cx+d).")

  user_entry = tuple(extract_ints_c(input()))
  attempts = 1
  
  while len(user_entry) != 4:
    attempts += 1
    print("Invalid entry. Try again!")
    user_entry = (extract_ints_c(input()))
  f,g,h,i = user_entry

  while len(user_entry) != 4 or get_trinomial_c(a,b,c,d) != get_trinomial_c(f,g,h,i):
    attempts += 1
    print("Try again!")
    user_entry = (extract_ints_c(input()))
    if len(user_entry) == 4:
      f,g,h,i = user_entry
    else:
      print("Invalid Entry. Try again!")
      user_entry = (extract_ints_c(input()))

  if attempts !=1:
    word = "attempts"
  else:
    word = "attempt"
  return print(f"You are correct! You answered it in {attempts} {word}.")
      
  
if __name__ == "__main__":
  import doctest
  doctest.testmod()

  user_entry = input("Which level would you like to practice in (a, b or c)? ")
  levels = "abcABC"
  
  while user_entry not in levels:
    print("Invalid_entry type letter a, b, or c: ")
    user_entry = input()
  
  if user_entry in "Aa":
    trinomials_a(get_two_factors())
  elif user_entry in "Bb":
    trinomials_b()
  else:
    trinomials_c()
