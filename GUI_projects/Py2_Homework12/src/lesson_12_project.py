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
            if mimetypes.guess_type(file)[0] == 'text/plain' or mimetypes.guess_type(file)[0] == 'text/html':
                file_msg = email.message_from_file(open(r'{0}'.format(file)))
                msg.attach(file_msg)
            if mimetypes.guess_type(file)[0] == 'image/png' or mimetypes.guess_type(file)[0] == 'image/bmp':
                with open(file, 'rb') as fp:
                    file_img = MIMEImage(fp.read())
                msg.attach(file_img) 
    return msg

if __name__ == "__main__":
    import os
    import smtplib
    path = './'
    toAddress = 'rduvalwag@gmail.com'
    message = "Hi,\n   This is a test message.\nThe Sender"
    files = [os.path.join(path, 'plain_text_file.txt'), os.path.join(path, 'Hello_World.html'), os.path.join(path, 'python-logo.png')]
    msg = createMessage(toAddress, message)
    print("Sending Message 1")
    srv = smtplib.SMTP('mail.oreillyschool.com', 25)
    srv.sendmail(msg['From'], msg['To'], msg.as_string())
    srv.quit()   
    msg2 = createMessage(toAddress, message, files)
    print("Sending Message 2")
    srv = smtplib.SMTP('mail.oreillyschool.com', 25)
    srv.sendmail(msg2['From'], msg2['To'], msg2.as_string())
    srv.quit()
