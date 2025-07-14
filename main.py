import random
'''
Converting to Python because Go sucks
'''

# Alice announces these, Eve intercepts them before passing them to Bob.
p = 1000000007
alpha = 5

# Alice and Bob choose SA and SB respectively (secret, never transmitted)
SA = random.randint(10000)
print("Alice's secret is: " + SA)
SB = random.randint(10000)
print("Bob's secret is: " + SB)

# Alice and Bob caluclate TA and TB respecitvely based on alpha, p, and their secret number.
TA = alpha^SA%p
print("TA calculated by Alice is: " + TA)
TB = alpha^SB%p
print("TB calculated by Bob is: " + TB)
# These values TA and TB are sent to each other (and pass through Eve first, who can manipulate them)

# Alice calculates the shared key.
KeyA = TB^SA%p
print("Alice calculates the shared key to be: " + KeyA)
# Bob does the same on his end. These steps aren't visible to Eve.
keyB = TA^SB%p
print("Bob calculates the shared key to be: " + KeyB)