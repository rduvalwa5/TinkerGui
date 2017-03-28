'''
Created on Mar 7, 2013
classFactory.py function to return tailored classes
@author: rduval
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
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow
