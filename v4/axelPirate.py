# -*- coding: utf-8 -*-
import os
import re
import shutil

from guessit import guessit

seasonepisode = re.compile("[sS][0-9]+[eE][0-9]+|[0-9]+x[0-9]+|[0-9]{3}[\s]")
seasonre = re.compile("[sS](eason|eries)?\s?\d{1,2}$")
episodere = re.compile("([eE](pisode)?)?\s?\d+(\.\w{3})?$")

def checkdirexistance(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def moveFiles(filesToMove, badFolder, goodFolder):
    for file in filesToMove:
        info = guessit(file[0]) #Use guessit to obtain relatively good info about the file
        if info.__contains__("type"):
            
            splitfilepath = file[1].split("\\")
            filename = splitfilepath[-1]
            
            # MOVIES
            if info["type"] == "movie":
                newpath = os.path.join(goodFolder, "Movies")
                checkdirexistance(newpath)
                #newpath = os.path.join(newpath, filename)

            # EPISODES
            elif info["type"] == "episode":
                newpath = os.path.join(goodFolder, "Episodes")
                checkdirexistance(newpath)

                season = ''
                showname = ''

                # IF EPISODE IN FOLDER IN FOLDER
                if len(splitfilepath) > 3:
                    # IF EPISODE IS NAMED EPISODE
                    for i in splitfilepath:
                        if re.search(seasonre, i):
                            season = str(re.search(seasonre, i).group(0))
                        if not re.search(seasonre, i) and i != filename and not re.search(seasonepisode, i) and i != 'Subtitles':
                            showname = i
                    print('SHOWNAME: ', showname, 'SEASON:' , season)

                # IF EPISODE IF IN ROOT
                elif False:
                    filename = re.split(seasonepisode, file[0])

                # MAKE DIRECTORIES IN OS
                newpath = os.path.join(newpath, showname)
                checkdirexistance(newpath)
                newpath = os.path.join(newpath, season)
                checkdirexistance(newpath)
                newpath = os.path.join(newpath, filename)
                checkdirexistance(newpath)
                print('NEWPATH: ', newpath)

            # MOVE FILE TO NEW PATH
            checkdirexistance(newpath)
            if not os.path.isfile(os.path.join(newpath, file[0])):
                #print(newpath)
                shutil.move(file[1], newpath)

def pirate2(badFolder, goodFolder):
    theFiles = []
    movies = []
    garbage = ["nfo", "url", "txt", "dat", "ini"] #Garbage files
    for root, directory, files in os.walk(badFolder):
        for file in files:
            if len(file) > 0 and file[-3:] in garbage or file[-4:-3] != '.' or "sample" in file: #Remove sample files and grabage files
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
