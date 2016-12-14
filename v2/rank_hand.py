def rank_hand(hand):
    rank = 0
    straight = False
    flush = False
    combo = [(card[0:-1], card[-1]) for card in hand]
    nrs = sorted([1 if n == "A" else 10 if n == "T" else 11 if n == "J" else 12 if n == "Q" else 13 if n == "K" else int(n) for n, y in combo])
    nrsAce = sorted([14 if n == 1 else n for n in nrs])
    suits = [y for x, y in combo]
    countDups = len([x for x in nrs if nrs.count(x) >= 2])
    if countDups >= 2: #1 pair
        rank = 1
    if countDups >= 4: #2 pair
        rank = 2
    if countDups == 3: #3 of a kind
        rank = 3
    if countDups == 4 and len(set(nrs)) <= 2: #4 of a kind
        rank = 7
    if len(set(nrs)) == 5:  #Straight
        if (max(nrs) - min(nrs) == 4) or (max(nrsAce) - min(nrsAce)) == 4:
            rank = 4
            straight = True
    if len(set(suits)) == 1: #Flush
        rank = 5
        flush = True
    if flush and straight:
        rank = 8
    if len(set(nrs)) == 2 and len([x for x in nrs if nrs.count(x) >= 2]) == 5: #Full house 33311
        rank = 6
    if flush and straight and min(nrsAce) == 10:
        rank = 9
    return rank

x = rank_hand(["2H", "3H", "4H", "JH", "KH"])
print(x)