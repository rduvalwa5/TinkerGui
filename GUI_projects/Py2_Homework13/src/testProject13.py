'''
Created on May 1, 2013
Use test-driven development, and state the purpose of each test in the suite in 
docstrings that will eventually document your program.
@author: rduvalwa2
'''

import settings
import mysql.connector
from database import login_info
from datetime import timedelta
from datetime import datetime
import unittest
import create_text_email_Prj13


db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

class DBTest(unittest.TestCase):
    
    def setUp(self):
        """
        Set up allows this code to be run anytime and produce an output
        by changing the STARTTIME to the current date
        """
        today = datetime.now()
        YR = int(today.strftime('%Y'))
        DY = int(today.strftime('%d'))
        MNTH = int(today.strftime('%m'))
        settings.STARTTIME = datetime(YR, MNTH, DY)
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
 
        c = create_text_email_Prj13
        c. createDailyMessage()
        db.commit()
    def test_total_stored_emails(self):
        """
        Test that the total number of emails stored in the data base is the correct number of records.
        For each day there should be one email for each recipient.
        This is accomplished by comparing the length of the settings RECIPIENTS tuple (after conversion to a list) 
        and multiplying this by the total settings DAYCOUNT.
        This result is compared to the total number of records stored in the daily_email table.
        """
        expected = settings.DAYCOUNT * len(settings.RECIPIENTS)
        cursor.execute("select count(*) from daily_email")
        actual = cursor.fetchone()[0]
        self.assertEqual(actual, expected)    

    def test_one_recipient_stored_emails(self):
        """
        This test veifies that a sample email recipient has the correct number of email records stored in daily_email table.
        Each recipeint should have one record for each count in DAYCOUNT.
        """
        recipientList = list(settings.RECIPIENTS)
        expected = settings.DAYCOUNT
        statement = "select count(*) from daily_email where msgRecipientAddress like '" + recipientList[0][1] + "';"
        cursor.execute(statement)
        actual = cursor.fetchone()[0]
        self.assertEqual(actual, expected)  
    
    def test_first_send_date(self):
        """
        This test verifies that the data stored in daily_email table starts on the expected date.
        """
        expected = settings.STARTTIME
        statement = "select min(msgSendDate) from daily_email"
        cursor.execute(statement)
        actual = cursor.fetchone()[0]
        self.assertEqual(expected, actual, "First date is wrong")

    def test_last_send_date(self):
        """
        This test verifies that the data stored in daily_email table ends on the expected date.
        """
        expected = settings.STARTTIME + timedelta(days=settings.DAYCOUNT - 1)
        statement = "select max(msgSendDate) from daily_email"
        cursor.execute(statement)
        actual = cursor.fetchone()[0]
        self.assertEqual(expected, actual, "Last date is wrong")
        
    def test_sent_emails(self):
        """
        This test verifies that for the current date the number of email messages sent is equal to 
        the number of email recipients expecting an email.
        """
        c = create_text_email_Prj13
        emailMessages = c.createDailyMail()
        for email in emailMessages:
            print(email)
        emailRecipients = []     
        for message in emailMessages:
            if not emailRecipients.__contains__(message.get('To')):
                emailRecipients.append(message.get('To'))
        self.assertEqual(len(emailRecipients), len(settings.RECIPIENTS))   

if __name__ == "__main__":
    unittest.main()



