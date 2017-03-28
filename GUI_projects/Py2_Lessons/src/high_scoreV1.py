import shelve

def high_score(player, score):
    names = []
    dataBase = 'scores'
    shelf = shelve.open(dataBase)

    for name in shelf.items():
        names.append(name[1][0])
    if names.__contains__(player):
        for pl in shelf.items():
            if pl[1][0] == player:
                if int(pl[1][1]) < score:
                    shelf[pl[0]] = (pl[1][0], score)
                    return shelf[pl[0]][1]
                else:
                    return shelf[pl[0]][1]
    else:
        shelf[player] = (player, score)
        return shelf[player][1]
