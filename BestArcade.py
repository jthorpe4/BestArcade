# -*- coding: utf-8 -*-
import sys, os.path
from gui import GUI
from logger import Logger
    
if __name__ == "__main__":
    scriptDir = os.path.abspath(os.path.dirname(sys.argv[0]))
    title = 'BestArcade 1.5'
    logger = Logger()
    logger.log(title)
    logger.log('\nScript path : '+scriptDir)            
    gui = GUI(scriptDir,logger, title) 
    gui.draw()


#1.6
#----
# retest for N2
# allow to choose between pi3 and N2
# add vertical games tab
# add info to generate dat from mame exe (see my handheld thread on reddit) -> hhhhhhm si if regular xml from mame site work
# allow basicsorter generation without dat / prevents generation without dat ?