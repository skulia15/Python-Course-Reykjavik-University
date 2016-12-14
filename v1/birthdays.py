def birthdays(kts):
    ktString = ''.join(kts)
    ktList = ktString.split()
    sortedKts = sorted(ktList)
    ans = []
    for x in sortedKts:
        dups = []
        for y in sortedKts:
            if y[:4] == x[:4]:
                dups.append(y)
                dups.append(x)
        if len(dups) > 2:
            temp = sorted(dups)
            ans.append(tuple(set(temp)))
    return list(set(ans))

#kts = ['''0212862149
#0407792319
#0212849289
#1112792819
#0407992939
#0212970299''']
#ktString = ''.join(kts)
#ktList = ktString.split()
#sortedKts = sorted(ktList)
#ans = []
#for x in sortedKts:
#    dups = []
#    for y in sortedKts:
#        if y[:4] == x[:4]:
#            dups.append(y)
#            dups.append(x)
#    if(len(dups) > 2):
#        ans.append(tuple(set(dups)))
#print(set(ans))
