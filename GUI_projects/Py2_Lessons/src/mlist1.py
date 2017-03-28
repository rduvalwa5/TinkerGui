'''
Created on Apr 3, 2013

@author: rduval
'''
from database import login_info
import mysql.connector
from email import message_from_string
conn = mysql.connector.Connect(**login_info)
curs = conn.cursor()
curs.execute("select msgText from message order by msgDate")
for text, in curs.fetchall():
    msg = message_from_string(text)
    print(msg['date'], msg['subject'])

