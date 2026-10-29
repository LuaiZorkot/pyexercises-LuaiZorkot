"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a whole number N typed by the user.
# 2. Process:he program goes through every number from 1 to N and checks whether it divides evenly by 2.
# 3. Out:one line per number saying whether it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
# -the programprints "0 is even", because 0 divides evenly by 2.
#- negative: the program counts down from -1 to N, so -4 gives -1, -2, -3, -4.
#- very large: anything above 100 is capped at 100, with a message telling the user (same for anything below -100).


# Your code below
MAX = 100
n = int(input("Enter a number: "))

# Cap very large (or very negative) numbers
if n > MAX:
    print(f"That's a lot of numbers, so I'll only go up to {MAX}.")
    n = MAX
elif n < -MAX:
    print(f"That's a lot of numbers, so I'll only go down to -{MAX}.")
    n = -MAX


# Decide which numbers to check
if n == 0:
    numbers = [0]
elif n > 0:
    numbers = range(1, n + 1)
else:
    numbers = range(-1, n - 1, -1)

for i in numbers:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
