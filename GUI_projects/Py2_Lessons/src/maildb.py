"""
Email message handling module: contains logic to store and retrieve
email messages using a MySQL relational database.
"""
from database import login_info
import mysql.connector as msc
from email import message_from_string
from email.utils import parsedate_tz, mktime_tz, parseaddr
from datetime import datetime, timedelta

conn = msc.Connect(**login_info)
curs = conn.cursor()

def store(msg):
    """
    Stores an email message, if necessary, returning its primary key.
    """ 
    message_id = msg['message-id']
#    text = msg.as_string()
    curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if result:
        return result[0]
    date = msg['date']
    name, email = parseaddr(msg['from'])
    dt = datetime.fromtimestamp(mktime_tz(parsedate_tz(date)))
    text = msg.as_string()
    curs.execute("INSERT INTO message (msgMessageID, msgDate,msgSenderName,msgSenderAddress,msgText) VALUES (%s, %s, %s,%s,%s)",
             (message_id, dt,name,email, text))
    conn.commit()
    curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
    return curs.fetchone()[0]

# def msgs_by_date(mindate=None, maxdate=None):
def msgs(mindate=None,maxdate=None, namesearch=None, addsearch=None):
    """
    Return a list of all messages sent on or after mindate and on or before maxdate.
    If mindate is not specified, there is no lower bound on the date, and similarly
    if maxdate is not specified, no upper bound. If namesearch is given, the
    result set is restricted to messages with sender names containing that string. If
    addsearch is given, the result set is restricted to messages with email
    addresses containing that string.
    """ 
#    if not (mindate or maxdate):
#        raise TypeError("Must provide at leastone of mindate, maxdate")
    conds = []
    data = []
    if mindate:
        conds.append("msgDate >= %s")
        data.append(mindate)
    if maxdate:
        conds.append("msgdate < %s")
        data.append(maxdate+timedelta(days=1))
    if namesearch:
        conds.append("msgSenderName like %s")
        data.append("%" + namesearch.strip().lower() + "%s")
    if addsearch:
        conds.append("msgSenderAddress like %s")
        data.append("%s" + addsearch.string().lower() + "%s")
#    sql = "select msgid, msgText from message where "
#    sql += "and ".join(conds)
    sql = "select msgid, msgText from message"
    if conds:
        sql += " where " + "and ".join(conds)
    curs.execute(sql, tuple(data))
    result = []
    for id, text in curs.fetchall():
        result.append((id, message_from_string(text)))
    return result

def msg_by_id(id):
    """
    Return the (presumably singleton) message whose primary key is given
    or raise KeyError if no such message exists.
    """
    curs.execute("SELECT msgID, msgText FROM message WHERE msgID=%s", (id, ))
    result = curs.fetchone()
    if  not result:
        raise KeyError("Id {0} not found in store".format(id))
    id, text = result
    msg = message_from_string(text)
    return id, msg

def msg_by_message_id(message_id):
    """
    Return the (presumably singleton) message whose "Message-ID" is given
    or raise KeyError if no such message exists.
    """
    curs.execute("SELECT msgID, msgText FROM message WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if  not result:
        raise KeyError("Message-Id {0} not found in store".format(message_id))
    id, text = result
    msg = message_from_string(text)
    return id, msg

