'''
Created on Mar 14, 2013
Here are your instructions:
1) Modify the classFactory.py source code so that the 
2) DataRow class returned by the build_row function has another method:
   -  retrieve(self, curs, condition=None)
3) self is (as usual) the instance whose method is being called
   = curs is a database cursor on an existing database connection, 
   - condition (if present) is a string of condition(s) which must be true of all received rows.
4) retrieve method should be a generator, 
   yielding successive rows of the result set until it is completely exhausted. 
5) Each row should be a new object of type DataRow.

Test Data Base
mysql> select * from user;
+------+--------------+------------------+
| id   | name         | email            |
+------+--------------+------------------+
|    1 | Steve Holden | steve@holden.com |        

|    2 | Steve Badly  | steve@badly.com  |
|    3 | Jon Badly    | jon@badly.com    |
|    4 | Bob Bob      | bod@bod.com      |
+------+--------------+------------------+
4 rows in set (0.00 sec)
@author: rduvalwa2
'''
import types
import mysql.connector
import create_user
from database import login_info
import unittest
from lesson_11_project import build_row

class DBTest(unittest.TestCase):

    def setUp(self):
        create_user
        C = build_row("user", "id name email")
        self.c = C([1, "Stevie Holden", "steve@holdenweb.com"])

    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Stevie Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")

    def test_repr(self):
        repr(self.c)
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Stevie Holden', 'steve@holdenweb.com')")

    def test_retrieve_2records(self):
        D = build_row("user", "id name email")
        d = D([1, 'Any One', 'one@one.com'])
        db = mysql.connector.Connect(**login_info)
        condition = "name like 'Steve%'"
        records = d.retrieve(db.cursor(), condition)
        self.assertIsInstance(records, types.GeneratorType, "Not Generator")
        for record in records:
            self.assertEqual(record.name[0:5], "Steve")

    def test_retrieve_1record(self):
        D = build_row("user", "id name email")
        d = D([1, 'Any One', 'one@one.com'])
        db = mysql.connector.Connect(**login_info)
        condition = "id='2'"
        records = d.retrieve(db.cursor(), condition)
        self.assertIsInstance(records, types.GeneratorType, "Not Generator")
        for record in records:
            self.assertEqual(record.id, 2)

    def test_retrieve_no_conditions(self):
        D = build_row("user", "id name email")
        d = D([1, 'Any One', 'one@one.com'])
        db = mysql.connector.Connect(**login_info)
        records = d.retrieve(db.cursor())
        self.assertIsInstance(records, types.GeneratorType, "Not Generator")
        expect_Count = 4
        rec_count = 0
        for r in records:
            rec_count += 1
        self.assertEqual(expect_Count, rec_count)
        
if __name__ == "__main__":
    unittest.main()

