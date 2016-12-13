def extract(wrong):
    wrong = list(wrong)
    wrong = [x.upper() for x in wrong if x.isalnum()]
    if len(wrong) == 0:
        return wrong
    ans = []
    tmp = ""
    counter = 0
    length = len(wrong)
    for x in wrong:
        if x.isdigit():
            if int(x) < 4:
                tmp += x
                if len(tmp) >= 2 or counter == (length - 1):
                    if int(tmp) > 10 or int(tmp) < 4:
                        return None
                    else:
                        if tmp != "":
                            ans.append(tmp)
                        tmp = ""
            elif tmp != "":
                return None
            else:
                ans.append(x)
        if x.isalpha():
            if x == "L":
                tmp += "1"
            elif x == "O":
                if tmp == "1":
                    tmp += "0"
                else:
                    return None
            elif x == "M" or x == "S":
                ans.append(x)
                tmp = ""
            else:
                return None
            if tmp != "":
                if len(tmp) >= 2 or counter == (length - 1):
                    if int(tmp) > 10 or int(tmp) < 4:
                        return None
                    else:
                        if tmp != "":
                            ans.append(tmp)
                        else:
                            return None
                        tmp = ""
        if counter == length:
            if x.isdigit() and int(x) >= 4:
                ans.append(x)
            else:
                return None
        counter += 1
    if len(ans) == 0:
        return None
    return ans;

