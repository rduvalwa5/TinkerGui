'''
Created on Mar 18, 2013
Create the user table and add all necessary data.
'''

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

cursor.execute("""DROP TABLE IF EXISTS user""")
cursor.execute("""
    CREATE TABLE user (
        ID INTEGER ,
        NAME VARCHAR(50),
        EMAIL VARCHAR(50))
    """)

data = [('1', 'Steve Holden', 'steve@holden.com'),
        ('2', 'Steve Badly', 'steve@badly.com'),
        ('3', 'Jon Badly', 'jon@badly.com'),
        ('4', 'Bob Bob', 'bob@bob.com')]

for id, name, email in data:
    cursor.execute("""INSERT INTO user (id, name, email)
                        VALUES (%s, %s, %s)""", (id, name, email))
    db.commit()
