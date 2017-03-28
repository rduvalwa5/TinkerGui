'''
Created on Oct 20, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""
high_score.py
function that keeps players high scores in a shelve persistence
"""

import high_score
import unittest
import os
import shelve


global database
dataBase = 'scores'

class test_high_score(unittest.TestCase):
    
    def setUp(self):
        
        shelf = shelve.open(dataBase)
        joe = 21
        sam = 24
        jim = 30
        shelf['joe'] = joe
        shelf['sam'] = sam
        shelf['jim'] = jim
        shelf.close()

    def test_no_change_same(self):
        score = 21
        expected = 21 
        player = 'joe'
        observed = high_score.high_score(player, score)
        self.assertEqual(observed, expected)
        
    def test_change_less(self):
        score = 29 
        expected = 30
        player = 'jim'
        observed = high_score.high_score(player, score)
        self.assertEqual(observed, expected)
     
    def test_new_high_score(self):
        score = 27
        expected = 27 
        player = 'sam'
        observed = high_score.high_score(player, score)
        self.assertEqual(observed, expected)

    def test_new_player_score(self):
        score = 12 
        expected = 12
        player = 'chuck'
        observed = high_score.high_score(player, score)
        self.assertEqual(observed, expected)
    
    def tearDown(self):
            os.remove(dataBase + '.db')

if __name__ == "__main__":
    unittest.main()            
