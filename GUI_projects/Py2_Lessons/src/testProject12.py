'''
Created on Mar 21, 2013

@author: rduvalwa2
'''
import os
import unittest
import datetime
from lesson_12_project import createMessage 

class emailTest(unittest.TestCase):
    
    def setUp(self):
        path = "./"
        self.toAddress = 'ToAny@there.com'
        self.message = "Hi,\n   This is a test message.\nThe Sender"
        self.files = [os.path.join(path, 'Xplain_text.txt'), os.path.join(path, 'plain_text.txt'), os.path.join(path, 'foot.png'), os.path.join(path, 'TestHelloWorld.html'), os.path.join(path, 'feet.bmp')]  # ,'HerMajesty.mp3']
        
    def testMessageNoList(self):
        msg = createMessage(self.toAddress, self.message)
        self.assertEqual(msg['To'], self.toAddress)
        self.assertEqual(msg.get_payload(), self.message)
        self.assertEqual(msg['Date'], datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600"))
        self.assertEqual(msg['From'], 'anybody@home.com')
        self.assertEqual(msg['Subject'], "Text Type Email")
        self.assertEqual(msg.get_content_type(), 'text/plain')
        self.assertFalse(msg.is_multipart()) 
        print(msg)       
    
    def testMessageList(self):
        msg = createMessage(self.toAddress, self.message, self.files)
        self.assertEqual(msg['To'], self.toAddress)
        self.assertEqual(msg['From'], 'anybody@home.com')
        self.assertEqual(msg['Subject'], "MIME Type Email")
        self.assertTrue(msg.is_multipart())
        expectedCount = len(self.files)  # do not add one for the text message not a file one file fails to load
        actualCount = 0
        for m in msg.get_payload():
            actualCount += 1
        self.assertEqual(expectedCount, actualCount) 
        
if __name__ == "__main__":
    unittest.main()
