#/usr/bin/env python3

import psycopg2
import os

DB_NAME="ogre_test"
DB_USER="postgres"
DB_HOST="psql-1.c1so8qiqiw95.us-east-2.rds.amazonaws.com"
DB_PASSWD=os.environ['DB_PASSWD']

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s" % (DB_NAME, DB_USER, DB_PASSWD, DB_HOST))
#cur = conn.cursor()
#cur.execute("select * from Characters")
#records = cur.fetchall()
#print(records)
