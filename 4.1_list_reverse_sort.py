"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the list of numbers I built in exercise 4.0.
# 2. Process: the program puts the list in four different orders, always working on a new list or a copy, so the original is never changed
# 3. Out:  the list in four orders, then the original list at the end to prove it has not moved.
# 4. My four orders, and which ones modify the original:
#    - Smallest to largest with sorted(): returns a new list, the original is untouched.
#    - Largest to smallest with .sort(reverse=True): modifies the list in place, so I used it on a copy.
#    - Last to first with [::-1]: slicing returns a new list, the original is untouched.
#    - Random order with random.shuffle(): modifies the list in place, so I used it on a copy.




# Your code below
# Your code below
import random

numbers = [4, 5, 6, 7, 8, 9, 10, 11, 2, 1]
backup = numbers.copy()

print("Original:", numbers)

# 1. sorted() gives back a NEW list
smallest_first = sorted(numbers)
print("Smallest to largest:", smallest_first)

# 2. .sort() changes the list itself, so I sort a copy
largest_first = numbers.copy()
largest_first.sort(reverse=True)
print("Largest to smallest:", largest_first)

# 3. [::-1] gives back a NEW list
last_to_first = numbers[::-1]
print("Last to first:", last_to_first)

# 4. random.shuffle() changes the list itself, so I shuffle a copy
shuffled = numbers.copy()
random.shuffle(shuffled)
print("Random order:", shuffled)

# Proof the original was not damaged
print("Original unchanged?", numbers == backup)
print("Original at the end:", numbers)