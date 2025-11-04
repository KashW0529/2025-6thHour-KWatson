#Name: Kash
#Class: 5th Hour
#Assignment: HW12

import random
from numbers import Number

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 1:
    print(i)
    i -= 1
else:
    print('Hello World')

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

m = 1
while m <= 30:
    if m % 2 == 0:
        print(m)
    m += 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

e = 1
while e <= 30:
    if e % 3 == 0:
        e += 1
        continue
    print(e)
    e += 1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.

l = 1
while l >= 1:
    l = (random.randint(1, 6))
    print(l)
    if l == 1:
        break

#5. Create a while loop that asks for a number input until the user inputs the number 0.
p = 2
while p >= 1:
    p = int(input('Enter a number: '))
    if p > 0:
        print('Enter a Different Number')
        continue
    else:
        print('Good Job!')