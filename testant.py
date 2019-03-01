"""
Example of how to use the ANT module
"""
import sys
import os
from psychopy import visual, core, event, monitors, tools, logging, gui, clock, data

import pyglet
import time
import numpy as np
import random as random
from ant import ANTExp
import threading
import itchat

friend = '言午'
try:
    itchat.auto_login(True)
    itchat.send('Hello',toUserName = 'filehelper')
except Exception:
    print("error!!!")
################################
### Main program starts here
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'ANTSend'  # from the Builder filename that created this script
expInfo = {'session': '01', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/downloads/ant-master/testant.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp



# Start Code - component code to be run before the window creation
# Prepare the window and stimulus
winsize = [1440, 900]

mon = monitors.Monitor('testMonitor', distance=60, width=28.5)
mon.setDistance(60)
mon.setWidth(28.5)
mon.setSizePix(winsize)

win = visual.Window(winsize, waitBlanking=True, winType='pyglet', fullscr=True, 
        color='white', units='deg', monitor=mon)
pw = visual.TextStim(win, alignHoriz='center', wrapWidth=12, height=0.01, color='black', 
        text="Please wait (checking screen timing)...")
pw.autoDraw = True
pw.draw()
win.flip()
refresh = win.getActualFrameRate(nIdentical=50, nMaxFrames=900, nWarmUpFrames=100, threshold=1)
pw.autoDraw = False

halted = False

win.flip()
globalClock = core.Clock()
startTime = time.time()
now = globalClock.getTime()
if now > 0.001:
    sys.stderr.write("WARNING: Your machine seems a little slow; just looking at the watch takes more than 1 mS (%.3f)!\n" % t0)
else:
    print("Internal initial timing offset is not to worry about (only %0.6f s)" % now)

endExperiment = False




exp = ANTExp(mon, win, winsize, refresh, globalClock, startTime, logFile)

noPractice = exp.displayInstructions()

allData = None
if noPractice:
    sys.stderr.write("Skipped practice block on user's request\n")
else:
    exp.displayText("Starting practice block in 2 seconds", noWait=True, showLine=False, time=2)
    if not exp.practiceBlock():
        sys.stderr.write("Shortened practice block on user's request\n")

clock = core.Clock()


for r in range(4):
    if r%2 == 0:
        if exp.displayText("Starting experimental block %d of 2\nHit any key when ready to start." % (r/2+1), showLine=False):
            break
        core.wait(1)
        if r ==2:
            exp.displayText("现在开始休息1分钟", noWait = True, time = 60)
    block = exp.fullExperiment(friend)
    
 
 
    if block == None:
        break
    if allData == None:
        allData = block
    else:
        allData = np.concatenate((allData, block))

# do something with allData here!

endTime = time.time()
now = globalClock.getTime()
print("Real time was %0.3f and global clock counted %0.3f (compare %0.6f to initial timing offset to determine drift)" % 
        (endTime-startTime, now, now - (endTime-startTime)))
        
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit

win.close()
core.quit()
