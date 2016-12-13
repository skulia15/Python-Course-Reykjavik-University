def insert_operators(seq, target):
    import itertools as it
    import math
    countOps = len(seq) - 1
    availableOps = "+-C"
    perms = it.product(availableOps, repeat=countOps)
    perms =  [''.join(p) for p in perms]
    ans = []
    for per in perms:
        s = ""
        for x in range(countOps):
            s += str(seq[x])
            if per[x]!= "C":
                s += per[x]
        s += str(seq[-1])
        ans.append(s)
    for x in ans:
        if eval(x) == target:
            return(x + "=" + str(target))
    return None