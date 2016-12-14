#def sort_names(names):
import locale
names = ['Þórir Jakob Olgeirsson',
    'Arnar Björn Pálsson',
    'Eyþór Snær Tryggvason',
    'Arnar Jóhannsson',
    'Eyþór Traustason',
    'Arnar Bjarni Arnarson',
    'Þórhildur Þorleiksdóttir']
locale.setlocale(locale.LC_ALL, 'isl')
str = ""
print(names)
for x in names:
    print(x)
    str = str + ', '.join(x)
str = str.split(',')
#print(str)
nameList = []
for x in str:
    p = x.split()
    nameList.append(p)
nameList.sort(key=lambda x: (x[0].lower(), x[-1].lower()))
ans = []
for x in nameList:
    ansStr = ""
    for y in x:
        if ansStr == "":
            ansStr = y
        else:
            ansStr = ansStr + " " + y
    ans.append(ansStr)
print(ans)


nameList.sort(key=lambda x: (locale.strxfrm(x[0].lower()), locale.strxfrm(x[-1].lower()), locale.strxfrm(x[1].lower()) if (len(x) ==  3) else (locale.strxfrm(x[0].lower()), locale.strxfrm(x[-1].lower)))
ans = []