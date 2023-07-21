#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on May 13, 2023, at 19:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.0')


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
psychopyVersion = '2023.1.0'
expName = 'merve'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\wasd0\\Desktop\\merve\\merve.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='norm')
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

# --- Initialize components for Routine "yonerge" ---
KAYonerge = keyboard.Keyboard()
TAYonerge = visual.TextStim(win=win, name='TAYonerge',
    text='Çalışmamıza hoş geldiniz.\n\nBirazdan ekranınıza kutucuk / kutucuklar içinde bazı renkler, ve, noktalardan oluşan bir çemberin içinde ve dışında bulunacak şekilde 2 harf (X ve Z) sunulacaktır. Sizden, ekranınıza gelen kutucukların renk ve konum bilgileriyle beraber, çember içindeki harfi de aklınızda tutmanız beklenmektedir. \n\nBu sunumun gerçekleşmesinin ardından ilk olarak çemberin içindeki harfin ne olduğu (X için 0, Z için 2 tuşuna tıklayınız), ardından da ilk ekranda belirmiş olan pozisyondaki kutucuklardan bir tanesi sunularak renk ve konum bilgisinin doğru olup olmadığını cevaplamanız (eşleşme varsa S, eşleşme yoksa A tuşuna tıklayınız) beklenmektedir.\n\nİlk 16 deneme alıştırma niteliğinde olup, 16. denemenin ardından deneye başlanacaktır.\n\nAlıştırma aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "FA800ms" ---
IA800 = visual.ImageStim(
    win=win,
    name='IA800', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TCondition = visual.TextStim(win=win, name='TCondition',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TLoadTask = visual.TextStim(win=win, name='TLoadTask',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from CA800
counter = 0

r1 = 0
g1 = 0
b1 = 0
r2 = 0
g2 = 0
b2 = 0
r3 = 0
g3 = 0
b3 = 0
r4 = 0
g4 = 0
b4 = 0
r5 = 0
g5 = 0
b5 = 0
r6 = 0
g6 = 0
b6 = 0

# --- Initialize components for Routine "LA200msL" ---
IALoadBackgroundL = visual.ImageStim(
    win=win,
    name='IALoadBackgroundL', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
IA1L = visual.ImageStim(
    win=win,
    name='IA1L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
IA2L = visual.ImageStim(
    win=win,
    name='IA2L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IA3L = visual.ImageStim(
    win=win,
    name='IA3L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
IA4L = visual.ImageStim(
    win=win,
    name='IA4L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IA5L = visual.ImageStim(
    win=win,
    name='IA5L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
IA6L = visual.ImageStim(
    win=win,
    name='IA6L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "BA2000ms" ---
IA2000 = visual.ImageStim(
    win=win,
    name='IA2000', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "FA2000msL" ---
IAFlankerBackgroundL = visual.ImageStim(
    win=win,
    name='IAFlankerBackgroundL', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TAHedefL = visual.TextStim(win=win, name='TAHedefL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.13, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TACeldiriciL = visual.TextStim(win=win, name='TACeldiriciL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.186, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "FA500ms" ---
IA500 = visual.ImageStim(
    win=win,
    name='IA500', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
KAFlankerR = keyboard.Keyboard()
SAFlankerR = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SAFlankerR')
SAFlankerR.setVolume(1.0)

# --- Initialize components for Routine "LAmsR" ---
IALoadBackgroundR = visual.ImageStim(
    win=win,
    name='IALoadBackgroundR', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
IA1R = visual.ImageStim(
    win=win,
    name='IA1R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
IA2R = visual.ImageStim(
    win=win,
    name='IA2R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IA3R = visual.ImageStim(
    win=win,
    name='IA3R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
IA4R = visual.ImageStim(
    win=win,
    name='IA4R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IA5R = visual.ImageStim(
    win=win,
    name='IA5R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
IA6R = visual.ImageStim(
    win=win,
    name='IA6R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
dfgfhdf = visual.TextStim(win=win, name='dfgfhdf',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "yonerge" ---
continueRoutine = True
# update component parameters for each repeat
KAYonerge.keys = []
KAYonerge.rt = []
_KAYonerge_allKeys = []
# keep track of which components have finished
yonergeComponents = [KAYonerge, TAYonerge]
for thisComponent in yonergeComponents:
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

# --- Run Routine "yonerge" ---
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
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in yonergeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "yonerge" ---
for thisComponent in yonergeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KAYonerge.keys in ['', [], None]:  # No response was made
    KAYonerge.keys = None
thisExp.addData('KAYonerge.keys',KAYonerge.keys)
if KAYonerge.keys != None:  # we had a response
    thisExp.addData('KAYonerge.rt', KAYonerge.rt)
thisExp.nextEntry()
# the Routine "yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopAlistirma = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('deney_zhang.xlsx'),
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
    
    # --- Prepare to start Routine "FA800ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    TCondition.setText(condition)
    TLoadTask.setText(taskcevap)
    # Run 'Begin Routine' code from CA800
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(800 / FRate)
    frame = 0
    # keep track of which components have finished
    FA800msComponents = [IA800, TCondition, TLoadTask]
    for thisComponent in FA800msComponents:
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
    
    # --- Run Routine "FA800ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IA800* updates
        
        # if IA800 is starting this frame...
        if IA800.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA800.frameNStart = frameN  # exact frame index
            IA800.tStart = t  # local t and not account for scr refresh
            IA800.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA800, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA800.started')
            # update status
            IA800.status = STARTED
            IA800.setAutoDraw(True)
        
        # if IA800 is active this frame...
        if IA800.status == STARTED:
            # update params
            pass
        
        # if IA800 is stopping this frame...
        if IA800.status == STARTED:
            if frameN >= (IA800.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA800.tStop = t  # not accounting for scr refresh
                IA800.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA800.stopped')
                # update status
                IA800.status = FINISHED
                IA800.setAutoDraw(False)
        
        # *TCondition* updates
        
        # if TCondition is starting this frame...
        if TCondition.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TCondition.frameNStart = frameN  # exact frame index
            TCondition.tStart = t  # local t and not account for scr refresh
            TCondition.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TCondition, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TCondition.started')
            # update status
            TCondition.status = STARTED
            TCondition.setAutoDraw(True)
        
        # if TCondition is active this frame...
        if TCondition.status == STARTED:
            # update params
            pass
        
        # if TCondition is stopping this frame...
        if TCondition.status == STARTED:
            if frameN >= (TCondition.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TCondition.tStop = t  # not accounting for scr refresh
                TCondition.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TCondition.stopped')
                # update status
                TCondition.status = FINISHED
                TCondition.setAutoDraw(False)
        
        # *TLoadTask* updates
        
        # if TLoadTask is starting this frame...
        if TLoadTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TLoadTask.frameNStart = frameN  # exact frame index
            TLoadTask.tStart = t  # local t and not account for scr refresh
            TLoadTask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TLoadTask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TLoadTask.started')
            # update status
            TLoadTask.status = STARTED
            TLoadTask.setAutoDraw(True)
        
        # if TLoadTask is active this frame...
        if TLoadTask.status == STARTED:
            # update params
            pass
        
        # if TLoadTask is stopping this frame...
        if TLoadTask.status == STARTED:
            if frameN >= (TLoadTask.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TLoadTask.tStop = t  # not accounting for scr refresh
                TLoadTask.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TLoadTask.stopped')
                # update status
                TLoadTask.status = FINISHED
                TLoadTask.setAutoDraw(False)
        # Run 'Each Frame' code from CA800
        frame = frame + 1
        requirement = 800 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FA800msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FA800ms" ---
    for thisComponent in FA800msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from CA800
    counter = counter + 1
    
    r1 = float(round(random(),4))
    g1 = float(round(random(),4))
    b1 = float(round(random(),4))
    
    r2 = float(round(random(),4))
    g2 = float(round(random(),4))
    b2 = float(round(random(),4))
    
    r3 = float(round(random(),4))
    g3 = float(round(random(),4))
    b3 = float(round(random(),4))
    
    r4 = float(round(random(),4))
    g4 = float(round(random(),4))
    b4 = float(round(random(),4))
    
    r5 = float(round(random(),4))
    g5 = float(round(random(),4))
    b5 = float(round(random(),4))
    
    r6 = float(round(random(),4))
    g6 = float(round(random(),4))
    b6 = float(round(random(),4))
    # the Routine "FA800ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LA200msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IA1L.setColor([r1,g1,b1], colorSpace='rgb')
    IA2L.setColor([r2,g2,b2], colorSpace='rgb')
    IA3L.setColor([r3,g3,b3], colorSpace='rgb')
    IA4L.setColor([r4,g4,b4], colorSpace='rgb')
    IA5L.setColor([r5,g5,b5], colorSpace='rgb')
    IA6L.setColor([r6,g6,b6], colorSpace='rgb')
    # Run 'Begin Routine' code from CAL
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(200 / FRate)
    frame = 0
    
    if TCondition.text == "LL": #LOW LOAD LARGE COLOR CHANGE
        IA5L.size = (0.053, 0.093)
        IA6L.size = (0.053, 0.093)
    elif TCondition.text == "HL": #HİGH LOAD LARGE COLOR CHANGE
        IA1L.size = (0.053, 0.093)
        IA2L.size = (0.053, 0.093)
        IA3L.size = (0.053, 0.093)
        IA4L.size = (0.053, 0.093)
    elif TCondition.text == "LS": # LOW LOAD SMALL COLOR CHANGE
        IA5L.size = (0.053, 0.093)
        IA6L.size = (0.053, 0.093)
    # keep track of which components have finished
    LA200msLComponents = [IALoadBackgroundL, IA1L, IA2L, IA3L, IA4L, IA5L, IA6L]
    for thisComponent in LA200msLComponents:
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
    
    # --- Run Routine "LA200msL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IALoadBackgroundL* updates
        
        # if IALoadBackgroundL is starting this frame...
        if IALoadBackgroundL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IALoadBackgroundL.frameNStart = frameN  # exact frame index
            IALoadBackgroundL.tStart = t  # local t and not account for scr refresh
            IALoadBackgroundL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IALoadBackgroundL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IALoadBackgroundL.started')
            # update status
            IALoadBackgroundL.status = STARTED
            IALoadBackgroundL.setAutoDraw(True)
        
        # if IALoadBackgroundL is active this frame...
        if IALoadBackgroundL.status == STARTED:
            # update params
            pass
        
        # if IALoadBackgroundL is stopping this frame...
        if IALoadBackgroundL.status == STARTED:
            if frameN >= (IALoadBackgroundL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IALoadBackgroundL.tStop = t  # not accounting for scr refresh
                IALoadBackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IALoadBackgroundL.stopped')
                # update status
                IALoadBackgroundL.status = FINISHED
                IALoadBackgroundL.setAutoDraw(False)
        
        # *IA1L* updates
        
        # if IA1L is starting this frame...
        if IA1L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA1L.frameNStart = frameN  # exact frame index
            IA1L.tStart = t  # local t and not account for scr refresh
            IA1L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA1L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA1L.started')
            # update status
            IA1L.status = STARTED
            IA1L.setAutoDraw(True)
        
        # if IA1L is active this frame...
        if IA1L.status == STARTED:
            # update params
            pass
        
        # if IA1L is stopping this frame...
        if IA1L.status == STARTED:
            if frameN >= (IA1L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA1L.tStop = t  # not accounting for scr refresh
                IA1L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA1L.stopped')
                # update status
                IA1L.status = FINISHED
                IA1L.setAutoDraw(False)
        
        # *IA2L* updates
        
        # if IA2L is starting this frame...
        if IA2L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA2L.frameNStart = frameN  # exact frame index
            IA2L.tStart = t  # local t and not account for scr refresh
            IA2L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA2L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA2L.started')
            # update status
            IA2L.status = STARTED
            IA2L.setAutoDraw(True)
        
        # if IA2L is active this frame...
        if IA2L.status == STARTED:
            # update params
            pass
        
        # if IA2L is stopping this frame...
        if IA2L.status == STARTED:
            if frameN >= (IA2L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA2L.tStop = t  # not accounting for scr refresh
                IA2L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA2L.stopped')
                # update status
                IA2L.status = FINISHED
                IA2L.setAutoDraw(False)
        
        # *IA3L* updates
        
        # if IA3L is starting this frame...
        if IA3L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA3L.frameNStart = frameN  # exact frame index
            IA3L.tStart = t  # local t and not account for scr refresh
            IA3L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA3L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA3L.started')
            # update status
            IA3L.status = STARTED
            IA3L.setAutoDraw(True)
        
        # if IA3L is active this frame...
        if IA3L.status == STARTED:
            # update params
            pass
        
        # if IA3L is stopping this frame...
        if IA3L.status == STARTED:
            if frameN >= (IA3L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA3L.tStop = t  # not accounting for scr refresh
                IA3L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA3L.stopped')
                # update status
                IA3L.status = FINISHED
                IA3L.setAutoDraw(False)
        
        # *IA4L* updates
        
        # if IA4L is starting this frame...
        if IA4L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA4L.frameNStart = frameN  # exact frame index
            IA4L.tStart = t  # local t and not account for scr refresh
            IA4L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA4L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA4L.started')
            # update status
            IA4L.status = STARTED
            IA4L.setAutoDraw(True)
        
        # if IA4L is active this frame...
        if IA4L.status == STARTED:
            # update params
            pass
        
        # if IA4L is stopping this frame...
        if IA4L.status == STARTED:
            if frameN >= (IA4L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA4L.tStop = t  # not accounting for scr refresh
                IA4L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA4L.stopped')
                # update status
                IA4L.status = FINISHED
                IA4L.setAutoDraw(False)
        
        # *IA5L* updates
        
        # if IA5L is starting this frame...
        if IA5L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA5L.frameNStart = frameN  # exact frame index
            IA5L.tStart = t  # local t and not account for scr refresh
            IA5L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA5L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA5L.started')
            # update status
            IA5L.status = STARTED
            IA5L.setAutoDraw(True)
        
        # if IA5L is active this frame...
        if IA5L.status == STARTED:
            # update params
            pass
        
        # if IA5L is stopping this frame...
        if IA5L.status == STARTED:
            if frameN >= (IA5L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA5L.tStop = t  # not accounting for scr refresh
                IA5L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA5L.stopped')
                # update status
                IA5L.status = FINISHED
                IA5L.setAutoDraw(False)
        
        # *IA6L* updates
        
        # if IA6L is starting this frame...
        if IA6L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA6L.frameNStart = frameN  # exact frame index
            IA6L.tStart = t  # local t and not account for scr refresh
            IA6L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA6L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA6L.started')
            # update status
            IA6L.status = STARTED
            IA6L.setAutoDraw(True)
        
        # if IA6L is active this frame...
        if IA6L.status == STARTED:
            # update params
            pass
        
        # if IA6L is stopping this frame...
        if IA6L.status == STARTED:
            if frameN >= (IA6L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA6L.tStop = t  # not accounting for scr refresh
                IA6L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA6L.stopped')
                # update status
                IA6L.status = FINISHED
                IA6L.setAutoDraw(False)
        # Run 'Each Frame' code from CAL
        frame = frame + 1
        requirement = 200 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LA200msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LA200msL" ---
    for thisComponent in LA200msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LA200msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "BA2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CAB
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(2000 / FRate)
    frame = 0
    # keep track of which components have finished
    BA2000msComponents = [IA2000]
    for thisComponent in BA2000msComponents:
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
    
    # --- Run Routine "BA2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IA2000* updates
        
        # if IA2000 is starting this frame...
        if IA2000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA2000.frameNStart = frameN  # exact frame index
            IA2000.tStart = t  # local t and not account for scr refresh
            IA2000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA2000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA2000.started')
            # update status
            IA2000.status = STARTED
            IA2000.setAutoDraw(True)
        
        # if IA2000 is active this frame...
        if IA2000.status == STARTED:
            # update params
            pass
        
        # if IA2000 is stopping this frame...
        if IA2000.status == STARTED:
            if frameN >= (IA2000.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA2000.tStop = t  # not accounting for scr refresh
                IA2000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA2000.stopped')
                # update status
                IA2000.status = FINISHED
                IA2000.setAutoDraw(False)
        # Run 'Each Frame' code from CAB
        frame = frame + 1
        requirement = 2000 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BA2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BA2000ms" ---
    for thisComponent in BA2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BA2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FA2000msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    TAHedefL.setPos(pozisyonhedef)
    TAHedefL.setText(hedef)
    TACeldiriciL.setPos(pozisyonceldirici)
    TACeldiriciL.setText(celdirici)
    # keep track of which components have finished
    FA2000msLComponents = [IAFlankerBackgroundL, TAHedefL, TACeldiriciL]
    for thisComponent in FA2000msLComponents:
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
    
    # --- Run Routine "FA2000msL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IAFlankerBackgroundL* updates
        
        # if IAFlankerBackgroundL is starting this frame...
        if IAFlankerBackgroundL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IAFlankerBackgroundL.frameNStart = frameN  # exact frame index
            IAFlankerBackgroundL.tStart = t  # local t and not account for scr refresh
            IAFlankerBackgroundL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IAFlankerBackgroundL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IAFlankerBackgroundL.started')
            # update status
            IAFlankerBackgroundL.status = STARTED
            IAFlankerBackgroundL.setAutoDraw(True)
        
        # if IAFlankerBackgroundL is active this frame...
        if IAFlankerBackgroundL.status == STARTED:
            # update params
            pass
        
        # if IAFlankerBackgroundL is stopping this frame...
        if IAFlankerBackgroundL.status == STARTED:
            if frameN >= (IAFlankerBackgroundL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IAFlankerBackgroundL.tStop = t  # not accounting for scr refresh
                IAFlankerBackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IAFlankerBackgroundL.stopped')
                # update status
                IAFlankerBackgroundL.status = FINISHED
                IAFlankerBackgroundL.setAutoDraw(False)
        
        # *TAHedefL* updates
        
        # if TAHedefL is starting this frame...
        if TAHedefL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TAHedefL.frameNStart = frameN  # exact frame index
            TAHedefL.tStart = t  # local t and not account for scr refresh
            TAHedefL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TAHedefL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TAHedefL.started')
            # update status
            TAHedefL.status = STARTED
            TAHedefL.setAutoDraw(True)
        
        # if TAHedefL is active this frame...
        if TAHedefL.status == STARTED:
            # update params
            pass
        
        # if TAHedefL is stopping this frame...
        if TAHedefL.status == STARTED:
            if frameN >= (TAHedefL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TAHedefL.tStop = t  # not accounting for scr refresh
                TAHedefL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TAHedefL.stopped')
                # update status
                TAHedefL.status = FINISHED
                TAHedefL.setAutoDraw(False)
        
        # *TACeldiriciL* updates
        
        # if TACeldiriciL is starting this frame...
        if TACeldiriciL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TACeldiriciL.frameNStart = frameN  # exact frame index
            TACeldiriciL.tStart = t  # local t and not account for scr refresh
            TACeldiriciL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TACeldiriciL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TACeldiriciL.started')
            # update status
            TACeldiriciL.status = STARTED
            TACeldiriciL.setAutoDraw(True)
        
        # if TACeldiriciL is active this frame...
        if TACeldiriciL.status == STARTED:
            # update params
            pass
        
        # if TACeldiriciL is stopping this frame...
        if TACeldiriciL.status == STARTED:
            if frameN >= (TACeldiriciL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TACeldiriciL.tStop = t  # not accounting for scr refresh
                TACeldiriciL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TACeldiriciL.stopped')
                # update status
                TACeldiriciL.status = FINISHED
                TACeldiriciL.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FA2000msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FA2000msL" ---
    for thisComponent in FA2000msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "FA2000msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FA500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    KAFlankerR.keys = []
    KAFlankerR.rt = []
    _KAFlankerR_allKeys = []
    SAFlankerR.setSound('yanlis.wav', hamming=True)
    SAFlankerR.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CA500
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(500 / FRate)
    frame = 0
    # keep track of which components have finished
    FA500msComponents = [IA500, KAFlankerR, SAFlankerR]
    for thisComponent in FA500msComponents:
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
    
    # --- Run Routine "FA500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IA500* updates
        
        # if IA500 is starting this frame...
        if IA500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA500.frameNStart = frameN  # exact frame index
            IA500.tStart = t  # local t and not account for scr refresh
            IA500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA500.started')
            # update status
            IA500.status = STARTED
            IA500.setAutoDraw(True)
        
        # if IA500 is active this frame...
        if IA500.status == STARTED:
            # update params
            pass
        
        # if IA500 is stopping this frame...
        if IA500.status == STARTED:
            if frameN >= (IA500.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA500.tStop = t  # not accounting for scr refresh
                IA500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA500.stopped')
                # update status
                IA500.status = FINISHED
                IA500.setAutoDraw(False)
        
        # *KAFlankerR* updates
        waitOnFlip = False
        
        # if KAFlankerR is starting this frame...
        if KAFlankerR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            KAFlankerR.frameNStart = frameN  # exact frame index
            KAFlankerR.tStart = t  # local t and not account for scr refresh
            KAFlankerR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KAFlankerR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KAFlankerR.started')
            # update status
            KAFlankerR.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KAFlankerR.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KAFlankerR.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if KAFlankerR is stopping this frame...
        if KAFlankerR.status == STARTED:
            if frameN >= (KAFlankerR.frameNStart + FrameN):
                # keep track of stop time/frame for later
                KAFlankerR.tStop = t  # not accounting for scr refresh
                KAFlankerR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KAFlankerR.stopped')
                # update status
                KAFlankerR.status = FINISHED
                KAFlankerR.status = FINISHED
        if KAFlankerR.status == STARTED and not waitOnFlip:
            theseKeys = KAFlankerR.getKeys(keyList=['x','z'], waitRelease=False)
            _KAFlankerR_allKeys.extend(theseKeys)
            if len(_KAFlankerR_allKeys):
                KAFlankerR.keys = _KAFlankerR_allKeys[-1].name  # just the last key pressed
                KAFlankerR.rt = _KAFlankerR_allKeys[-1].rt
                # was this correct?
                if (KAFlankerR.keys == str(flankercevap)) or (KAFlankerR.keys == flankercevap):
                    KAFlankerR.corr = 1
                else:
                    KAFlankerR.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SAFlankerR
        # Run 'Each Frame' code from CA500
        frame = frame + 1
        requirement = 500 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FA500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FA500ms" ---
    for thisComponent in FA500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KAFlankerR.keys in ['', [], None]:  # No response was made
        KAFlankerR.keys = None
        # was no response the correct answer?!
        if str(flankercevap).lower() == 'none':
           KAFlankerR.corr = 1;  # correct non-response
        else:
           KAFlankerR.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopAlistirma (TrialHandler)
    LoopAlistirma.addData('KAFlankerR.keys',KAFlankerR.keys)
    LoopAlistirma.addData('KAFlankerR.corr', KAFlankerR.corr)
    if KAFlankerR.keys != None:  # we had a response
        LoopAlistirma.addData('KAFlankerR.rt', KAFlankerR.rt)
    SAFlankerR.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CA500
    if KAFlankerR.keys == None == 0:
        SAFlankerR.play()
    # the Routine "FA500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LAmsR" ---
    continueRoutine = True
    # update component parameters for each repeat
    IA1R.setColor([r1,g1,b1], colorSpace='rgb')
    IA2R.setColor([r2,g2,b2], colorSpace='rgb')
    IA3R.setColor([r3,g3,b3], colorSpace='rgb')
    IA4R.setColor([r4,g4,b4], colorSpace='rgb')
    IA5R.setColor([r5,g5,b5], colorSpace='rgb')
    IA6R.setColor([r6,g6,b6], colorSpace='rgb')
    # Run 'Begin Routine' code from CAR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(10000 / FRate)
    frame = 0
    
    if TCondition.text == "LL":
        IA5R.size = (0.053, 0.093)
        IA6R.size = (0.053, 0.093)
        
        if TLoadTask.text == "y":
            r5 = r5 + .5333
            g5 = g5 + .5333
            b5 = b5 + .5333
            
            r6 = r6 + .5333
            g6 = g6 + .5333
            b6 = b6 + .5333
            
            if r5 > .10000:
                p1 = .10000 - r5
                p2 = .5333 - p1
                p3 = .10000 - p2
                r5 = -p3
                
            if g5 > .10000:
                p1 = .10000 - g5
                p2 = .5333 - p1
                p3 = .10000 - p2
                g5 = -p3
                
            if b5 > .10000:
                p1 = .10000 - b5
                p2 = .5333 - p1
                p3 = .10000 - p2
                b5 = -p3
                
            if r6 > .10000:
                p1 = .10000 - r6
                p2 = .5333 - p1
                p3 = .10000 - p2
                r6 = -p3
                
            if g6 > .10000:
                p1 = .10000 - g6
                p2 = .5333 - p1
                p3 = .10000 - p2
                g6 = -p3
                
            if b6 > .10000:
                p1 = .10000 - b6
                p2 = .5333 - p1
                p3 = .10000 - p2
                b6 = -p3
    
    elif TCondition.text == "HL": 
        IA1R.size = (0.053, 0.093)
        IA2R.size = (0.053, 0.093)
        IA3R.size = (0.053, 0.093)
        IA4R.size = (0.053, 0.093)
        
        if TLoadTask.text == "y":
            r1 = r1 + .5333
            g1 = g1 + .5333
            b1 = b1 + .5333
            
            r2 = r2 + .5333
            g2 = g2 + .5333
            b2 = b2 + .5333
            
            r3 = r3 + .5333
            g3 = g3 + .5333
            b3 = b3 + .5333
            
            r4 = r4 + .5333
            g4 = g4 + .5333
            b4 = b4 + .5333
            
            if r1 > .10000:
                p1 = .10000 - r1
                p2 = .5333 - p1
                p3 = .10000 - p2
                r1 = -p3
                
            if g1 > .10000:
                p1 = .10000 - g1
                p2 = .5333 - p1
                p3 = .10000 - p2
                g1 = -p3
                
            if b1 > .10000:
                p1 = .10000 - b1
                p2 = .5333 - p1
                p3 = .10000 - p2
                b1 = -p3
                
            if r2 > .10000:
                p1 = .10000 - r2
                p2 = .5333 - p1
                p3 = .10000 - p2
                r2 = -p3
                
            if g2 > .10000:
                p1 = .10000 - g2
                p2 = .5333 - p1
                p3 = .10000 - p2
                g2 = -p3
                
            if b2 > .10000:
                p1 = .10000 - b2
                p2 = .5333 - p1
                p3 = .10000 - p2
                b2 = -p3
                
            if r3 > .10000:
                p1 = .10000 - r3
                p2 = .5333 - p1
                p3 = .10000 - p2
                r3 = -p3
                
            if g3 > .10000:
                p1 = .10000 - g3
                p2 = .5333 - p1
                p3 = .10000 - p2
                g3 = -p3
                
            if b3 > .10000:
                p1 = .10000 - b3
                p2 = .5333 - p1
                p3 = .10000 - p2
                b3 = -p3
                
                
            if r4 > .10000:
                p1 = .10000 - r4
                p2 = .5333 - p1
                p3 = .10000 - p2
                r4 = -p3
                
            if g4 > .10000:
                p1 = .10000 - g4
                p2 = .5333 - p1
                p3 = .10000 - p2
                g4 = -p3
                
            if b4 > .10000:
                p1 = .10000 - b4
                p2 = .5333 - p1
                p3 = .10000 - p2
                b4 = -p3
    
    elif TCondition.text == "LS": 
        IA5R.size = (0.053, 0.093)
        IA6R.size = (0.053, 0.093)
        
        if TLoadTask.text == "y":
            r5 = r5 + .1333
            g5 = g5 + .1333
            b5 = b5 + .1333
            
            r6 = r6 + .1333
            g6 = g6 + .1333
            b6 = b6 + .1333
            
            if r5 > .10000:
                p1 = .10000 - r5
                p2 = .1333 - p1
                p3 = .10000 - p2
                r5 = -p3
                
            if g5 > .10000:
                p1 = .10000 - g5
                p2 = .1333 - p1
                p3 = .10000 - p2
                g5 = -p3
                
            if b5 > .10000:
                p1 = .10000 - b5
                p2 = .1333 - p1
                p3 = .10000 - p2
                b5 = -p3
                
            if r6 > .10000:
                p1 = .10000 - r6
                p2 = .1333 - p1
                p3 = .10000 - p2
                r6 = -p3
                
            if g6 > .10000:
                p1 = .10000 - g6
                p2 = .1333 - p1
                p3 = .10000 - p2
                g6 = -p3
                
            if b6 > .10000:
                p1 = .10000 - b6
                p2 = .1333 - p1
                p3 = .10000 - p2
                b6 = -p3
    
    IA1R.setColor((r1,g1,b1))
    IA2R.setColor((r2,g2,b2))
    IA3R.setColor((r3,g3,b3))
    IA4R.setColor((r4,g4,b4))
    IA5R.setColor((r5,g5,b5))
    IA6R.setColor((r6,g6,b6))
    dfgfhdf.setText(int(r1))
    # keep track of which components have finished
    LAmsRComponents = [IALoadBackgroundR, IA1R, IA2R, IA3R, IA4R, IA5R, IA6R, dfgfhdf]
    for thisComponent in LAmsRComponents:
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
    
    # --- Run Routine "LAmsR" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IALoadBackgroundR* updates
        
        # if IALoadBackgroundR is starting this frame...
        if IALoadBackgroundR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IALoadBackgroundR.frameNStart = frameN  # exact frame index
            IALoadBackgroundR.tStart = t  # local t and not account for scr refresh
            IALoadBackgroundR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IALoadBackgroundR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IALoadBackgroundR.started')
            # update status
            IALoadBackgroundR.status = STARTED
            IALoadBackgroundR.setAutoDraw(True)
        
        # if IALoadBackgroundR is active this frame...
        if IALoadBackgroundR.status == STARTED:
            # update params
            pass
        
        # if IALoadBackgroundR is stopping this frame...
        if IALoadBackgroundR.status == STARTED:
            if frameN >= (IALoadBackgroundR.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IALoadBackgroundR.tStop = t  # not accounting for scr refresh
                IALoadBackgroundR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IALoadBackgroundR.stopped')
                # update status
                IALoadBackgroundR.status = FINISHED
                IALoadBackgroundR.setAutoDraw(False)
        
        # *IA1R* updates
        
        # if IA1R is starting this frame...
        if IA1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA1R.frameNStart = frameN  # exact frame index
            IA1R.tStart = t  # local t and not account for scr refresh
            IA1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA1R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA1R.started')
            # update status
            IA1R.status = STARTED
            IA1R.setAutoDraw(True)
        
        # if IA1R is active this frame...
        if IA1R.status == STARTED:
            # update params
            pass
        
        # if IA1R is stopping this frame...
        if IA1R.status == STARTED:
            if frameN >= (IA1R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA1R.tStop = t  # not accounting for scr refresh
                IA1R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA1R.stopped')
                # update status
                IA1R.status = FINISHED
                IA1R.setAutoDraw(False)
        
        # *IA2R* updates
        
        # if IA2R is starting this frame...
        if IA2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA2R.frameNStart = frameN  # exact frame index
            IA2R.tStart = t  # local t and not account for scr refresh
            IA2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA2R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA2R.started')
            # update status
            IA2R.status = STARTED
            IA2R.setAutoDraw(True)
        
        # if IA2R is active this frame...
        if IA2R.status == STARTED:
            # update params
            pass
        
        # if IA2R is stopping this frame...
        if IA2R.status == STARTED:
            if frameN >= (IA2R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA2R.tStop = t  # not accounting for scr refresh
                IA2R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA2R.stopped')
                # update status
                IA2R.status = FINISHED
                IA2R.setAutoDraw(False)
        
        # *IA3R* updates
        
        # if IA3R is starting this frame...
        if IA3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA3R.frameNStart = frameN  # exact frame index
            IA3R.tStart = t  # local t and not account for scr refresh
            IA3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA3R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA3R.started')
            # update status
            IA3R.status = STARTED
            IA3R.setAutoDraw(True)
        
        # if IA3R is active this frame...
        if IA3R.status == STARTED:
            # update params
            pass
        
        # if IA3R is stopping this frame...
        if IA3R.status == STARTED:
            if frameN >= (IA3R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA3R.tStop = t  # not accounting for scr refresh
                IA3R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA3R.stopped')
                # update status
                IA3R.status = FINISHED
                IA3R.setAutoDraw(False)
        
        # *IA4R* updates
        
        # if IA4R is starting this frame...
        if IA4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA4R.frameNStart = frameN  # exact frame index
            IA4R.tStart = t  # local t and not account for scr refresh
            IA4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA4R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA4R.started')
            # update status
            IA4R.status = STARTED
            IA4R.setAutoDraw(True)
        
        # if IA4R is active this frame...
        if IA4R.status == STARTED:
            # update params
            pass
        
        # if IA4R is stopping this frame...
        if IA4R.status == STARTED:
            if frameN >= (IA4R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA4R.tStop = t  # not accounting for scr refresh
                IA4R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA4R.stopped')
                # update status
                IA4R.status = FINISHED
                IA4R.setAutoDraw(False)
        
        # *IA5R* updates
        
        # if IA5R is starting this frame...
        if IA5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA5R.frameNStart = frameN  # exact frame index
            IA5R.tStart = t  # local t and not account for scr refresh
            IA5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA5R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA5R.started')
            # update status
            IA5R.status = STARTED
            IA5R.setAutoDraw(True)
        
        # if IA5R is active this frame...
        if IA5R.status == STARTED:
            # update params
            pass
        
        # if IA5R is stopping this frame...
        if IA5R.status == STARTED:
            if frameN >= (IA5R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA5R.tStop = t  # not accounting for scr refresh
                IA5R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA5R.stopped')
                # update status
                IA5R.status = FINISHED
                IA5R.setAutoDraw(False)
        
        # *IA6R* updates
        
        # if IA6R is starting this frame...
        if IA6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA6R.frameNStart = frameN  # exact frame index
            IA6R.tStart = t  # local t and not account for scr refresh
            IA6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA6R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA6R.started')
            # update status
            IA6R.status = STARTED
            IA6R.setAutoDraw(True)
        
        # if IA6R is active this frame...
        if IA6R.status == STARTED:
            # update params
            pass
        
        # if IA6R is stopping this frame...
        if IA6R.status == STARTED:
            if frameN >= (IA6R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA6R.tStop = t  # not accounting for scr refresh
                IA6R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA6R.stopped')
                # update status
                IA6R.status = FINISHED
                IA6R.setAutoDraw(False)
        # Run 'Each Frame' code from CAR
        frame = frame + 1
        requirement = 200 / FRate
        if frame >= requirement:
            continueRoutine = False
        
        # *dfgfhdf* updates
        
        # if dfgfhdf is starting this frame...
        if dfgfhdf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dfgfhdf.frameNStart = frameN  # exact frame index
            dfgfhdf.tStart = t  # local t and not account for scr refresh
            dfgfhdf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dfgfhdf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dfgfhdf.started')
            # update status
            dfgfhdf.status = STARTED
            dfgfhdf.setAutoDraw(True)
        
        # if dfgfhdf is active this frame...
        if dfgfhdf.status == STARTED:
            # update params
            pass
        
        # if dfgfhdf is stopping this frame...
        if dfgfhdf.status == STARTED:
            if frameN >= (dfgfhdf.frameNStart + FrameN):
                # keep track of stop time/frame for later
                dfgfhdf.tStop = t  # not accounting for scr refresh
                dfgfhdf.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dfgfhdf.stopped')
                # update status
                dfgfhdf.status = FINISHED
                dfgfhdf.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LAmsRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LAmsR" ---
    for thisComponent in LAmsRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LAmsR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LoopAlistirma'

# get names of stimulus parameters
if LoopAlistirma.trialList in ([], [None], None):
    params = []
else:
    params = LoopAlistirma.trialList[0].keys()
# save data for this loop
LoopAlistirma.saveAsExcel(filename + '.xlsx', sheetName='LoopAlistirma',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
