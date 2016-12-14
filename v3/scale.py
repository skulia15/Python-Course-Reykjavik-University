import re
from fractions import Fraction
def scale(rec, scale):
    lis = rec.splitlines()
    noTabLis = []
    getFrac = []
    calcNums = []
    scale = Fraction(scale)
    for x in lis:
        noTabLis.append(re.sub(' ', '', x, 4))
    for x in noTabLis[2:]:
        if x == "":
            continue
        else:
            print(x)
            for i, letter in enumerate(x):
                if letter.isdigit() or letter == '/':
                    print(i, letter)
                    if not x[i + 2].isdigit():
                        getFrac.append(letter)
                        
            print("getFrac", getFrac)
        #print("Fraction we get: ",getFrac)
        if len(getFrac) == 0:
            continue
        first = ""
        for x in getFrac:
            if x.isdigit() or x == '/':
                first += x
            elif x == ' ':
                first += ' '
        print("Fraction read: ", first)
        first = first.split(' ')
        frac = Fraction(0)
        #print(first)
        for y in first:
            frac += Fraction(y)
        frac = Fraction(frac) * scale
        getFrac.clear()
        print("frac", frac)
        num = frac.numerator
        denom = frac.denominator
        p = ""
        if (num // denom) > 0:
            whole = num // denom
            p = str(whole)
            if int(whole) > 0:
                if Fraction(num - (whole * denom), denom) != 0:
                    p += " " + str(Fraction(num - (whole * denom), denom))
            else:
                p = str(num) + "/" + str(denom)
            calcNums.append(p)
            print("appended: ", p)
        else:
            calcNums.append(str(frac))
            print("appended1: ", str(frac))
    #print(calcNums)
    mix = re.split("([0-9]+ [0-9]+/[0-9]+|[0-9]+/[0-9]+|[0-9]+)", rec)
    #print(mix)
    counter = 0
    ret = ""
    print("calcNums :", calcNums)
    for x in mix:
        #print(x)
        if x[0].isdigit():
            if len(calcNums) > counter:
                ret += ''.join(calcNums[counter])
                #print(calcNums[counter])
                counter += 1
            else:
                ret += "FAIL\n"
            #print(calcNums[counter])
            
        else:
            ret += ''.join(x)
    return ret

x = scale('''Ingredients\n\n    
            Frosting:\n    
            15 ounces semi-sweet chocolate, finely chopped\n
            1 1/2 cups heavy cream\n
            Cake:\n
            2 cups all-purpose unbleached flour\n
            1 1/2 teaspoons baking soda\n
            3/4 teaspoon baking powder\n
            3/4 teaspoon salt\n
            12 tablespoons unsalted butter, at room temperature, plus more for the pans\n
            2 cups plus 2 tablespoons sugar\n
            3/4 cup nonalkalized cocoa powder (not Dutch-processed)\n
            2 teaspoons pure vanilla extract\n
            3 large eggs, at room temperature\n
            1 1/4 cups water\n
            1/4 cup milk\n''', '1/2')
print(x)    