'''
Created on May 20, 2013
@author: rduvalwa2
'''
import smtplib
import email
import settings
import mysql.connector
from database import login_info
from datetime import timedelta
from datetime import datetime
from random import randint
# from email.utils import parsedate_tz, mktime_tz

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

def createDailyMessage():
    start = datetime.now()
    messageNumber = 1
    startDate = settings.STARTTIME
    for i in range(settings.DAYCOUNT):
        message = settings.MESSAGE + str(messageNumber)
        for recipient in settings.RECIPIENTS:
            msg = email.message_from_string("")
            msg['Date'] = startDate.strftime("%Y-%b-%d")  # (YR,MNTH,DY)
            msg['To'] = recipient[1]
            msg['Subject'] = "Message for the day"
            msg['From'] = 'anybody@home.com'
            msg['message-id'] = "<" + str(randint(100000, 900000)) + ">"
            msg['Message'] = message
            cursor.execute("INSERT INTO daily_email (messageId,msgRecipientAddress,msgFrom,msgSendDate,msgSubject,msgText) VALUES (%s,%s,%s,%s,%s,%s)", (msg['message-id'], msg['To'], msg['From'], startDate, msg['Subject'], msg['Message']))
        startDate += timedelta(days=1)
        messageNumber += 1
    db.commit()
    end = datetime.now()
    diffTime = end - start
    print("Data base Process time in microseconds ", (diffTime.microseconds))   
    messageNumber += 1

def createDailyMail():
    start = datetime.now()
    sentEmails = []
    fmt = '%Y-%m-%d'
    today = datetime.now()
    todayString = today.strftime(fmt)
    statement = "select messageId,msgRecipientAddress,msgFrom,msgSubject, msgText from daily_email where msgSendDate = '" + todayString + "';"
    cursor.execute(statement)
    result = cursor.fetchall()
    for rec in result:
        receiver = rec[1]
        sender = rec[2]
        subject = rec[3]
        text = rec[4]
        emailString = "To:" + receiver + "\n" + "From:" + sender + "\n" + "Subject:" + subject + "\n" + text + "\n"  
        theMsg = email.message_from_string(emailString)
        sentEmails.append(theMsg)
    end = datetime.now()
    diffTime = end - start
    print("Send Mail Process time in microseconds ", (diffTime.microseconds))   
    return sentEmails

def sendDailyMail(messages, server):
#    import smtplib
    srv = smtplib.SMTP(server, 25)
    for email in messages:
        print(email.as_string())

    for email in messages:
        try:
#            srv.sendmail(email.as_string())
            srv.sendmail(email['From'], email['To'], email.as_string())
            print(email)
            print ("Successfully sent email")
        except:
            print ("Error: unable to send email")
            print(email)
    srv.quit()

if __name__ == "__main__":
        server = 'mail.oreillyschool.com'
        cursor.execute("""DROP TABLE IF EXISTS daily_email""")
        cursor.execute("""
            CREATE TABLE daily_email (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            messageId VARCHAR(128),
            msgRecipientAddress VARCHAR(128),
            msgFrom VARCHAR(128),
            msgSendDate DATETIME,
            msgSubject VARCHAR(128),
            msgText LONGTEXT)
       """)
        
        createDailyMessage()
        myMessages = createDailyMail()
        try:
            sendDailyMail(myMessages, server)
        except IOError:
            print("Socket exception")
            print(IOError)
