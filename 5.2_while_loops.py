"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answer to "Do you want to continue? (yes/no)", typed up to 5 times.
# 2. Process: the loop cleans the answer with strip() and lower(), checks if it is yes or no, and counts the attempts.
# 3. Out: a message after each answer, then a summary showing how many attempts were used.
# 4. My stop condition, my attempt limit, my summary: the loop stops when the user answers yes or no (capitals and extra spaces are accepted because of strip() and lower()). The limit is 5 attempts, then the program stops with a message. The summary shows how many attempts were used.


# Your code below

from ast import While

i=0
while i < 5:
    print("attempt number:", i+1)
    i = i+1

while True :
    answer = input("Do you want to continue? (yes/no): ")
    if answer.strip().lower() == "yes":
        print("You chose to continue.")
        break
    elif answer.strip().lower() == "no":
        print("You chose to stop.")
        break
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")