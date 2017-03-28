'''Created on Mar 6, 2013
animal class represents animal data object
@author: rduval
'''
class Animal:
    def __init__(self, id, name, family, weight):
        self.id = id
        self.name = name
        self.family = family
        self.weight = weight

    def __repr__(self):
        return "Animal({0}, '{1}','{2}','{3}".format(self.id, self.name, self.family, self.weight)
        return ""
    
if __name__ == "__main__":
    import mysql.connector
    from database import login_info
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()    
    cursor.execute("select id, name, family, weight from animal")
    animals = [Animal(*row) for row in cursor.fetchall()]
    from pprint import pprint
    pprint(animals)
