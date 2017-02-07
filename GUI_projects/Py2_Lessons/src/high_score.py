import shelve

def high_score(player, score):
    dataBase = 'scores'
    shelf = shelve.open(dataBase)
    if player in shelf:
        if score > shelf[player]:
            shelf[player] = score
    else:
        shelf[player] = score
    highscore = shelf[player]
    shelf.close()
    return highscore
    
