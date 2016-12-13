def hangman(f, s, b):
    import re
    l = len(s)
    a = []
    with open(f, "r") as d:
        w = d.read().split('\n')
    k = [x for x in w if len(x) == len(s) and re.match("^[a-z]+$", x)]
    for x in k:
        if len([i for i in range(l) if x[i] == s[i] or s[i] == '-' and x[i] not in list(b)]) == l:
            a.append(x)
    return a

x = hangman("C:\\Users\\Skúli\\Desktop\\Python\\all_words.txt", "a--ri-a", "sogzp")
print(x)