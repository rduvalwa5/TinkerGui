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
import glob

global database
dataBase = 'scores'

class test_high_score(unittest.TestCase):
        
    def test_new_player_score(self):
        score = 12 
        expected = 12
        player = 'joe'
        observed = high_score.high_score(player,score)
        self.assertEqual(observed,expected)

    def test_no_change_same(self):
        old_score = 12
        score = 12
        expected = 12 
        player = 'joe'
        high_score.high_score(player,old_score)
        high_score.high_score(player,score)
        observed = high_score.high_score(player,0)
        self.assertEqual(observed,expected)
        
    def test_change_less(self):
        old_score = 12
        score = 11
        expected = 12 
        player = 'joe'
        high_score.high_score(player,old_score)        
        high_score.high_score(player,score)
        observed = high_score.high_score(player,0)
        self.assertEqual(observed,expected)
     
    def test_new_high_score(self):
        old_score = 12
        score = 21
        expected = 21 
        player = 'joe'
        high_score.high_score(player,old_score)        
        high_score.high_score(player,score)
        observed = high_score.high_score(player,0)
        self.assertEqual(observed,expected)
    
    def tearDown(self):
            files = glob.glob("scores.*")
            for fn in files:
                os.remove(fn)

if __name__ == "__main__":
    unittest.main()            