#!/usr/bin/env python3

import random
import os

# Generate a file with thousands of Accounts
# INSERT INTO Accounts(username) VALUES
#   ('<username>'),
#   ...,
#   ('<username>);

# usernames will consist of names with a string of 8 random numbers
NAMES = ['tommy', 'betty', 'george', 'kraig', 'bob', 'phil', 'steve', 'lara', 'sarah',
            'jen', 'billy', 'beorn', 'heather', 'hugo', 'hans']

NUM_USERS=5000

usernames = set()
for i in range(NUM_USERS):
    digits=''
    for i in range(4):
        digits += str(random.choice(range(1,100)))

    usernames.add("%s%s" % (random.choice(NAMES), digits))


print("produced %d unique usernames" % len(usernames))

with open("accounts.sql", 'w') as f:
    f.write("INSERT INTO Accounts(username) VALUES\n")
    for username in usernames: 
        f.write("\t('%s'),\n" % username)
