def scramble(theList, like):
    ans = []
    for x in like:
        ans.append(theList[x])
    return ans
#[100, 42, 4, 1337], [1,3,2,0])
#  0    1  2    3
#0 = 100
#1 = 42
#2 = 4
#3 = 1337
#result = [42, 1337, 4, 100]
#           1    3   2   0

    