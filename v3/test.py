# -*- coding: utf-8 -*-
import os
import sys
import re
import guessit
def pirate(badFolder, goodFolder):
    files =[]
    illegalFilenames =["nfo", "png", "url", "idx", "txt", "jpg", "dat"]
    #onlyfiles = [f for f in os.listdir(badFolder) if os.path.isfile(join(badFolder, f))]
    for root, directory, file in os.walk(badFolder):
        if len(file) > 0 and file[0][-3:] not in illegalFilenames:
            files.append(file[0].encode('utf-8', errors='replace'))
    for file in files:
       print(guessit.guessit(file))
       print(repr(file))
       pass
    return badFolder

test = pirate('notStructured', 'structured')
print(test)
