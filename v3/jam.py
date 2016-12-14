import re
from collections import Counter
def jam(jammers):
    ans = []
    ret = {}
    andSplit = []
    counter = 1
    pattern = re.compile("[0-9] and [0-9]")
    f = jammers.splitlines()
    for x in f:
        if "plus" in x:
            counter += 2
        print(counter)
        if pattern.search(x):
            x = x.replace(" and ", "", 1)
        x = x.replace(" and " , ",", counter)
        x = x.replace(" with " , ",", 1)
        x = x.replace(" plus " , " ")
        andSplit.append(x)
        counter = 1
    #print(andSplit)
    for x in andSplit:
        ans.append(re.split(",", x)[1:-1])
    
    guests = []
    #print(ans)
    for field in ans:
        guests.append(field)
    guests = [item for sublist in guests for item in sublist]
    guests = sorted(guests)
    for guest in guests:
        if guest.strip() in ret:
            ret[guest.strip()] += 1
        else:
            ret[guest.strip()] = 1
            
    return ret
    
x = jam('''422/25/8 22 February 1992, Nicholas Parsons with Derek Nimmo, Clement Freud, Peter Jones and Wendy Richard, advertising.
423/25/9 20 July 1992 and 27 July 1992, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, plus Paul Merton, Tony Hawks, Sheila Hancock, Tim Rice, Wendy Richard, Stephen Fry, Barry Cryer, Richard Murdoch, Peter Cook, Ian Messiter, Victoria Wood, Jimmy Mulville, Elaine Stritch and Sandi Toksvig, Silver Minutes.
864/73/8 24 August 2015 and 23 November 2015, Nicholas Parsons with Paul Merton, Gyles Brandreth, Susan Calman and Tom Allen, whisky galore
424/26/1 2 January 1993, Nicholas Parsons with Paul Merton, Clement Freud, Wendy Richard and Tony Slattery, briefs.''')
print(x)