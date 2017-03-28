'''
Created on Mar 20, 2013
Here are your instructions:
 1. Write a function that takes:
    - an email address,
    - a string,
    - and a list argument.
 2. It should return an email message 
    - addressed to the email address passed as the first argument,
    - with the second argument as the message body
 3. If the list is non-empty, 
    - then each list item should be treated as
      1. the name of a file
      2. and the corresponding file should be attached (with an appropriate MIME type) to the message.
 4. Include any files to attach in the same folder as your program.  
    There is no need to send it as an email with smtp
    - though you may wish to print it as a string as a part of testing
@author: rduvalwa2
'''
import os
import email
import datetime
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def createMessage (address, message, lst=None):
    if lst == None:
        msg = email.message_from_string(message)
        msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600") 
        msg['To'] = address
        msg['Subject'] = "Text Type Email"
        msg['From'] = 'anybody@home.com'
        
    else:
        msg = MIMEMultipart()
        msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600") 
        msg['To'] = address
        msg['Subject'] = "MIME Type Email"
        msg['From'] = 'anybody@home.com'
        text_msg = MIMEText(message, 'text')
        msg.attach(text_msg)
        for file in lst:
            if mimetypes.guess_type(file)[0].__contains__('text'):
                try:
                    file_msg = email.message_from_file(open(r'./{0}'.format(file)))
                    msg.attach(file_msg)
                except IOError:
                    print ("Error: cannot open {0}".format(file))
            if mimetypes.guess_type(file)[0].__contains__('image'):
                try:
                    with open(file, 'rb') as fp:
                        file_img = MIMEImage(fp.read())
                        msg.attach(file_img) 
                except IOError:
                    print ("Error: cannot open {0}".format(file))
    return msg

if __name__ == "__main__":
    
    toAddress = 'ToAny@there.com'
    message = "Hi,\n   This is a test message.\nThe Sender"
    path = "./"
    files = [os.path.join(path, 'plain_text.txt'), os.path.join(path, 'foot.png'), os.path.join(path, 'TestHelloWorld.html'), os.path.join(path, 'feet.bmp')]  # ,'HerMajesty.mp3']
        
    files = ['plain_text.txt', 'TestHelloWorld.html', 'foot.png']
    msg = createMessage(toAddress, message)
    print(msg.as_string())    
    msg2 = createMessage(toAddress, message, files)
#    print(msg2.as_string())
