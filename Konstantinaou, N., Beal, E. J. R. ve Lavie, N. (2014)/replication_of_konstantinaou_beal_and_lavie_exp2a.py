#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on May 08, 2023, at 07:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'deney2a'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\wasd0\\Desktop\\melikevize\\deney2a.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Yonerge" ---
KAYonerge = keyboard.Keyboard()
TAYonerge = visual.TextStim(win=win, name='TAYonerge',
    text='Çalışmamıza hoş geldiniz.\n\nBirazdan ekranınıza kutucuk / kutucuklar içinde bazı renkler sunulacaktır, sunum sırasında ekrana gelen renk ve konum bilgilerini aklınızda tutmanız beklenmektedir. Ardından bir çemberin içinde ve dışında bulunacak şekilde 2 harf (X ve Z) sunulacaktır. Sizden, çember içindeki harfi de aklınızda tutmanız beklenmektedir. \n\nBu sunumun gerçekleşmesinin ardından ilk olarak çemberin içindeki harfin ne olduğu, ardından da ilk ekranda belirmiş olan pozisyondaki kutucuklardan bir tanesi sunularak renk ve konum bilgisinin doğru olup olmadığını cevaplamanız beklenmektedir.\n\nİlk 16 deneme alıştırma niteliğinde olup, 16. denemenin ardından deneye başlanacaktır.\n\nAlıştırma aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "CA500ms" ---
FA500 = visual.ImageStim(
    win=win,
    name='FA500', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from CA500
counter = 0

# --- Initialize components for Routine "LA500msL" ---
IABackgroundL = visual.ImageStim(
    win=win,
    name='IABackgroundL', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TALoadL = visual.TextStim(win=win, name='TALoadL',
    text='low',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TA1L = visual.TextStim(win=win, name='TA1L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
TA2L = visual.TextStim(win=win, name='TA2L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375,0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
TA3L = visual.TextStim(win=win, name='TA3L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
TA4L = visual.TextStim(win=win, name='TA4L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,-0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
TA5L = visual.TextStim(win=win, name='TA5L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
TA6L = visual.TextStim(win=win, name='TA6L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, 0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Yonerge" ---
continueRoutine = True
# update component parameters for each repeat
KAYonerge.keys = []
KAYonerge.rt = []
_KAYonerge_allKeys = []
# keep track of which components have finished
YonergeComponents = [KAYonerge, TAYonerge]
for thisComponent in YonergeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Yonerge" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *KAYonerge* updates
    waitOnFlip = False
    
    # if KAYonerge is starting this frame...
    if KAYonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KAYonerge.frameNStart = frameN  # exact frame index
        KAYonerge.tStart = t  # local t and not account for scr refresh
        KAYonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KAYonerge, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KAYonerge.started')
        # update status
        KAYonerge.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KAYonerge.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KAYonerge.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KAYonerge.status == STARTED and not waitOnFlip:
        theseKeys = KAYonerge.getKeys(keyList=None, waitRelease=False)
        _KAYonerge_allKeys.extend(theseKeys)
        if len(_KAYonerge_allKeys):
            KAYonerge.keys = _KAYonerge_allKeys[-1].name  # just the last key pressed
            KAYonerge.rt = _KAYonerge_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *TAYonerge* updates
    
    # if TAYonerge is starting this frame...
    if TAYonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TAYonerge.frameNStart = frameN  # exact frame index
        TAYonerge.tStart = t  # local t and not account for scr refresh
        TAYonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TAYonerge, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TAYonerge.started')
        # update status
        TAYonerge.status = STARTED
        TAYonerge.setAutoDraw(True)
    
    # if TAYonerge is active this frame...
    if TAYonerge.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in YonergeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Yonerge" ---
for thisComponent in YonergeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KAYonerge.keys in ['', [], None]:  # No response was made
    KAYonerge.keys = None
thisExp.addData('KAYonerge.keys',KAYonerge.keys)
if KAYonerge.keys != None:  # we had a response
    thisExp.addData('KAYonerge.rt', KAYonerge.rt)
thisExp.nextEntry()
# the Routine "Yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopAlistirma = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LoopAlistirma')
thisExp.addLoop(LoopAlistirma)  # add the loop to the experiment
thisLoopAlistirma = LoopAlistirma.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopAlistirma.rgb)
if thisLoopAlistirma != None:
    for paramName in thisLoopAlistirma:
        exec('{} = thisLoopAlistirma[paramName]'.format(paramName))

for thisLoopAlistirma in LoopAlistirma:
    currentLoop = LoopAlistirma
    # abbreviate parameter names if possible (e.g. rgb = thisLoopAlistirma.rgb)
    if thisLoopAlistirma != None:
        for paramName in thisLoopAlistirma:
            exec('{} = thisLoopAlistirma[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "CA500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CA500
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(500 / FRate)
    frame = 0
    # keep track of which components have finished
    CA500msComponents = [FA500]
    for thisComponent in CA500msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CA500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FA500* updates
        
        # if FA500 is starting this frame...
        if FA500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FA500.frameNStart = frameN  # exact frame index
            FA500.tStart = t  # local t and not account for scr refresh
            FA500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FA500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FA500.started')
            # update status
            FA500.status = STARTED
            FA500.setAutoDraw(True)
        
        # if FA500 is active this frame...
        if FA500.status == STARTED:
            # update params
            pass
        
        # if FA500 is stopping this frame...
        if FA500.status == STARTED:
            if frameN >= (FA500.frameNStart + FrameN):
                # keep track of stop time/frame for later
                FA500.tStop = t  # not accounting for scr refresh
                FA500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FA500.stopped')
                # update status
                FA500.status = FINISHED
                FA500.setAutoDraw(False)
        # Run 'Each Frame' code from CA500
        frame = frame + 1
        requirement = 500 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CA500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CA500ms" ---
    for thisComponent in CA500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from CA500
    counter = counter + 1
    # the Routine "CA500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LA500msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IABackgroundL.setImage('1.png')
    TA1L.setText('')
    TA2L.setText('')
    TA3L.setText('')
    TA4L.setText('')
    TA5L.setText('')
    TA6L.setText('')
    # Run 'Begin Routine' code from CALoadL
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(500 / FRate)
    frame = 0
    
    YanitD = 0
    YanitY = 0
    
    TA1L.height = 0.00
    TA2L.height = 0.00
    TA3L.height = 0.00
    TA4L.height = 0.00
    TA5L.height = 0.00
    TA6L.height = 0.00
    
    harfler = ["F","H","K","L","M","T","V","W","Y","X"]
    shuffle(harfler)
    TA1L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TA2L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TA3L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TA4L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TA5L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TA6L.text = harfler[0]
    harfler.pop(0)
    
    
    poslar = [1,2,3,4,5,6]
    shuffle(poslar)
    pos1 = poslar[0]
    poslar.pop(0)
    
    shuffle(poslar)
    pos2 = poslar[0]
    poslar.pop(0)
    
    shuffle(poslar)
    pos3 = poslar[0]
    poslar.pop(0)
    
    shuffle(poslar)
    pos4 = poslar[0]
    poslar.pop(0)
    
    shuffle(poslar)
    pos5 = poslar[0]
    poslar.pop(0)
    
    shuffle(poslar)
    pos6 = poslar[0]
    poslar.pop(0)
    
    if TALoadL.text == "low":
        if pos1 == 1:
            TA1L.height = 0.18
            IABackgroundL.setImage('1.png')
        elif pos1 == 2:
            TA2L.height = 0.18
            IABackgroundL.setImage('2.png')
        elif pos1 == 3:
            TA3L.height = 0.18
            IABackgroundL.setImage('3.png')
        elif pos1 == 4:
            TA4L.height = 0.18
            IABackgroundL.setImage('4.png')
        elif pos1 == 5:
            TA5L.height = 0.18
            IABackgroundL.setImage('5.png')
        elif pos1 == 6:
            TA6L.height = 0.18
            IABackgroundL.setImage('6.png')
    
    else:
        if pos1 == 1:
            TA1L.height = 0.18
        elif pos1 == 2:
            TA2L.height = 0.18
        elif pos1 == 3:
            TA3L.height = 0.18
        elif pos1 == 4:
            TA4L.height = 0.18
        elif pos1 == 5:
            TA5L.height = 0.18
        elif pos1 == 6:
            TA6L.height = 0.18
    
        if pos2 == 1:
            TA1L.height = 0.18
        elif pos2 == 2:
            TA2L.height = 0.18
        elif pos2 == 3:
            TA3L.height = 0.18
        elif pos2 == 4:
            TA4L.height = 0.18
        elif pos2 == 5:
            TA5L.height = 0.18
        elif pos2 == 6:
            TA6L.height = 0.18
    
        if pos3 == 1:
            TA1L.height = 0.18
        elif pos3 == 2:
            TA2L.height = 0.18
        elif pos3 == 3:
            TA3L.height = 0.18
        elif pos3 == 4:
            TA4L.height = 0.18
        elif pos3 == 5:
            TA5L.height = 0.18
        elif pos3 == 6:
            TA6L.height = 0.18
    
        if pos4 == 1:
            TA1L.height = 0.18
        elif pos4 == 2:
            TA2L.height = 0.18
        elif pos4 == 3:
            TA3L.height = 0.18
        elif pos4 == 4:
            TA4L.height = 0.18
        elif pos4 == 5:
            TA5L.height = 0.18
        elif pos4 == 6:
            TA6L.height = 0.18
    
        if pos5 == 1:
            TA1L.height = 0.18
        elif pos5 == 2:
            TA2L.height = 0.18
        elif pos5 == 3:
            TA3L.height = 0.18
        elif pos5 == 4:
            TA4L.height = 0.18
        elif pos5 == 5:
            TA5L.height = 0.18
        elif pos5 == 6:
            TA6L.height = 0.18
    
        if pos6 == 1:
            TA1L.height = 0.18
        elif pos6 == 2:
            TA2L.height = 0.18
        elif pos6 == 3:
            TA3L.height = 0.18
        elif pos6 == 4:
            TA4L.height = 0.18
        elif pos6 == 5:
            TA5L.height = 0.18
        elif pos6 == 6:
            TA6L.height = 0.18
    # keep track of which components have finished
    LA500msLComponents = [IABackgroundL, TALoadL, TA1L, TA2L, TA3L, TA4L, TA5L, TA6L]
    for thisComponent in LA500msLComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LA500msL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IABackgroundL* updates
        
        # if IABackgroundL is starting this frame...
        if IABackgroundL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IABackgroundL.frameNStart = frameN  # exact frame index
            IABackgroundL.tStart = t  # local t and not account for scr refresh
            IABackgroundL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IABackgroundL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IABackgroundL.started')
            # update status
            IABackgroundL.status = STARTED
            IABackgroundL.setAutoDraw(True)
        
        # if IABackgroundL is active this frame...
        if IABackgroundL.status == STARTED:
            # update params
            pass
        
        # if IABackgroundL is stopping this frame...
        if IABackgroundL.status == STARTED:
            if frameN >= (IABackgroundL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IABackgroundL.tStop = t  # not accounting for scr refresh
                IABackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IABackgroundL.stopped')
                # update status
                IABackgroundL.status = FINISHED
                IABackgroundL.setAutoDraw(False)
        
        # *TALoadL* updates
        
        # if TALoadL is starting this frame...
        if TALoadL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TALoadL.frameNStart = frameN  # exact frame index
            TALoadL.tStart = t  # local t and not account for scr refresh
            TALoadL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TALoadL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TALoadL.started')
            # update status
            TALoadL.status = STARTED
            TALoadL.setAutoDraw(True)
        
        # if TALoadL is active this frame...
        if TALoadL.status == STARTED:
            # update params
            pass
        
        # if TALoadL is stopping this frame...
        if TALoadL.status == STARTED:
            if frameN >= (TALoadL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TALoadL.tStop = t  # not accounting for scr refresh
                TALoadL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TALoadL.stopped')
                # update status
                TALoadL.status = FINISHED
                TALoadL.setAutoDraw(False)
        
        # *TA1L* updates
        
        # if TA1L is starting this frame...
        if TA1L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TA1L.frameNStart = frameN  # exact frame index
            TA1L.tStart = t  # local t and not account for scr refresh
            TA1L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA1L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA1L.started')
            # update status
            TA1L.status = STARTED
            TA1L.setAutoDraw(True)
        
        # if TA1L is active this frame...
        if TA1L.status == STARTED:
            # update params
            pass
        
        # if TA1L is stopping this frame...
        if TA1L.status == STARTED:
            if frameN >= (TA1L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TA1L.tStop = t  # not accounting for scr refresh
                TA1L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA1L.stopped')
                # update status
                TA1L.status = FINISHED
                TA1L.setAutoDraw(False)
        
        # *TA2L* updates
        
        # if TA2L is starting this frame...
        if TA2L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TA2L.frameNStart = frameN  # exact frame index
            TA2L.tStart = t  # local t and not account for scr refresh
            TA2L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA2L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA2L.started')
            # update status
            TA2L.status = STARTED
            TA2L.setAutoDraw(True)
        
        # if TA2L is active this frame...
        if TA2L.status == STARTED:
            # update params
            pass
        
        # if TA2L is stopping this frame...
        if TA2L.status == STARTED:
            if frameN >= (TA2L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TA2L.tStop = t  # not accounting for scr refresh
                TA2L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA2L.stopped')
                # update status
                TA2L.status = FINISHED
                TA2L.setAutoDraw(False)
        
        # *TA3L* updates
        
        # if TA3L is starting this frame...
        if TA3L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TA3L.frameNStart = frameN  # exact frame index
            TA3L.tStart = t  # local t and not account for scr refresh
            TA3L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA3L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA3L.started')
            # update status
            TA3L.status = STARTED
            TA3L.setAutoDraw(True)
        
        # if TA3L is active this frame...
        if TA3L.status == STARTED:
            # update params
            pass
        
        # if TA3L is stopping this frame...
        if TA3L.status == STARTED:
            if frameN >= (TA3L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TA3L.tStop = t  # not accounting for scr refresh
                TA3L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA3L.stopped')
                # update status
                TA3L.status = FINISHED
                TA3L.setAutoDraw(False)
        
        # *TA4L* updates
        
        # if TA4L is starting this frame...
        if TA4L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TA4L.frameNStart = frameN  # exact frame index
            TA4L.tStart = t  # local t and not account for scr refresh
            TA4L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA4L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA4L.started')
            # update status
            TA4L.status = STARTED
            TA4L.setAutoDraw(True)
        
        # if TA4L is active this frame...
        if TA4L.status == STARTED:
            # update params
            pass
        
        # if TA4L is stopping this frame...
        if TA4L.status == STARTED:
            if frameN >= (TA4L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TA4L.tStop = t  # not accounting for scr refresh
                TA4L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA4L.stopped')
                # update status
                TA4L.status = FINISHED
                TA4L.setAutoDraw(False)
        
        # *TA5L* updates
        
        # if TA5L is starting this frame...
        if TA5L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TA5L.frameNStart = frameN  # exact frame index
            TA5L.tStart = t  # local t and not account for scr refresh
            TA5L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA5L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA5L.started')
            # update status
            TA5L.status = STARTED
            TA5L.setAutoDraw(True)
        
        # if TA5L is active this frame...
        if TA5L.status == STARTED:
            # update params
            pass
        
        # if TA5L is stopping this frame...
        if TA5L.status == STARTED:
            if frameN >= (TA5L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TA5L.tStop = t  # not accounting for scr refresh
                TA5L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA5L.stopped')
                # update status
                TA5L.status = FINISHED
                TA5L.setAutoDraw(False)
        
        # *TA6L* updates
        
        # if TA6L is starting this frame...
        if TA6L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TA6L.frameNStart = frameN  # exact frame index
            TA6L.tStart = t  # local t and not account for scr refresh
            TA6L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA6L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA6L.started')
            # update status
            TA6L.status = STARTED
            TA6L.setAutoDraw(True)
        
        # if TA6L is active this frame...
        if TA6L.status == STARTED:
            # update params
            pass
        
        # if TA6L is stopping this frame...
        if TA6L.status == STARTED:
            if frameN >= (TA6L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TA6L.tStop = t  # not accounting for scr refresh
                TA6L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA6L.stopped')
                # update status
                TA6L.status = FINISHED
                TA6L.setAutoDraw(False)
        # Run 'Each Frame' code from CALoadL
        frame = frame + 1
        requirement = 500 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LA500msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LA500msL" ---
    for thisComponent in LA500msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LA500msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'LoopAlistirma'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
