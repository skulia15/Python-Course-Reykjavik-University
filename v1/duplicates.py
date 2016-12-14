def duplicates(args):
    dups = []
    count = 0
    for x in args:
        for y in args:
            if x == y:
                count += 1
                if count >= 2:
                    dups.append(x)
        count = 0
    return set(dups)