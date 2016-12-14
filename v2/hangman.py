def hangman(file, state, banned):
    import re
    length = len(state)
    ans = []
    with open(file, "r") as data:
        w = data.read().split('\n')
    semi = [x for x in w if len(x) == len(state) and re.match("^[a-z]+$", x)]
    for x in semi:
        if len([i for i in range(length) if x[i] == state[i] or state[i] == '-' and x[i] not in list(banned)]) == length:
            ans.append(x)
    return ans

