def excel_index(theIndex):
    ans = 0
    length = len(theIndex)
    for x in theIndex:
        length = length - 1
        ans += (ord(x) - 64) * (26**length)
    return ans