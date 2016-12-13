def flatten(args):
    sortedList = sorted(args)
    ans = []
    for x in args:
        index = sortedList.index(x)
        ans.append(index)
    return ans