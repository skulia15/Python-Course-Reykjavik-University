# -*- coding: utf-8 -*-
import os
import shutil
import re
from guessit import guessit

def getPath(file, newpath, badFolder):
    seasonepisode = re.compile("[sS][0-9]+[eE][0-9]+|[0-9]+x[0-9]+|[0-9]{3}[\s]") #Check whether 
    epi = re.compile("^([eE](pisode)?)?\s?\d+(\.\w{3})?")
    title = re.split(seasonepisode, file[0])[0]
    if len(title)==0 or re.match(epi, file[0]):
        print("damn")
        print("maybe....: " , file[1])
        splitfilepath = file[1].split("\\")
        seasonre = re.compile("^[sS](eason|eries)?\s?\d{1,2}$")
        if re.match(epi,splitfilepath[-2]):
            print("FILEASFARGERGGASRGAFG:", file[1])
            print("matching with: ",splitfilepath[-2])
            #if re.match(seasonre, splitfilepath[-3]) and splitfilepath[-4] == badFolder:
                #   print("newpath: ", newpath)
                #  print("file[0]: ", file[0])
                # shutil.move(file[1], newpath)
            #elif re.match(seasonre, splitfilepath[-3]):
                #   newpath = os.path.join(newpath, splitfilepath[-4])
                #  if not os.path.exists(newpath):
                    #   os.makedirs(newpath)
                # newpath = os.path.join(newpath, splitfilepath[-3])
                #print("newpath-notbadfolder: ", newpath)
                # print("file[0]-notbadfolder: ", file[0])
                #if not os.path.exists(newpath):
                    #   os.makedirs(newpath)
            #else:
                #   newpath = os.path.join(newpath, splitfilepath[-3])
                #  if not os.path.exists(newpath):
                #     os.makedirs(newpath)
                # if info.__contains__("season"):
                #    newpath = os.path.join(newpath, ("Season " + str(info["season"])))
                    #   print("newpath-noseasonfolder: ", newpath)
                    #  print("file[0]-noseasonfolder: ", file[0])
                    # if not os.path.exists(newpath):
                    #    os.makedirs(newpath)
        elif re.match(seasonre, splitfilepath[-2]) and splitfilepath[-3] == badFolder:
            print("newpath: ", newpath)
            print("file[0]: ", file[0])
            shutil.move(file[1], newpath)
        elif re.match(seasonre, splitfilepath[-2]):
            newpath = os.path.join(newpath, splitfilepath[-3])
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            newpath = os.path.join(newpath, splitfilepath[-2])
            print("newpath-notbadfolder: ", newpath)
            print("file[0]-notbadfolder: ", file[0])
            if not os.path.exists(newpath):
                os.makedirs(newpath)
        else:
            newpath = os.path.join(newpath, splitfilepath[-2])
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            if info.__contains__("season"):
                newpath = os.path.join(newpath, ("Season " + str(info["season"])))
                print("newpath-noseasonfolder: ", newpath)
                print("file[0]-noseasonfolder: ", file[0])
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
        #shutil.move(file[1], os.path.join(newpath, file[0]))
    else:
        if info.__contains__("title"):
            newpath = os.path.join(newpath, info["title"])
            if not os.path.exists(newpath):
                #print("3")
                os.makedirs(newpath)
        else:
            newpath = os.path.join(newpath, file[0])
            #print("got here")
            #print("newpath is: ", newpath)
            if not os.path.exists(newpath):
                #print("3")
                os.makedirs(newpath)
        if info.__contains__("season"):
            newpath = os.path.join(newpath, ("Season " + str(info["season"])))
            if not os.path.exists(newpath):
                #print("newpath now is: ", newpath)
                os.makedirs(newpath)
            shutil.move(file[1], os.path.join(newpath, file[0]))
        else:
            shutil.move(file[1], os.path.join(newpath, file[0]))
def moveFiles(filesToMove, badFolder, goodFolder):
    for file in filesToMove:
        info = guessit(file[0]) #Use guessit to obtain relatively good info about the file
        if info.__contains__("type"):
            if info["type"] == "movie":
                newpath = os.path.join(goodFolder, "Movies")
                if not os.path.exists(newpath):
                    #print("1")
                    os.makedirs(newpath)
                shutil.move(file[1], os.path.join(newpath, file[0])) #If guessit guesses that the file is a movie, we put the file at the root of the movies directory
            elif info["type"] == "episode":
                newpath = os.path.join(goodFolder, "Episodes")
                if not os.path.exists(newpath):
                    #print("2")
                    os.makedirs(newpath)
                newPath = getPath(file, newpath)

def pirate2(badFolder, goodFolder):
    theFiles = []
    movies = []
    garbage = ["nfo", "url", "txt", "dat"] #Garbage files
    for root, directory, files in os.walk(badFolder):
        for file in files:
            if len(file) > 0 and file[-3:] in removeFileNames or file[-4:-3] != '.' or "sample" in file: #Remove sample files and grabage files
                os.remove(os.path.join(root, file))
            else:
                if file[-3:] != "mp3": #ignore all mp3 files
                    theFiles.append((str(file.encode('utf-8', errors='replace'), 'utf-8'), os.path.join(root, file)))
    moveFiles(theFiles, badFolder, goodFolder)
    return badFolder

pirate2("downloads - Copy", "structured")

##TODO: eyða tómum folders
# Laga alltof mikið sem viðkemur þáttum og nafnagift þeirra
# eyða sample files
#Capitalizea nöfn á möppum