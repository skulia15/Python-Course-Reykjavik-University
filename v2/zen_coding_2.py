def zen_expand(zen):
    import re
    def recurse(zen, multi):
        tag = zen[0]
        open = "<" + tag + ">"
        close = "</" + tag + ">"
        if len(zen) == 1:
            return multi * (open + close)
        op = zen[1]
        if op == '+':
            zen = zen[2:]
            return multi * (open + close) + recurse(zen, 1)
        if op == '*':
            multi = int(zen[2])
            del zen[1:3]
            return recurse(zen, multi)
        if op == ">":
            zen = zen[2:]
            return multi*(open + recurse(zen, 1) + close)
    ans = re.split('(>|\+|\*)', zen)
    return recurse(ans, 1)