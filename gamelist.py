import os.path


def initWrite(outputDir):
    gamelist = open(os.path.join(outputDir, "gamelist.xml"), 'w', encoding="utf-8")
    gamelist.write('<?xml version="1.0"?>\n')
    gamelist.write("<gameList>\n")
    return gamelist


def initRead(outputDir):
    gamelist = open(os.path.join(outputDir, "gamelist.xml"), 'r', encoding="utf-8")
    return gamelist


def writeGamelistHiddenEntry(gamelist, romName, genre, useGenreFolder):
    romPath = (genre + "/" + romName) if useGenreFolder else romName
    gamelist.write("    <game>\n")
    gamelist.write("        <path>./" + romPath + "</path>\n")
    gamelist.write("        <hidden>true</hidden>\n")
    gamelist.write("    </game>\n")

#<video>./videos/1944.mp4</video>
#<marquee>./images/1944-marquee.png</marquee>
#<thumbnail>./images/1944-thumb.png</thumbnail>
#<manual>./manuals/1944-manual.pdf</manual>
#<bezel>./images/outrun-bezel.png</bezel>
def writeGamelistEntry(gamelist, romName, name, desc, year, frontPic, developer, publisher, genre,
                        useGenreFolder,manual,video, marquee, thumbnail, bezel):
    romPath = (genre + "/" + romName) if useGenreFolder else romName
    gamelist.write("    <game>\n")
    gamelist.write("        <path>./" + romPath + "</path>\n")
    gamelist.write("        <name>" + name.replace('&', '&amp;') + "</name>\n")
    gamelist.write("        <desc>" + desc.replace('&', '&amp;') + "</desc>\n")
    gamelist.write("        <releasedate>" + year + "0101T000000</releasedate>\n")
    if(not frontPic == None):
        gamelist.write("        <image>" + frontPic + "</image>\n")
    if(not manual == None):
        gamelist.write("        <manual>" + manual + "</manual>\n")
    if(not video == None):
        gamelist.write("        <video>" + video + "</video>\n")
    if(not marquee == None):
        gamelist.write("        <marquee>" + marquee + "</marquee>\n")
    if(not thumbnail == None):
        gamelist.write("        <thumbnail>" + thumbnail + "</thumbnail>\n")
    if(not bezel == None):
        gamelist.write("        <bezel>" + bezel + "</bezel>\n")
    gamelist.write("        <developer>" + developer.replace('&', '&amp;').replace('<', '&lgt;').replace('>', '&rgt;') + "</developer>\n")
    gamelist.write("        <publisher>" + publisher.replace('&', '&amp;').replace('<', '&lgt;').replace('>', '&rgt;') + "</publisher>\n")
    gamelist.write("        <genre>" + genre.replace('[', '').replace(']', '') + "</genre>\n")
    gamelist.write("    </game>\n")


def writeGamelistFolder(gamelist, name, image):
    gamelist.write("    <folder>\n")
    gamelist.write("        <path>./" + name + "</path>\n")
    gamelist.write("        <name>" + name + "</name>\n")
    if(not image == None):    
        gamelist.write("        <image>./downloaded_images/" + name + ".png</image>\n")
    gamelist.write("    </folder>\n")


def closeWrite(gamelist):
    gamelist.write("</gameList>\n")
    gamelist.close()


def closeRead(gamelist):
    gamelist.close()
