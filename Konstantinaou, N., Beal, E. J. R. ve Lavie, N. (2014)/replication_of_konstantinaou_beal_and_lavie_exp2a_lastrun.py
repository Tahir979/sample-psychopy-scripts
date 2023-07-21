#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on July 21, 2023, at 13:59
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
expName = 'replication_of_konstantinaou_beal_and_lavie_exp2a'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\wasd0\\Desktop\\Psychopy\\Konstantinaou, N., Beal, E. J. R. ve Lavie, N. (2013)\\replication_of_konstantinaou_beal_and_lavie_exp2a_lastrun.py',
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
    monitor='Tahir', color=[0,0,0], colorSpace='rgb',
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
    text='Çalışmamıza hoş geldiniz.\n\nBirazdan ekranınıza harf ya da harfler sunulacaktır. Sizden ekranda beliren harf ya da harf dizilerini konumlarına bakmaksızın ezberlemeniz beklenmektedir. Ardından bir çemberin içinde ve dışında bulunacak şekilde 2 harf (N ve Z) sunulacaktır. Sizden, çember içindeki harfi de aklınızda tutmanız beklenmektedir (N için 0, Z için 2 tuşuna basınız).\n\nBu sunumun gerçekleşmesinin ardından ilk olarak çemberin içindeki harfin ne olduğu, ardından da ilk ekranda belirmiş olan harfin, ilk ekranda harflerden herhangi birisi olup olmadığını cevaplamanız beklenmektedir (eğer harfi içeriyorsa S, içermiyorsa A tuşuna basınız).\n\nİlk 16 deneme alıştırma niteliğinde olup, 16. denemenin ardından deneye başlanacaktır.\n\nAlıştırma aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "CA500ms" ---
