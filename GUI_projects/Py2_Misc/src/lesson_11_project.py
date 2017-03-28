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

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data) == len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)

        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))

        def retrieve(self, cursor, condition=None):
            conditions = [condition]
            if condition != None:
                statement = "SELECT {0} FROM {1} WHERE {2}".format(", ".join(self.cols), self.table, " AND ".join(conditions))
            if condition == None:
                statement = "SELECT {0} FROM {1}".format(", ".join(self.cols), self.table)
            cursor.execute(statement)
            result = cursor.fetchall()
            for rec in result:
                record = build_row(table, cols)
                ret = record(rec)
                yield ret
    
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow
