'''
Created on Mar 6, 2013
Demonstrate access by index to data elements
@author: rduval
'''

import mysql.connector
from database import login_info
#
db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

fmt = "{0:10} {1:6} {2:10}"
print(fmt.format("Animal", "Weight", "Family"))
print("-"*28)
# cursor.execute("select * from animal")
# for animal in cursor.fetchall():
#    print(fmt.format(animal[1],animal[3],animal[2]))
cursor.execute("select name, weight, family from animal")
for name, weight, family in cursor.fetchall():
    print(fmt.format(name, weight, family))
