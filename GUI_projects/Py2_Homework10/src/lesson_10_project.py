'''
Created on Mar 5, 2013
Test each animal id is in the food table
@author: rduval
'''

import unittest
import mysql.connector
from database import login_info

class TestFood(unittest.TestCase):
    def test_animal_food_pass(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select id from animal where id not in (select anid from food)"
        cursor.execute(statement)
        row = cursor.fetchone()
        self.assertTrue(row == None)

if __name__ == "__main__":
    unittest.main()
