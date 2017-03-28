'''
Created on Mar 8, 2013

@author: rduvalwa2
#!/usr/local/bin/python3
THIS one is working  dict_study_class.py
'''

class print_chart:
        def __init__(self, dictInput):
            self.dictIn = dictInput

dictIn = {1: 16, 2: 267, 3: 267, 4: 169, 5: 140, 6: 112, 7: 99, 8: 68, 9: 61, 10: 56, 11: 35, 12: 13, 13: 9, 14: 7, 15: 2}
# returns the hightest value from the dict
def get_max(dic):
    max = 0
    for ke in dic.keys():
        if dic[ke] > max:
                max = dic[ke]
    max = round(max / 100) * 100
    return max

# caluclate number of rows
def get_num_rows(max_val, row_val):
        return round(max_val / row_val)
         
# set value of each row this could be done by passing an argument
row_val = 10

# max_value is the highest value in the dict.  this is used to calcuation the number of rows to print
max_val = get_max(dictIn)

# get the number of rows
row_count = get_num_rows(max_val, row_val)

# number of columns
col_count = len(dictIn)

# store the printable row strings 
rows = {}
# Store the string for a column
columns = []
for r in range(1, row_count + 1):
        for col in range(1, col_count + 1):
            if dictIn[col] > row_val:
                    columns.append('***')
            else:
                columns.append('   ')
        row_val += 10
        rows[r] = "".join(columns)
        columns = []    

# label_row is used to determine when to apply a label
label_row = 1

# print the chart rows
for row in range(1, len(rows) + 1):
    label = row_val - 10
    if label_row == row:
            if len(str(label)) < 3:
#                print(" {0}-|{1}".format(label,rows[c - row]))     
                print(" {0}-|{1}".format(label, rows[(len(rows) + 1) - row]))     
            else:    
                print("{0}-|{1}".format(label, rows[(len(rows) + 1) - row]))     
            row_val = row_val - 10
            label_row = label_row + 5
    else:
            print("{0}-|{1}".format("   ", rows[(len(rows) + 1) - row]))     
            row_val = row_val - 10

# create the chart base line
base_line = ['  0 ']
for item in range(1, len(dictIn) + 1):
            base_line.append('-+-')

# print the chart base line
print(''.join(base_line))

# create the chart base labels
base_labels = ['    ']
for itm in dictIn.keys():
        if itm < 10:
            base_labels.append('  {0}'.format(itm))
        if itm > 9:
            base_labels.append(' {0}'.format(itm))

# print chart base labels
print(''.join(base_labels))