IA500 = visual.ImageStim(
    win=win,
    name='IA500', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from CA500
counter = 0

# --- Initialize components for Routine "LA500msL" ---
IALoadBackgroundL = visual.ImageStim(
    win=win,
    name='IALoadBackgroundL', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TALoadL = visual.TextStim(win=win, name='TALoadL',
    text='',
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
TABosL = visual.TextStim(win=win, name='TABosL',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, 0.375), height=0.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "CA2000ms" ---
IA2000 = visual.ImageStim(
    win=win,
    name='IA2000', units='norm', 
    image='blank.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "FA150msL" ---
IAFlankerBackgroundL = visual.ImageStim(
    win=win,
    name='IAFlankerBackgroundL', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TAHedefL = visual.TextStim(win=win, name='TAHedefL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.105, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TACeldiriciL = visual.TextStim(win=win, name='TACeldiriciL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "FA1850msR" ---
IA1850 = visual.ImageStim(
    win=win,
    name='IA1850', units='norm', 
    image='blank.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
KAFlankerR = keyboard.Keyboard()

# --- Initialize components for Routine "LA3000msR" ---
IALoadBackgroundR = visual.ImageStim(
    win=win,
    name='IALoadBackgroundR', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TA1R = visual.TextStim(win=win, name='TA1R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TA2R = visual.TextStim(win=win, name='TA2R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375,0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
TA3R = visual.TextStim(win=win, name='TA3R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
TA4R = visual.TextStim(win=win, name='TA4R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,-0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
TA5R = visual.TextStim(win=win, name='TA5R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
TA6R = visual.TextStim(win=win, name='TA6R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, 0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
TADYR = visual.TextStim(win=win, name='TADYR',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
KALoadR = keyboard.Keyboard()
SAFlankerR = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SAFlankerR')
SAFlankerR.setVolume(1.0)

# --- Initialize components for Routine "DeneyGecis" ---
KADGecis = keyboard.Keyboard()
TADGecis = visual.TextStim(win=win, name='TADGecis',
    text='Deney aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "CD500ms" ---
ID500 = visual.ImageStim(
    win=win,
    name='ID500', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "LD500msL" ---
IDLoadBackgroundL = visual.ImageStim(
    win=win,
    name='IDLoadBackgroundL', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TDLoadL = visual.TextStim(win=win, name='TDLoadL',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TD1L = visual.TextStim(win=win, name='TD1L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
TD2L = visual.TextStim(win=win, name='TD2L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375,0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
TD3L = visual.TextStim(win=win, name='TD3L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
TD4L = visual.TextStim(win=win, name='TD4L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,-0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
TD5L = visual.TextStim(win=win, name='TD5L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
TD6L = visual.TextStim(win=win, name='TD6L',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, 0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
TDBosL = visual.TextStim(win=win, name='TDBosL',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, 0.375), height=0.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "CD2000ms" ---
ID2000 = visual.ImageStim(
    win=win,
    name='ID2000', units='norm', 
    image='blank.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "FD150msL" ---
IDFlankerBackgroundL = visual.ImageStim(
    win=win,
    name='IDFlankerBackgroundL', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TDHedefL = visual.TextStim(win=win, name='TDHedefL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.105, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TdCeldiriciL = visual.TextStim(win=win, name='TdCeldiriciL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "FD1850msR" ---
ID1850 = visual.ImageStim(
    win=win,
    name='ID1850', units='norm', 
    image='blank.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
KDFlankerR = keyboard.Keyboard()

# --- Initialize components for Routine "LD3000msR" ---
IDLoadBackgroundR = visual.ImageStim(
    win=win,
    name='IDLoadBackgroundR', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
TD1R = visual.TextStim(win=win, name='TD1R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TD2R = visual.TextStim(win=win, name='TD2R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375,0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
TD3R = visual.TextStim(win=win, name='TD3R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
TD4R = visual.TextStim(win=win, name='TD4R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(0,-0.75), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
TD5R = visual.TextStim(win=win, name='TD5R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, -0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
TD6R = visual.TextStim(win=win, name='TD6R',
    text=None,
    font='Times New Roman',
    units='norm', pos=(-0.375, 0.375), height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
TDDYR = visual.TextStim(win=win, name='TDDYR',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
KDLoadR = keyboard.Keyboard()
SDFlankerR = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SDFlankerR')
SDFlankerR.setVolume(1.0)

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
LoopAlistirma = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('replication_of_konstantinaou_beal_and_lavie_exp2a.xlsx'),
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
    # keep track of which components have finished
    CA500msComponents = [IA500]
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
        
        # *IA500* updates
        
        # if IA500 is starting this frame...
        if IA500.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
                # keep track of stop time/frame for later
                IA500.tStop = t  # not accounting for scr refresh
                IA500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA500.stopped')
                # update status
                IA500.status = FINISHED
                IA500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    IALoadBackgroundL.setImage(pozisyonhedef)
    TALoadL.setText(yuk)
    TA1L.setText('')
    TA2L.setText('')
    TA3L.setText('')
    TA4L.setText('')
    TA5L.setText('')
    TA6L.setText('')
    TABosL.setText('')
    # Run 'Begin Routine' code from CALoadL
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
    
    shuffle(harfler)
    TABosL.text = harfler[0]
    harfler.pop(0)
    
    
    if TALoadL.text == "low":
        if IALoadBackgroundL.image == '1.png':
            TA1L.height = 0.18
        elif IALoadBackgroundL.image == '2.png':
            TA2L.height = 0.18
        elif IALoadBackgroundL.image == '3.png':
            TA3L.height = 0.18
        elif IALoadBackgroundL.image == '4.png':
            TA4L.height = 0.18
        elif IALoadBackgroundL.image == '5.png':
            TA5L.height = 0.18
        elif IALoadBackgroundL.image == '6.png':
            TA6L.height = 0.18
    
    else:
        TA1L.height = 0.18
        TA2L.height = 0.18
        TA3L.height = 0.18
        TA4L.height = 0.18
        TA5L.height = 0.18
        TA6L.height = 0.18
    # keep track of which components have finished
    LA500msLComponents = [IALoadBackgroundL, TALoadL, TA1L, TA2L, TA3L, TA4L, TA5L, TA6L, TABosL]
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
        
        # *IALoadBackgroundL* updates
        
        # if IALoadBackgroundL is starting this frame...
        if IALoadBackgroundL.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
                # keep track of stop time/frame for later
                IALoadBackgroundL.tStop = t  # not accounting for scr refresh
                IALoadBackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IALoadBackgroundL.stopped')
                # update status
                IALoadBackgroundL.status = FINISHED
                IALoadBackgroundL.setAutoDraw(False)
        
        # *TALoadL* updates
        
        # if TALoadL is starting this frame...
        if TALoadL.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
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
        if TA1L.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
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
        if TA2L.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
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
        if TA3L.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
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
        if TA4L.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
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
        if TA5L.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
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
        if TA6L.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 30:
                # keep track of stop time/frame for later
                TA6L.tStop = t  # not accounting for scr refresh
                TA6L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA6L.stopped')
                # update status
                TA6L.status = FINISHED
                TA6L.setAutoDraw(False)
        
        # *TABosL* updates
        
        # if TABosL is starting this frame...
        if TABosL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TABosL.frameNStart = frameN  # exact frame index
            TABosL.tStart = t  # local t and not account for scr refresh
            TABosL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TABosL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TABosL.started')
            # update status
            TABosL.status = STARTED
            TABosL.setAutoDraw(True)
        
        # if TABosL is active this frame...
        if TABosL.status == STARTED:
            # update params
            pass
        
        # if TABosL is stopping this frame...
        if TABosL.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TABosL.tStop = t  # not accounting for scr refresh
                TABosL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TABosL.stopped')
                # update status
                TABosL.status = FINISHED
                TABosL.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    
    # --- Prepare to start Routine "CA2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    CA2000msComponents = [IA2000]
    for thisComponent in CA2000msComponents:
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
    
    # --- Run Routine "CA2000ms" ---
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
        if IA2000.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 120:
                # keep track of stop time/frame for later
                IA2000.tStop = t  # not accounting for scr refresh
                IA2000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA2000.stopped')
                # update status
                IA2000.status = FINISHED
                IA2000.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CA2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CA2000ms" ---
    for thisComponent in CA2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "CA2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FA150msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IAFlankerBackgroundL.setImage(pozisyonhedef)
    TAHedefL.setPos(pozisyonharf)
    TAHedefL.setText(hedef)
    TACeldiriciL.setPos(pozisyonceldirici)
    TACeldiriciL.setText(celdirici)
    # keep track of which components have finished
    FA150msLComponents = [IAFlankerBackgroundL, TAHedefL, TACeldiriciL]
    for thisComponent in FA150msLComponents:
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
    
    # --- Run Routine "FA150msL" ---
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
        if IAFlankerBackgroundL.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 9:
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
        if TAHedefL.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 9:
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
        if TACeldiriciL.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 9:
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
        for thisComponent in FA150msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FA150msL" ---
    for thisComponent in FA150msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "FA150msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FA1850msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    KAFlankerR.keys = []
    KAFlankerR.rt = []
    _KAFlankerR_allKeys = []
    # keep track of which components have finished
    FA1850msRComponents = [IA1850, KAFlankerR]
    for thisComponent in FA1850msRComponents:
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
    
    # --- Run Routine "FA1850msR" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IA1850* updates
        
        # if IA1850 is starting this frame...
        if IA1850.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            IA1850.frameNStart = frameN  # exact frame index
            IA1850.tStart = t  # local t and not account for scr refresh
            IA1850.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA1850, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA1850.started')
            # update status
            IA1850.status = STARTED
            IA1850.setAutoDraw(True)
        
        # if IA1850 is active this frame...
        if IA1850.status == STARTED:
            # update params
            pass
        
        # if IA1850 is stopping this frame...
        if IA1850.status == STARTED:
            if frameN >= 111:
                # keep track of stop time/frame for later
                IA1850.tStop = t  # not accounting for scr refresh
                IA1850.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA1850.stopped')
                # update status
                IA1850.status = FINISHED
                IA1850.setAutoDraw(False)
        
        # *KAFlankerR* updates
        waitOnFlip = False
        
        # if KAFlankerR is starting this frame...
        if KAFlankerR.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 111:
                # keep track of stop time/frame for later
                KAFlankerR.tStop = t  # not accounting for scr refresh
                KAFlankerR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KAFlankerR.stopped')
                # update status
                KAFlankerR.status = FINISHED
                KAFlankerR.status = FINISHED
        if KAFlankerR.status == STARTED and not waitOnFlip:
            theseKeys = KAFlankerR.getKeys(keyList=['0','2'], waitRelease=False)
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FA1850msRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FA1850msR" ---
    for thisComponent in FA1850msRComponents:
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
    # the Routine "FA1850msR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LA3000msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    IALoadBackgroundR.setImage('1.png')
    TA1R.setText('')
    TA2R.setText('')
    TA3R.setText('')
    TA4R.setText('')
    TA5R.setText('')
    TA6R.setText('')
    TADYR.setText(taskcevap)
    KALoadR.keys = []
    KALoadR.rt = []
    _KALoadR_allKeys = []
    SAFlankerR.setSound('yanlis.wav', hamming=True)
    SAFlankerR.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CALoadR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(3000 / FRate)
    frame = 0
    
    TA1R.height = 0.00
    TA2R.height = 0.00
    TA3R.height = 0.00
    TA4R.height = 0.00
    TA5R.height = 0.00
    TA6R.height = 0.00
    
    dizi = [1,2,3,4,5,6]
    shuffle(dizi)
    deger = dizi[0]
    
    karistir = [TA1L.text,TA2L.text,TA3L.text,TA4L.text,TA5L.text,TA6L.text,]
    shuffle(karistir)
    harf = karistir[0]
    
    if deger == 1:
        if TADYR.text == "s":
            TA1R.height = 0.18
            TA1R.text = harf
            IALoadBackgroundR.image = '1.png'
        else:
            TA1R.height = 0.18
            TA1R.text = TABosL.text
            IALoadBackgroundR.image = '1.png'
    elif deger == 2:
        if TADYR.text == "s":
            TA2R.height = 0.18
            TA2R.text = harf
            IALoadBackgroundR.image = '2.png'
        else:
            TA2R.height = 0.18
            TA2R.text = TABosL.text
            IALoadBackgroundR.image = '2.png'
    elif deger == 3:
        if TADYR.text == "s":
            TA3R.height = 0.18
            TA3R.text = harf
            IALoadBackgroundR.image = '3.png'
        else:
            TA3R.height = 0.18
            TA3R.text = TABosL.text
            IALoadBackgroundR.image = '3.png'
    elif deger == 4:
        if TADYR.text == "s":
            TA4R.height = 0.18
            TA4R.text = harf
            IALoadBackgroundR.image = '4.png'
        else:
            TA4R.height = 0.18
            TA4R.text = TABosL.text
            IALoadBackgroundR.image = '4.png'
    elif deger ==5:
        if TADYR.text == "s":
            TA5R.height = 0.18
            TA5R.text = harf
            IALoadBackgroundR.image = '5.png'
        else:
            TA5R.height = 0.18
            TA5R.text = TABosL.text
            IALoadBackgroundR.image = '5.png'
    elif deger == 6:
        if TADYR.text == "s":
            TA6R.height = 0.18
            TA6R.text = harf
            IALoadBackgroundR.image = '6.png'
        else:
            TA6R.height = 0.18
            TA6R.text = TABosL.text
            IALoadBackgroundR.image = '6.png'
    # keep track of which components have finished
    LA3000msRComponents = [IALoadBackgroundR, TA1R, TA2R, TA3R, TA4R, TA5R, TA6R, TADYR, KALoadR, SAFlankerR]
    for thisComponent in LA3000msRComponents:
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
    
    # --- Run Routine "LA3000msR" ---
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
        if IALoadBackgroundR.status == NOT_STARTED and frameN >= 0:
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
            if frameN >= 180:
                # keep track of stop time/frame for later
                IALoadBackgroundR.tStop = t  # not accounting for scr refresh
                IALoadBackgroundR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IALoadBackgroundR.stopped')
                # update status
                IALoadBackgroundR.status = FINISHED
                IALoadBackgroundR.setAutoDraw(False)
        
        # *TA1R* updates
        
        # if TA1R is starting this frame...
        if TA1R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TA1R.frameNStart = frameN  # exact frame index
            TA1R.tStart = t  # local t and not account for scr refresh
            TA1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA1R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA1R.started')
            # update status
            TA1R.status = STARTED
            TA1R.setAutoDraw(True)
        
        # if TA1R is active this frame...
        if TA1R.status == STARTED:
            # update params
            pass
        
        # if TA1R is stopping this frame...
        if TA1R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TA1R.tStop = t  # not accounting for scr refresh
                TA1R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA1R.stopped')
                # update status
                TA1R.status = FINISHED
                TA1R.setAutoDraw(False)
        
        # *TA2R* updates
        
        # if TA2R is starting this frame...
        if TA2R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TA2R.frameNStart = frameN  # exact frame index
            TA2R.tStart = t  # local t and not account for scr refresh
            TA2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA2R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA2R.started')
            # update status
            TA2R.status = STARTED
            TA2R.setAutoDraw(True)
        
        # if TA2R is active this frame...
        if TA2R.status == STARTED:
            # update params
            pass
        
        # if TA2R is stopping this frame...
        if TA2R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TA2R.tStop = t  # not accounting for scr refresh
                TA2R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA2R.stopped')
                # update status
                TA2R.status = FINISHED
                TA2R.setAutoDraw(False)
        
        # *TA3R* updates
        
        # if TA3R is starting this frame...
        if TA3R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TA3R.frameNStart = frameN  # exact frame index
            TA3R.tStart = t  # local t and not account for scr refresh
            TA3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA3R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA3R.started')
            # update status
            TA3R.status = STARTED
            TA3R.setAutoDraw(True)
        
        # if TA3R is active this frame...
        if TA3R.status == STARTED:
            # update params
            pass
        
        # if TA3R is stopping this frame...
        if TA3R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TA3R.tStop = t  # not accounting for scr refresh
                TA3R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA3R.stopped')
                # update status
                TA3R.status = FINISHED
                TA3R.setAutoDraw(False)
        
        # *TA4R* updates
        
        # if TA4R is starting this frame...
        if TA4R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TA4R.frameNStart = frameN  # exact frame index
            TA4R.tStart = t  # local t and not account for scr refresh
            TA4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA4R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA4R.started')
            # update status
            TA4R.status = STARTED
            TA4R.setAutoDraw(True)
        
        # if TA4R is active this frame...
        if TA4R.status == STARTED:
            # update params
            pass
        
        # if TA4R is stopping this frame...
        if TA4R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TA4R.tStop = t  # not accounting for scr refresh
                TA4R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA4R.stopped')
                # update status
                TA4R.status = FINISHED
                TA4R.setAutoDraw(False)
        
        # *TA5R* updates
        
        # if TA5R is starting this frame...
        if TA5R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TA5R.frameNStart = frameN  # exact frame index
            TA5R.tStart = t  # local t and not account for scr refresh
            TA5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA5R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA5R.started')
            # update status
            TA5R.status = STARTED
            TA5R.setAutoDraw(True)
        
        # if TA5R is active this frame...
        if TA5R.status == STARTED:
            # update params
            pass
        
        # if TA5R is stopping this frame...
        if TA5R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TA5R.tStop = t  # not accounting for scr refresh
                TA5R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA5R.stopped')
                # update status
                TA5R.status = FINISHED
                TA5R.setAutoDraw(False)
        
        # *TA6R* updates
        
        # if TA6R is starting this frame...
        if TA6R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TA6R.frameNStart = frameN  # exact frame index
            TA6R.tStart = t  # local t and not account for scr refresh
            TA6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TA6R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TA6R.started')
            # update status
            TA6R.status = STARTED
            TA6R.setAutoDraw(True)
        
        # if TA6R is active this frame...
        if TA6R.status == STARTED:
            # update params
            pass
        
        # if TA6R is stopping this frame...
        if TA6R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TA6R.tStop = t  # not accounting for scr refresh
                TA6R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TA6R.stopped')
                # update status
                TA6R.status = FINISHED
                TA6R.setAutoDraw(False)
        
        # *TADYR* updates
        
        # if TADYR is starting this frame...
        if TADYR.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TADYR.frameNStart = frameN  # exact frame index
            TADYR.tStart = t  # local t and not account for scr refresh
            TADYR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TADYR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TADYR.started')
            # update status
            TADYR.status = STARTED
            TADYR.setAutoDraw(True)
        
        # if TADYR is active this frame...
        if TADYR.status == STARTED:
            # update params
            pass
        
        # if TADYR is stopping this frame...
        if TADYR.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TADYR.tStop = t  # not accounting for scr refresh
                TADYR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TADYR.stopped')
                # update status
                TADYR.status = FINISHED
                TADYR.setAutoDraw(False)
        
        # *KALoadR* updates
        waitOnFlip = False
        
        # if KALoadR is starting this frame...
        if KALoadR.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KALoadR.frameNStart = frameN  # exact frame index
            KALoadR.tStart = t  # local t and not account for scr refresh
            KALoadR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KALoadR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KALoadR.started')
            # update status
            KALoadR.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KALoadR.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KALoadR.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if KALoadR is stopping this frame...
        if KALoadR.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                KALoadR.tStop = t  # not accounting for scr refresh
                KALoadR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KALoadR.stopped')
                # update status
                KALoadR.status = FINISHED
                KALoadR.status = FINISHED
        if KALoadR.status == STARTED and not waitOnFlip:
            theseKeys = KALoadR.getKeys(keyList=['a','s'], waitRelease=False)
            _KALoadR_allKeys.extend(theseKeys)
            if len(_KALoadR_allKeys):
                KALoadR.keys = _KALoadR_allKeys[-1].name  # just the last key pressed
                KALoadR.rt = _KALoadR_allKeys[-1].rt
                # was this correct?
                if (KALoadR.keys == str(taskcevap)) or (KALoadR.keys == taskcevap):
                    KALoadR.corr = 1
                else:
                    KALoadR.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SAFlankerR
        # Run 'Each Frame' code from CALoadR
        frame = frame + 1
        requirement = 3000 / FRate
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
        for thisComponent in LA3000msRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LA3000msR" ---
    for thisComponent in LA3000msRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KALoadR.keys in ['', [], None]:  # No response was made
        KALoadR.keys = None
        # was no response the correct answer?!
        if str(taskcevap).lower() == 'none':
           KALoadR.corr = 1;  # correct non-response
        else:
           KALoadR.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopAlistirma (TrialHandler)
    LoopAlistirma.addData('KALoadR.keys',KALoadR.keys)
    LoopAlistirma.addData('KALoadR.corr', KALoadR.corr)
    if KALoadR.keys != None:  # we had a response
        LoopAlistirma.addData('KALoadR.rt', KALoadR.rt)
    SAFlankerR.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CALoadR
    if KALoadR.corr == 0:
        SAFlankerR.play()
        
    if counter == 16:
        LoopAlistirma.finished = True
    # the Routine "LA3000msR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LoopAlistirma'


# --- Prepare to start Routine "DeneyGecis" ---
continueRoutine = True
# update component parameters for each repeat
KADGecis.keys = []
KADGecis.rt = []
_KADGecis_allKeys = []
# keep track of which components have finished
DeneyGecisComponents = [KADGecis, TADGecis]
for thisComponent in DeneyGecisComponents:
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

# --- Run Routine "DeneyGecis" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *KADGecis* updates
    waitOnFlip = False
    
    # if KADGecis is starting this frame...
    if KADGecis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KADGecis.frameNStart = frameN  # exact frame index
        KADGecis.tStart = t  # local t and not account for scr refresh
        KADGecis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KADGecis, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KADGecis.started')
        # update status
        KADGecis.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KADGecis.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KADGecis.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KADGecis.status == STARTED and not waitOnFlip:
        theseKeys = KADGecis.getKeys(keyList=None, waitRelease=False)
        _KADGecis_allKeys.extend(theseKeys)
        if len(_KADGecis_allKeys):
            KADGecis.keys = _KADGecis_allKeys[-1].name  # just the last key pressed
            KADGecis.rt = _KADGecis_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *TADGecis* updates
    
    # if TADGecis is starting this frame...
    if TADGecis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TADGecis.frameNStart = frameN  # exact frame index
        TADGecis.tStart = t  # local t and not account for scr refresh
        TADGecis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TADGecis, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TADGecis.started')
        # update status
        TADGecis.status = STARTED
        TADGecis.setAutoDraw(True)
    
    # if TADGecis is active this frame...
    if TADGecis.status == STARTED:
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
    for thisComponent in DeneyGecisComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DeneyGecis" ---
for thisComponent in DeneyGecisComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KADGecis.keys in ['', [], None]:  # No response was made
    KADGecis.keys = None
thisExp.addData('KADGecis.keys',KADGecis.keys)
if KADGecis.keys != None:  # we had a response
    thisExp.addData('KADGecis.rt', KADGecis.rt)
thisExp.nextEntry()
# the Routine "DeneyGecis" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopDeney = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('replication_of_konstantinaou_beal_and_lavie_exp2a.xlsx'),
    seed=None, name='LoopDeney')
thisExp.addLoop(LoopDeney)  # add the loop to the experiment
thisLoopDeney = LoopDeney.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopDeney.rgb)
if thisLoopDeney != None:
    for paramName in thisLoopDeney:
        exec('{} = thisLoopDeney[paramName]'.format(paramName))

for thisLoopDeney in LoopDeney:
    currentLoop = LoopDeney
    # abbreviate parameter names if possible (e.g. rgb = thisLoopDeney.rgb)
    if thisLoopDeney != None:
        for paramName in thisLoopDeney:
            exec('{} = thisLoopDeney[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "CD500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    CD500msComponents = [ID500]
    for thisComponent in CD500msComponents:
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
    
    # --- Run Routine "CD500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ID500* updates
        
        # if ID500 is starting this frame...
        if ID500.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            ID500.frameNStart = frameN  # exact frame index
            ID500.tStart = t  # local t and not account for scr refresh
            ID500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID500.started')
            # update status
            ID500.status = STARTED
            ID500.setAutoDraw(True)
        
        # if ID500 is active this frame...
        if ID500.status == STARTED:
            # update params
            pass
        
        # if ID500 is stopping this frame...
        if ID500.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                ID500.tStop = t  # not accounting for scr refresh
                ID500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID500.stopped')
                # update status
                ID500.status = FINISHED
                ID500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CD500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CD500ms" ---
    for thisComponent in CD500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "CD500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LD500msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IDLoadBackgroundL.setImage(pozisyonhedef)
    TDLoadL.setText(yuk)
    TD1L.setText('')
    TD2L.setText('')
    TD3L.setText('')
    TD4L.setText('')
    TD5L.setText('')
    TD6L.setText('')
    TDBosL.setText('')
    # Run 'Begin Routine' code from CDLoadL
    YanitD = 0
    YanitY = 0
    
    TD1L.height = 0.00
    TD2L.height = 0.00
    TD3L.height = 0.00
    TD4L.height = 0.00
    TD5L.height = 0.00
    TD6L.height = 0.00
    
    harfler = ["F","H","K","L","M","T","V","W","Y","X"]
    shuffle(harfler)
    TD1L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TD2L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TD3L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TD4L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TD5L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TD6L.text = harfler[0]
    harfler.pop(0)
    
    shuffle(harfler)
    TDBosL.text = harfler[0]
    harfler.pop(0)
    
    
    if TDLoadL.text == "low":
        if IDLoadBackgroundL.image == '1.png':
            TD1L.height = 0.18
        elif IDLoadBackgroundL.image == '2.png':
            TD2L.height = 0.18
        elif IDLoadBackgroundL.image == '3.png':
            TD3L.height = 0.18
        elif IDLoadBackgroundL.image == '4.png':
            TD4L.height = 0.18
        elif IDLoadBackgroundL.image == '5.png':
            TD5L.height = 0.18
        elif IDLoadBackgroundL.image == '6.png':
            TD6L.height = 0.18
    
    else:
        TD1L.height = 0.18
        TD2L.height = 0.18
        TD3L.height = 0.18
        TD4L.height = 0.18
        TD5L.height = 0.18
        TD6L.height = 0.18
    # keep track of which components have finished
    LD500msLComponents = [IDLoadBackgroundL, TDLoadL, TD1L, TD2L, TD3L, TD4L, TD5L, TD6L, TDBosL]
    for thisComponent in LD500msLComponents:
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
    
    # --- Run Routine "LD500msL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IDLoadBackgroundL* updates
        
        # if IDLoadBackgroundL is starting this frame...
        if IDLoadBackgroundL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            IDLoadBackgroundL.frameNStart = frameN  # exact frame index
            IDLoadBackgroundL.tStart = t  # local t and not account for scr refresh
            IDLoadBackgroundL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IDLoadBackgroundL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IDLoadBackgroundL.started')
            # update status
            IDLoadBackgroundL.status = STARTED
            IDLoadBackgroundL.setAutoDraw(True)
        
        # if IDLoadBackgroundL is active this frame...
        if IDLoadBackgroundL.status == STARTED:
            # update params
            pass
        
        # if IDLoadBackgroundL is stopping this frame...
        if IDLoadBackgroundL.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                IDLoadBackgroundL.tStop = t  # not accounting for scr refresh
                IDLoadBackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IDLoadBackgroundL.stopped')
                # update status
                IDLoadBackgroundL.status = FINISHED
                IDLoadBackgroundL.setAutoDraw(False)
        
        # *TDLoadL* updates
        
        # if TDLoadL is starting this frame...
        if TDLoadL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TDLoadL.frameNStart = frameN  # exact frame index
            TDLoadL.tStart = t  # local t and not account for scr refresh
            TDLoadL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDLoadL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDLoadL.started')
            # update status
            TDLoadL.status = STARTED
            TDLoadL.setAutoDraw(True)
        
        # if TDLoadL is active this frame...
        if TDLoadL.status == STARTED:
            # update params
            pass
        
        # if TDLoadL is stopping this frame...
        if TDLoadL.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TDLoadL.tStop = t  # not accounting for scr refresh
                TDLoadL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDLoadL.stopped')
                # update status
                TDLoadL.status = FINISHED
                TDLoadL.setAutoDraw(False)
        
        # *TD1L* updates
        
        # if TD1L is starting this frame...
        if TD1L.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD1L.frameNStart = frameN  # exact frame index
            TD1L.tStart = t  # local t and not account for scr refresh
            TD1L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD1L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD1L.started')
            # update status
            TD1L.status = STARTED
            TD1L.setAutoDraw(True)
        
        # if TD1L is active this frame...
        if TD1L.status == STARTED:
            # update params
            pass
        
        # if TD1L is stopping this frame...
        if TD1L.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TD1L.tStop = t  # not accounting for scr refresh
                TD1L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD1L.stopped')
                # update status
                TD1L.status = FINISHED
                TD1L.setAutoDraw(False)
        
        # *TD2L* updates
        
        # if TD2L is starting this frame...
        if TD2L.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD2L.frameNStart = frameN  # exact frame index
            TD2L.tStart = t  # local t and not account for scr refresh
            TD2L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD2L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD2L.started')
            # update status
            TD2L.status = STARTED
            TD2L.setAutoDraw(True)
        
        # if TD2L is active this frame...
        if TD2L.status == STARTED:
            # update params
            pass
        
        # if TD2L is stopping this frame...
        if TD2L.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TD2L.tStop = t  # not accounting for scr refresh
                TD2L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD2L.stopped')
                # update status
                TD2L.status = FINISHED
                TD2L.setAutoDraw(False)
        
        # *TD3L* updates
        
        # if TD3L is starting this frame...
        if TD3L.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD3L.frameNStart = frameN  # exact frame index
            TD3L.tStart = t  # local t and not account for scr refresh
            TD3L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD3L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD3L.started')
            # update status
            TD3L.status = STARTED
            TD3L.setAutoDraw(True)
        
        # if TD3L is active this frame...
        if TD3L.status == STARTED:
            # update params
            pass
        
        # if TD3L is stopping this frame...
        if TD3L.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TD3L.tStop = t  # not accounting for scr refresh
                TD3L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD3L.stopped')
                # update status
                TD3L.status = FINISHED
                TD3L.setAutoDraw(False)
        
        # *TD4L* updates
        
        # if TD4L is starting this frame...
        if TD4L.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD4L.frameNStart = frameN  # exact frame index
            TD4L.tStart = t  # local t and not account for scr refresh
            TD4L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD4L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD4L.started')
            # update status
            TD4L.status = STARTED
            TD4L.setAutoDraw(True)
        
        # if TD4L is active this frame...
        if TD4L.status == STARTED:
            # update params
            pass
        
        # if TD4L is stopping this frame...
        if TD4L.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TD4L.tStop = t  # not accounting for scr refresh
                TD4L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD4L.stopped')
                # update status
                TD4L.status = FINISHED
                TD4L.setAutoDraw(False)
        
        # *TD5L* updates
        
        # if TD5L is starting this frame...
        if TD5L.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD5L.frameNStart = frameN  # exact frame index
            TD5L.tStart = t  # local t and not account for scr refresh
            TD5L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD5L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD5L.started')
            # update status
            TD5L.status = STARTED
            TD5L.setAutoDraw(True)
        
        # if TD5L is active this frame...
        if TD5L.status == STARTED:
            # update params
            pass
        
        # if TD5L is stopping this frame...
        if TD5L.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TD5L.tStop = t  # not accounting for scr refresh
                TD5L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD5L.stopped')
                # update status
                TD5L.status = FINISHED
                TD5L.setAutoDraw(False)
        
        # *TD6L* updates
        
        # if TD6L is starting this frame...
        if TD6L.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD6L.frameNStart = frameN  # exact frame index
            TD6L.tStart = t  # local t and not account for scr refresh
            TD6L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD6L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD6L.started')
            # update status
            TD6L.status = STARTED
            TD6L.setAutoDraw(True)
        
        # if TD6L is active this frame...
        if TD6L.status == STARTED:
            # update params
            pass
        
        # if TD6L is stopping this frame...
        if TD6L.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TD6L.tStop = t  # not accounting for scr refresh
                TD6L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD6L.stopped')
                # update status
                TD6L.status = FINISHED
                TD6L.setAutoDraw(False)
        
        # *TDBosL* updates
        
        # if TDBosL is starting this frame...
        if TDBosL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TDBosL.frameNStart = frameN  # exact frame index
            TDBosL.tStart = t  # local t and not account for scr refresh
            TDBosL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDBosL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDBosL.started')
            # update status
            TDBosL.status = STARTED
            TDBosL.setAutoDraw(True)
        
        # if TDBosL is active this frame...
        if TDBosL.status == STARTED:
            # update params
            pass
        
        # if TDBosL is stopping this frame...
        if TDBosL.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                TDBosL.tStop = t  # not accounting for scr refresh
                TDBosL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDBosL.stopped')
                # update status
                TDBosL.status = FINISHED
                TDBosL.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LD500msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LD500msL" ---
    for thisComponent in LD500msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LD500msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "CD2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    CD2000msComponents = [ID2000]
    for thisComponent in CD2000msComponents:
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
    
    # --- Run Routine "CD2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ID2000* updates
        
        # if ID2000 is starting this frame...
        if ID2000.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            ID2000.frameNStart = frameN  # exact frame index
            ID2000.tStart = t  # local t and not account for scr refresh
            ID2000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID2000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID2000.started')
            # update status
            ID2000.status = STARTED
            ID2000.setAutoDraw(True)
        
        # if ID2000 is active this frame...
        if ID2000.status == STARTED:
            # update params
            pass
        
        # if ID2000 is stopping this frame...
        if ID2000.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                ID2000.tStop = t  # not accounting for scr refresh
                ID2000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID2000.stopped')
                # update status
                ID2000.status = FINISHED
                ID2000.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CD2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CD2000ms" ---
    for thisComponent in CD2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "CD2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FD150msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IDFlankerBackgroundL.setImage(pozisyonhedef)
    TDHedefL.setPos(pozisyonharf)
    TDHedefL.setText(hedef)
    TdCeldiriciL.setPos(pozisyonceldirici)
    TdCeldiriciL.setText(celdirici)
    # keep track of which components have finished
    FD150msLComponents = [IDFlankerBackgroundL, TDHedefL, TdCeldiriciL]
    for thisComponent in FD150msLComponents:
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
    
    # --- Run Routine "FD150msL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IDFlankerBackgroundL* updates
        
        # if IDFlankerBackgroundL is starting this frame...
        if IDFlankerBackgroundL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            IDFlankerBackgroundL.frameNStart = frameN  # exact frame index
            IDFlankerBackgroundL.tStart = t  # local t and not account for scr refresh
            IDFlankerBackgroundL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IDFlankerBackgroundL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IDFlankerBackgroundL.started')
            # update status
            IDFlankerBackgroundL.status = STARTED
            IDFlankerBackgroundL.setAutoDraw(True)
        
        # if IDFlankerBackgroundL is active this frame...
        if IDFlankerBackgroundL.status == STARTED:
            # update params
            pass
        
        # if IDFlankerBackgroundL is stopping this frame...
        if IDFlankerBackgroundL.status == STARTED:
            if frameN >= 9:
                # keep track of stop time/frame for later
                IDFlankerBackgroundL.tStop = t  # not accounting for scr refresh
                IDFlankerBackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IDFlankerBackgroundL.stopped')
                # update status
                IDFlankerBackgroundL.status = FINISHED
                IDFlankerBackgroundL.setAutoDraw(False)
        
        # *TDHedefL* updates
        
        # if TDHedefL is starting this frame...
        if TDHedefL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TDHedefL.frameNStart = frameN  # exact frame index
            TDHedefL.tStart = t  # local t and not account for scr refresh
            TDHedefL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDHedefL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDHedefL.started')
            # update status
            TDHedefL.status = STARTED
            TDHedefL.setAutoDraw(True)
        
        # if TDHedefL is active this frame...
        if TDHedefL.status == STARTED:
            # update params
            pass
        
        # if TDHedefL is stopping this frame...
        if TDHedefL.status == STARTED:
            if frameN >= 9:
                # keep track of stop time/frame for later
                TDHedefL.tStop = t  # not accounting for scr refresh
                TDHedefL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDHedefL.stopped')
                # update status
                TDHedefL.status = FINISHED
                TDHedefL.setAutoDraw(False)
        
        # *TdCeldiriciL* updates
        
        # if TdCeldiriciL is starting this frame...
        if TdCeldiriciL.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TdCeldiriciL.frameNStart = frameN  # exact frame index
            TdCeldiriciL.tStart = t  # local t and not account for scr refresh
            TdCeldiriciL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TdCeldiriciL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TdCeldiriciL.started')
            # update status
            TdCeldiriciL.status = STARTED
            TdCeldiriciL.setAutoDraw(True)
        
        # if TdCeldiriciL is active this frame...
        if TdCeldiriciL.status == STARTED:
            # update params
            pass
        
        # if TdCeldiriciL is stopping this frame...
        if TdCeldiriciL.status == STARTED:
            if frameN >= 9:
                # keep track of stop time/frame for later
                TdCeldiriciL.tStop = t  # not accounting for scr refresh
                TdCeldiriciL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TdCeldiriciL.stopped')
                # update status
                TdCeldiriciL.status = FINISHED
                TdCeldiriciL.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FD150msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FD150msL" ---
    for thisComponent in FD150msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "FD150msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FD1850msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    KDFlankerR.keys = []
    KDFlankerR.rt = []
    _KDFlankerR_allKeys = []
    # keep track of which components have finished
    FD1850msRComponents = [ID1850, KDFlankerR]
    for thisComponent in FD1850msRComponents:
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
    
    # --- Run Routine "FD1850msR" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ID1850* updates
        
        # if ID1850 is starting this frame...
        if ID1850.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            ID1850.frameNStart = frameN  # exact frame index
            ID1850.tStart = t  # local t and not account for scr refresh
            ID1850.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID1850, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID1850.started')
            # update status
            ID1850.status = STARTED
            ID1850.setAutoDraw(True)
        
        # if ID1850 is active this frame...
        if ID1850.status == STARTED:
            # update params
            pass
        
        # if ID1850 is stopping this frame...
        if ID1850.status == STARTED:
            if frameN >= 111:
                # keep track of stop time/frame for later
                ID1850.tStop = t  # not accounting for scr refresh
                ID1850.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID1850.stopped')
                # update status
                ID1850.status = FINISHED
                ID1850.setAutoDraw(False)
        
        # *KDFlankerR* updates
        waitOnFlip = False
        
        # if KDFlankerR is starting this frame...
        if KDFlankerR.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KDFlankerR.frameNStart = frameN  # exact frame index
            KDFlankerR.tStart = t  # local t and not account for scr refresh
            KDFlankerR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KDFlankerR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KDFlankerR.started')
            # update status
            KDFlankerR.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KDFlankerR.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KDFlankerR.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if KDFlankerR is stopping this frame...
        if KDFlankerR.status == STARTED:
            if frameN >= 111:
                # keep track of stop time/frame for later
                KDFlankerR.tStop = t  # not accounting for scr refresh
                KDFlankerR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KDFlankerR.stopped')
                # update status
                KDFlankerR.status = FINISHED
                KDFlankerR.status = FINISHED
        if KDFlankerR.status == STARTED and not waitOnFlip:
            theseKeys = KDFlankerR.getKeys(keyList=['0','2'], waitRelease=False)
            _KDFlankerR_allKeys.extend(theseKeys)
            if len(_KDFlankerR_allKeys):
                KDFlankerR.keys = _KDFlankerR_allKeys[-1].name  # just the last key pressed
                KDFlankerR.rt = _KDFlankerR_allKeys[-1].rt
                # was this correct?
                if (KDFlankerR.keys == str(flankercevap)) or (KDFlankerR.keys == flankercevap):
                    KDFlankerR.corr = 1
                else:
                    KDFlankerR.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FD1850msRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FD1850msR" ---
    for thisComponent in FD1850msRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KDFlankerR.keys in ['', [], None]:  # No response was made
        KDFlankerR.keys = None
        # was no response the correct answer?!
        if str(flankercevap).lower() == 'none':
           KDFlankerR.corr = 1;  # correct non-response
        else:
           KDFlankerR.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopDeney (TrialHandler)
    LoopDeney.addData('KDFlankerR.keys',KDFlankerR.keys)
    LoopDeney.addData('KDFlankerR.corr', KDFlankerR.corr)
    if KDFlankerR.keys != None:  # we had a response
        LoopDeney.addData('KDFlankerR.rt', KDFlankerR.rt)
    # the Routine "FD1850msR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LD3000msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    IDLoadBackgroundR.setImage('1.png')
    TD1R.setText('')
    TD2R.setText('')
    TD3R.setText('')
    TD4R.setText('')
    TD5R.setText('')
    TD6R.setText('')
    TDDYR.setText(taskcevap)
    KDLoadR.keys = []
    KDLoadR.rt = []
    _KDLoadR_allKeys = []
    SDFlankerR.setSound('yanlis.wav', hamming=True)
    SDFlankerR.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CDLoadR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(3000 / FRate)
    frame = 0
    
    TD1R.height = 0.00
    TD2R.height = 0.00
    TD3R.height = 0.00
    TD4R.height = 0.00
    TD5R.height = 0.00
    TD6R.height = 0.00
    
    dizi = [1,2,3,4,5,6]
    shuffle(dizi)
    deger = dizi[0]
    
    karistir = [TD1L.text,TD2L.text,TD3L.text,TD4L.text,TD5L.text,TD6L.text,]
    shuffle(karistir)
    harf = karistir[0]
    
    if deger == 1:
        if TDDYR.text == "s":
            TD1R.height = 0.18
            TD1R.text = harf
            IDLoadBackgroundR.image = '1.png'
        else:
            TD1R.height = 0.18
            TD1R.text = TABosL.text
            IDLoadBackgroundR.image = '1.png'
    elif deger == 2:
        if TDDYR.text == "s":
            TD2R.height = 0.18
            TD2R.text = harf
            IDLoadBackgroundR.image = '2.png'
        else:
            TD2R.height = 0.18
            TD2R.text = TABosL.text
            IDLoadBackgroundR.image = '2.png'
    elif deger == 3:
        if TDDYR.text == "s":
            TD3R.height = 0.18
            TD3R.text = harf
            IDLoadBackgroundR.image = '3.png'
        else:
            TD3R.height = 0.18
            TD3R.text = TABosL.text
            IDLoadBackgroundR.image = '3.png'
    elif deger == 4:
        if TDDYR.text == "s":
            TD4R.height = 0.18
            TD4R.text = harf
            IDLoadBackgroundR.image = '4.png'
        else:
            TD4R.height = 0.18
            TD4R.text = TABosL.text
            IDLoadBackgroundR.image = '4.png'
    elif deger ==5:
        if TDDYR.text == "s":
            TD5R.height = 0.18
            TD5R.text = harf
            IDLoadBackgroundR.image = '5.png'
        else:
            TD5R.height = 0.18
            TD5R.text = TABosL.text
            IDLoadBackgroundR.image = '5.png'
    elif deger == 6:
        if TDDYR.text == "s":
            TD6R.height = 0.18
            TD6R.text = harf
            IDLoadBackgroundR.image = '6.png'
        else:
            TD6R.height = 0.18
            TD6R.text = TABosL.text
            IDLoadBackgroundR.image = '6.png'
    # keep track of which components have finished
    LD3000msRComponents = [IDLoadBackgroundR, TD1R, TD2R, TD3R, TD4R, TD5R, TD6R, TDDYR, KDLoadR, SDFlankerR]
    for thisComponent in LD3000msRComponents:
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
    
    # --- Run Routine "LD3000msR" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IDLoadBackgroundR* updates
        
        # if IDLoadBackgroundR is starting this frame...
        if IDLoadBackgroundR.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            IDLoadBackgroundR.frameNStart = frameN  # exact frame index
            IDLoadBackgroundR.tStart = t  # local t and not account for scr refresh
            IDLoadBackgroundR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IDLoadBackgroundR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IDLoadBackgroundR.started')
            # update status
            IDLoadBackgroundR.status = STARTED
            IDLoadBackgroundR.setAutoDraw(True)
        
        # if IDLoadBackgroundR is active this frame...
        if IDLoadBackgroundR.status == STARTED:
            # update params
            pass
        
        # if IDLoadBackgroundR is stopping this frame...
        if IDLoadBackgroundR.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                IDLoadBackgroundR.tStop = t  # not accounting for scr refresh
                IDLoadBackgroundR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IDLoadBackgroundR.stopped')
                # update status
                IDLoadBackgroundR.status = FINISHED
                IDLoadBackgroundR.setAutoDraw(False)
        
        # *TD1R* updates
        
        # if TD1R is starting this frame...
        if TD1R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD1R.frameNStart = frameN  # exact frame index
            TD1R.tStart = t  # local t and not account for scr refresh
            TD1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD1R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD1R.started')
            # update status
            TD1R.status = STARTED
            TD1R.setAutoDraw(True)
        
        # if TD1R is active this frame...
        if TD1R.status == STARTED:
            # update params
            pass
        
        # if TD1R is stopping this frame...
        if TD1R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TD1R.tStop = t  # not accounting for scr refresh
                TD1R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD1R.stopped')
                # update status
                TD1R.status = FINISHED
                TD1R.setAutoDraw(False)
        
        # *TD2R* updates
        
        # if TD2R is starting this frame...
        if TD2R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD2R.frameNStart = frameN  # exact frame index
            TD2R.tStart = t  # local t and not account for scr refresh
            TD2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD2R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD2R.started')
            # update status
            TD2R.status = STARTED
            TD2R.setAutoDraw(True)
        
        # if TD2R is active this frame...
        if TD2R.status == STARTED:
            # update params
            pass
        
        # if TD2R is stopping this frame...
        if TD2R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TD2R.tStop = t  # not accounting for scr refresh
                TD2R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD2R.stopped')
                # update status
                TD2R.status = FINISHED
                TD2R.setAutoDraw(False)
        
        # *TD3R* updates
        
        # if TD3R is starting this frame...
        if TD3R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD3R.frameNStart = frameN  # exact frame index
            TD3R.tStart = t  # local t and not account for scr refresh
            TD3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD3R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD3R.started')
            # update status
            TD3R.status = STARTED
            TD3R.setAutoDraw(True)
        
        # if TD3R is active this frame...
        if TD3R.status == STARTED:
            # update params
            pass
        
        # if TD3R is stopping this frame...
        if TD3R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TD3R.tStop = t  # not accounting for scr refresh
                TD3R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD3R.stopped')
                # update status
                TD3R.status = FINISHED
                TD3R.setAutoDraw(False)
        
        # *TD4R* updates
        
        # if TD4R is starting this frame...
        if TD4R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD4R.frameNStart = frameN  # exact frame index
            TD4R.tStart = t  # local t and not account for scr refresh
            TD4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD4R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD4R.started')
            # update status
            TD4R.status = STARTED
            TD4R.setAutoDraw(True)
        
        # if TD4R is active this frame...
        if TD4R.status == STARTED:
            # update params
            pass
        
        # if TD4R is stopping this frame...
        if TD4R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TD4R.tStop = t  # not accounting for scr refresh
                TD4R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD4R.stopped')
                # update status
                TD4R.status = FINISHED
                TD4R.setAutoDraw(False)
        
        # *TD5R* updates
        
        # if TD5R is starting this frame...
        if TD5R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD5R.frameNStart = frameN  # exact frame index
            TD5R.tStart = t  # local t and not account for scr refresh
            TD5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD5R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD5R.started')
            # update status
            TD5R.status = STARTED
            TD5R.setAutoDraw(True)
        
        # if TD5R is active this frame...
        if TD5R.status == STARTED:
            # update params
            pass
        
        # if TD5R is stopping this frame...
        if TD5R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TD5R.tStop = t  # not accounting for scr refresh
                TD5R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD5R.stopped')
                # update status
                TD5R.status = FINISHED
                TD5R.setAutoDraw(False)
        
        # *TD6R* updates
        
        # if TD6R is starting this frame...
        if TD6R.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TD6R.frameNStart = frameN  # exact frame index
            TD6R.tStart = t  # local t and not account for scr refresh
            TD6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TD6R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TD6R.started')
            # update status
            TD6R.status = STARTED
            TD6R.setAutoDraw(True)
        
        # if TD6R is active this frame...
        if TD6R.status == STARTED:
            # update params
            pass
        
        # if TD6R is stopping this frame...
        if TD6R.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TD6R.tStop = t  # not accounting for scr refresh
                TD6R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TD6R.stopped')
                # update status
                TD6R.status = FINISHED
                TD6R.setAutoDraw(False)
        
        # *TDDYR* updates
        
        # if TDDYR is starting this frame...
        if TDDYR.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            TDDYR.frameNStart = frameN  # exact frame index
            TDDYR.tStart = t  # local t and not account for scr refresh
            TDDYR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDDYR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDDYR.started')
            # update status
            TDDYR.status = STARTED
            TDDYR.setAutoDraw(True)
        
        # if TDDYR is active this frame...
        if TDDYR.status == STARTED:
            # update params
            pass
        
        # if TDDYR is stopping this frame...
        if TDDYR.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                TDDYR.tStop = t  # not accounting for scr refresh
                TDDYR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDDYR.stopped')
                # update status
                TDDYR.status = FINISHED
                TDDYR.setAutoDraw(False)
        
        # *KDLoadR* updates
        waitOnFlip = False
        
        # if KDLoadR is starting this frame...
        if KDLoadR.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KDLoadR.frameNStart = frameN  # exact frame index
            KDLoadR.tStart = t  # local t and not account for scr refresh
            KDLoadR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KDLoadR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KDLoadR.started')
            # update status
            KDLoadR.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KDLoadR.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KDLoadR.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if KDLoadR is stopping this frame...
        if KDLoadR.status == STARTED:
            if frameN >= 180:
                # keep track of stop time/frame for later
                KDLoadR.tStop = t  # not accounting for scr refresh
                KDLoadR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KDLoadR.stopped')
                # update status
                KDLoadR.status = FINISHED
                KDLoadR.status = FINISHED
        if KDLoadR.status == STARTED and not waitOnFlip:
            theseKeys = KDLoadR.getKeys(keyList=['a','s'], waitRelease=False)
            _KDLoadR_allKeys.extend(theseKeys)
            if len(_KDLoadR_allKeys):
                KDLoadR.keys = _KDLoadR_allKeys[-1].name  # just the last key pressed
                KDLoadR.rt = _KDLoadR_allKeys[-1].rt
                # was this correct?
                if (KDLoadR.keys == str(taskcevap)) or (KDLoadR.keys == taskcevap):
                    KDLoadR.corr = 1
                else:
                    KDLoadR.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SDFlankerR
        # Run 'Each Frame' code from CDLoadR
        frame = frame + 1
        requirement = 3000 / FRate
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
        for thisComponent in LD3000msRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LD3000msR" ---
    for thisComponent in LD3000msRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KDLoadR.keys in ['', [], None]:  # No response was made
        KDLoadR.keys = None
        # was no response the correct answer?!
        if str(taskcevap).lower() == 'none':
           KDLoadR.corr = 1;  # correct non-response
        else:
           KDLoadR.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopDeney (TrialHandler)
    LoopDeney.addData('KDLoadR.keys',KDLoadR.keys)
    LoopDeney.addData('KDLoadR.corr', KDLoadR.corr)
    if KDLoadR.keys != None:  # we had a response
        LoopDeney.addData('KDLoadR.rt', KDLoadR.rt)
    SDFlankerR.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CDLoadR
    if KDLoadR.corr == 0:
        SDFlankerR.play()
    # the Routine "LD3000msR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LoopDeney'


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
