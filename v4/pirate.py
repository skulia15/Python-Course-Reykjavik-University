# -*- coding: utf-8 -*-
import os
import shutil
from guessit import guessit
def moveFiles(filesToMove, goodFolder):
    for file in filesToMove:
        #print("length:", len(file), "file:")
        info = guessit(file[0])
        if info.__contains__("type"):
            #print("file[1]" , file[1])
            if info["type"] == "movie":
                newpath = os.path.join(goodFolder, "Movies")
             #   print("newpath:",newpath)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                shutil.move(file[1], os.path.join(newpath, file[0]))
                #print("moving ", file[0])
            elif info["type"] == "episode":
                newpath = os.path.join(goodFolder, "Episodes")
               # print("newpath:",newpath)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                if info.__contains__("title"):
                    newpath = os.path.join(newpath, info["title"])
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    if info.__contains__("season"):
                        newpath = os.path.join(newpath, ("S" + str(info["season"])))
                        if not os.path.exists(newpath):
                            os.makedirs(newpath)
                        shutil.move(file[1], os.path.join(newpath, file[0]))
                        #print("moving ", file[0])
                    else:
                        shutil.move(file[1], os.path.join(newpath, file[0]))
                        #print("moving ", file[0])
                else:
                    shutil.move(file[1], os.path.join(newpath, file[0]))

def pirate(badFolder, goodFolder):
    theFiles = []
    movies = []
    removeFileNames = ["nfo", "url", "txt", "dat", "path", "mp3"] #ignore mp3 insted of del
    #illegalFilenames = [ "png",  "idx",  "jpg",  "mp3", "rar", "mta"] #Never moved file types
    for root, directory, files in os.walk(badFolder):
        #if len(file) > 0:
            #print(file[0].encode('utf-8', errors='replace'))
        for file in files:
            if len(file) > 0 and file[-3:] in removeFileNames or file[-4:-3] != '.':
                os.remove(os.path.join(root, file))
            else:
                theFiles.append((str(file.encode('utf-8', errors='replace'), 'utf-8'), os.path.join(root, file)))
    moveFiles(theFiles, goodFolder)
    for root, directory, files in os.walk(badFolder):
        try:
            if os.listdir(root) == []:
                #os.removedirs(root)
                pass
        except OSError as ex:
            print(ex)
    #for x in movies:
        #print(x)
    return badFolder

test = pirate('b4', 'structured')
#print(test)

##TODO: eyða tómum folders
# eyða sample files
