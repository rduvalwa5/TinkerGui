'''
Created on Mar 8, 2013
extract values  from dict
@author: rduvalwa2
'''

def sort_by_value(dict_in):
    dict_in = dict_in
    values = []

    def print_length_count(dict):
            print(" Length Count")
            for length in sorted(dict.keys()):
                print(" {0} {1}".format(length , dict[length]))
    
    def sort_by_count(dict):
        for length in dict.keys():
            values.append(dict[length])
        sorted_values = sorted(values, reverse=True)    
        print(sorted_values)
        return(sorted_values)

if __name__ == "__main__":
    dict = {1: 16, 2: 267, 3: 267, 4: 169, 5: 140, 6: 112, 7: 99, 8: 68, 9: 61, 10: 56, 11: 35, 12: 13, 13: 9, 14: 7, 15: 2}
    sort_by_value.sort_by_count(dict)        
        
