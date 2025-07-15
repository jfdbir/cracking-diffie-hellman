import random

# Alice announces these, Eve intercepts them before passing to Bob
p = 1000000007
alpha = 5

# Alice and Bob choose SA and SB respectively (secret, never transmitted)
SA = random.randint(0, 10000)
print(f"Alice's secret is: {SA}")
SB = random.randint(0, 10000)
print(f"Bob's secret is: {SB}")

# Alice and Bob calculate TA and TB respectively based on alpha, p, and their secret number
TA = pow(alpha, SA, p)
print(f"TA calculated by Alice is: {TA}")
TB = pow(alpha, SB, p)
print(f"TB calculated by Bob is: {TB}")
# These values TA and TB are sent to each other (and pass through Eve first, who can manipulate them)

# Alice calculates the shared key
KeyA = pow(TB, SA, p)
print(f"Alice calculates the shared key to be: {KeyA}")
# Bob does the same on his end. These steps aren't visible to Eve
KeyB = pow(TA, SB, p)
print(f"Bob calculates the shared key to be: {KeyB}")

KeysMatch = KeyA == KeyB
print(f"Do the keys match? {KeysMatch}")

''' 
WHAT WAS CHANGED
Removed extra quotes
Fixed spelling of "calculate" to "make" in comments.
Used easier f-strings to show text and numbers.
Made sure spacing was even.
Removed extra blank spaces at the end of lines.
Made comments shorter and easier to understand.
I hope this works; I probably didn't do anything (changed the format lol)
'''
