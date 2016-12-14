import os
#import pathlib
#import glob
def parse_submissions(submissions):
    #submissions += "\*"
    data = []
    ans = []
    grading = ""
    team = ""
    problem = ""
    #folders = glob.glob(submissions)
    #for folder in folders:
    #    with open(folder + "\data.tcl") as f:
    #        data.append(f.readlines())
    for r, d, f in os.walk(submissions):
        if len(f) > 0 and f[0].endswith(".tcl"):
            path = os.path.join(r, f[0])
            with open(path) as f:
                data.append(f.readlines())
    
    for x in data:
        tmp = x
        for t in tmp:
            team = tmp[2].split()[2]
            problem = tmp[1].split()[2]
            date = tmp[0].split()[2]
            grading = tmp[3].split()[2]
        if grading == "Accepted":
            ans.append((team, problem, date))
    print(ans)
    print("----------")
    return [(x[0], x[1]) for x in sorted(ans, key=lambda p: p[2])]

x = parse_submissions('.')
print(x)