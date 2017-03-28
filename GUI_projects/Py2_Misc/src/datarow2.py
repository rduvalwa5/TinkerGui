'''
Created on Mar 6, 2013
datarow.py : implements a simple database record class

the build_row function has another method:
retrieve(self, curs, condition=None)
self is (as usual) the instance whose method is being called, 
1) curs is a database cursor on an existing database connection, 
2) condition (if present) is a string of condition(s) which must be true of all received rows
3) retrieve method should be a generator, yielding successive rows of the result set until it is completely exhausted 
4) Each row should be a new object of type DataRow.

@author: rduval
'''

class row:
    def __init__(self, cols, data):
        self.__dict__.update(zip(cols, data))
    
    def __repr__(self):
        return "user_record(id={0.id} name={0.name} email={0.email})".format(self)   
    
    def retrieve(self, curs, condition=None):
        statement = "{0} {1} {2} {3};".format('select' , ", ".join(columns), ' from email ', condition)
        curs.execute(statement)
        return [self(*row) for row in curs.fetchall()]
         
if __name__ == "__main__":  # Simple self-test
    columns = ['id', 'name', 'email']
 #   r1 = row(['id', 'name', 'email']
    r1 = row(columns,
             (1, "Steve Holden", "steve@holdenweb.com"))
    if r1.id != 1 or r1.name != "Steve Holden" or r1.email != "steve@holdenweb.com":
        print("TEST FAILED: id={0.id} name={0.name} email={0.email}".format(r1))
    else:
        print("TEST passed: id={0.id} name={0.name} email={0.email}".format(r1))
        
    condition = "where name = 'Steve%'"    
#    statement = "{0} {1} {2} {3};".format('select' ,", ".join(columns),' from email ', condition)
#    print(statement)
