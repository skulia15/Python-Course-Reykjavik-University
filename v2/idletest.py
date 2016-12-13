def sort_names(names):
    import locale
    locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')
    print(names)
    names = list(names)
    nameList = []
    tmpList = []
    for x in names:
        p = x.split()
        nameList.append(p)
    print(nameList)
    nameList.sort(key=lambda x: (locale.strxfrm(x[0].lower()), locale.strxfrm(x[-1].lower()), locale.strxfrm(' '.join(x[1:-1]))))
    ans = []
    for x in nameList:
        ansStr = ""
        for y in x:
            if ansStr == "":
                ansStr = y
            else:
                ansStr = ansStr + " " + y
        ans.append(ansStr)
    return(ans)
