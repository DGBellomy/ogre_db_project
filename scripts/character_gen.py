#!/usr/bin/env python

import psycopg2
import os
import random

DB_NAME="ogre"
DB_USER="postgres"
DB_HOST="psql-1.c1so8qiqiw95.us-east-2.rds.amazonaws.com"
DB_PASSWD=os.environ['DB_PASSWD']

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s" % (DB_NAME, DB_USER, DB_PASSWD, DB_HOST))

# INSERT INTO Characters(name, accountID) VALUES
#   ('<name>', <accountID>),
#   ...,
#   ('<name>', <accountID>);

MAX_COUNT=8000

names = ['bob', 'steve', 'dan', 'gord', 'eve', 'crusher', 'korg', 'dansk']

name_mods = ['builder', 'crusher', 'herder', 'goat', 'unicorn', 'frogleg', 'peanut', 'destroyer']

cur = conn.cursor()
cur.execute("SELECT id FROM Accounts")
account_ids = cur.fetchall()

cur.execute("SELECT name FROM Classes")
classes = cur.fetchall()

characternames = set()
for i in range(MAX_COUNT):
    digits=''
    for i in range(4):
        digits += str(random.choice(range(1,100)))

    characternames.add("%s the %s - %s" % (random.choice(names), random.choice(name_mods), digits))


print("produced %d unique characters" % len(characternames))

with open("characters.sql", 'w') as f:
    f.write("INSERT INTO Characters(name, accountID, className) VALUES\n")
    for name in characternames: 
        f.write("\t('%s', %d, '%s'),\n" % (name, random.choice(account_ids)[0], random.choice(classes)[0]))
