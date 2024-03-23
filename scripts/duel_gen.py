#!/usr/bin/env python

import psycopg2
import os
import random
import time
from datetime import datetime as dt

DB_NAME="ogre"
DB_USER="postgres"
DB_HOST="psql-1.c1so8qiqiw95.us-east-2.rds.amazonaws.com"
DB_PASSWD=os.environ['DB_PASSWD']

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s" % (DB_NAME, DB_USER, DB_PASSWD, DB_HOST))

# INSERT INTO Duels(winnerCharacterID, loserCharacterID) VALUES
#   ('<winnerCharacterID>', <loserCharacterID>),
#   ...,
#   ('<winnerCharacterID>', <loserCharacterID>);

MAX_DUELS=800

cur = conn.cursor()
cur.execute("SELECT id FROM Accounts")
account_ids = cur.fetchall()

with open("duels.sql", 'w') as f:
    f.write("INSERT INTO Duels(timestamp, winnerCharacterID, loserCharacterID) VALUES\n")

    duel_count = 0
    while duel_count < MAX_DUELS:
        winner = random.choice(account_ids)[0]
        loser = random.choice(account_ids)[0]
        while loser == winner:
            loser = random.choice(account_ids)[0]
        f.write("\t('%s', %d, %d),\n" % (dt.fromtimestamp(time.time()-duel_count).strftime('%Y-%m-%d %H:%M:%S'), random.choice(account_ids)[0], random.choice(account_ids)[0]))
        duel_count += 1
