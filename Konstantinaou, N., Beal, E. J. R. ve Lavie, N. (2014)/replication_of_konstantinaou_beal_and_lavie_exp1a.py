#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on May 08, 2023, at 05:42
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
expName = 'melikevize'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\wasd0\\Desktop\\melikevize\\deney1a.py',
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

# --- Initialize components for Routine "Yonerge" ---
KAYonerge = keyboard.Keyboard()
TAYonerge = visual.TextStim(win=win, name='TAYonerge',
    text='Çalışmamıza hoş geldiniz.\n\nBirazdan ekranınıza kutucuk / kutucuklar içinde bazı renkler, ve, noktalardan oluşan bir çemberin içinde ve dışında bulunacak şekilde 2 harf (X ve Z) sunulacaktır. Sizden, ekranınıza gelen kutucukların renk ve konum bilgileriyle beraber, çember içindeki harfi de aklınızda tutmanız beklenmektedir. \n\nBu sunumun gerçekleşmesinin ardından ilk olarak çemberin içindeki harfin ne olduğu, ardından da ilk ekranda belirmiş olan pozisyondaki kutucuklardan bir tanesi sunularak renk ve konum bilgisinin doğru olup olmadığını cevaplamanız beklenmektedir.\n\nİlk 16 deneme alıştırma niteliğinde olup, 16. denemenin ardından deneye başlanacaktır.\n\nAlıştırma aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "CA1000ms" ---
PA1000 = visual.ShapeStim(
    win=win, name='PA1000', vertices='cross',units='norm', 
    size=(0.022, 0.04),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from CA1000
counter = 0

# --- Initialize components for Routine "LaFA150msL" ---
IABackgroundL = visual.ImageStim(
    win=win,
    name='IABackgroundL', units='norm', 
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
TALoadL = visual.TextStim(win=win, name='TALoadL',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
IA1L = visual.ImageStim(
    win=win,
    name='IA1L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IA2L = visual.ImageStim(
    win=win,
    name='IA2L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
IA3L = visual.ImageStim(
    win=win,
    name='IA3L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IA4L = visual.ImageStim(
    win=win,
    name='IA4L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
IA5L = visual.ImageStim(
    win=win,
    name='IA5L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
IA6L = visual.ImageStim(
    win=win,
    name='IA6L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
IA7L = visual.ImageStim(
    win=win,
    name='IA7L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
IA8L = visual.ImageStim(
    win=win,
    name='IA8L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
IA9L = visual.ImageStim(
    win=win,
    name='IA9L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# --- Initialize components for Routine "FA1850msR" ---
TAFlankerR = visual.TextStim(win=win, name='TAFlankerR',
    text='?',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KAFlankerR = keyboard.Keyboard()
SAFlankerR = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SAFlankerR')
SAFlankerR.setVolume(1.0)

# --- Initialize components for Routine "CA2000ms" ---
PA2000 = visual.ShapeStim(
    win=win, name='PA2000', vertices='cross',units='norm', 
    size=(0.022, 0.04),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "LA3000msR" ---
IA1R = visual.ImageStim(
    win=win,
    name='IA1R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
IA2R = visual.ImageStim(
    win=win,
    name='IA2R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
IA3R = visual.ImageStim(
    win=win,
    name='IA3R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IA4R = visual.ImageStim(
    win=win,
    name='IA4R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
IA5R = visual.ImageStim(
    win=win,
    name='IA5R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
IA6R = visual.ImageStim(
    win=win,
    name='IA6R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
IA7R = visual.ImageStim(
    win=win,
    name='IA7R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
IA8R = visual.ImageStim(
    win=win,
    name='IA8R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
IA9R = visual.ImageStim(
    win=win,
    name='IA9R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
TADYR = visual.TextStim(win=win, name='TADYR',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
KALoadR = keyboard.Keyboard()

# --- Initialize components for Routine "DeneyGecis" ---
KADGecis = keyboard.Keyboard()
TADGecis = visual.TextStim(win=win, name='TADGecis',
    text='Deney aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "CD1000ms" ---
PD1000 = visual.ShapeStim(
    win=win, name='PD1000', vertices='cross',units='norm', 
    size=(0.022, 0.04),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "LaFD150msL" ---
IDBackgroundL = visual.ImageStim(
    win=win,
    name='IDBackgroundL', units='norm', 
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
TDCeldiriciL = visual.TextStim(win=win, name='TDCeldiriciL',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.18, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
TDLoadL = visual.TextStim(win=win, name='TDLoadL',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ID1L = visual.ImageStim(
    win=win,
    name='ID1L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
ID2L = visual.ImageStim(
    win=win,
    name='ID2L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
ID3L = visual.ImageStim(
    win=win,
    name='ID3L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
ID4L = visual.ImageStim(
    win=win,
    name='ID4L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
ID5L = visual.ImageStim(
    win=win,
    name='ID5L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
ID6L = visual.ImageStim(
    win=win,
    name='ID6L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
ID7L = visual.ImageStim(
    win=win,
    name='ID7L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
ID8L = visual.ImageStim(
    win=win,
    name='ID8L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
ID9L = visual.ImageStim(
    win=win,
    name='ID9L', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# --- Initialize components for Routine "FD1850msR" ---
TDFlankerR = visual.TextStim(win=win, name='TDFlankerR',
    text='?',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KDFlankerR = keyboard.Keyboard()
SDFlankerR = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SDFlankerR')
SDFlankerR.setVolume(1.0)

# --- Initialize components for Routine "CD2000ms" ---
PD2000 = visual.ShapeStim(
    win=win, name='PD2000', vertices='cross',units='norm', 
    size=(0.022, 0.04),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "LD3000msR" ---
ID1R = visual.ImageStim(
    win=win,
    name='ID1R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ID2R = visual.ImageStim(
    win=win,
    name='ID2R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ID3R = visual.ImageStim(
    win=win,
    name='ID3R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ID4R = visual.ImageStim(
    win=win,
    name='ID4R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
ID5R = visual.ImageStim(
    win=win,
    name='ID5R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
ID6R = visual.ImageStim(
    win=win,
    name='ID6R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, 0), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
ID7R = visual.ImageStim(
    win=win,
    name='ID7R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
ID8R = visual.ImageStim(
    win=win,
    name='ID8R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
ID9R = visual.ImageStim(
    win=win,
    name='ID9R', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.0295, -0.053), size=(0,0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
TDDYR = visual.TextStim(win=win, name='TDDYR',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
KDLoadR = keyboard.Keyboard()

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
    trialList=data.importConditions('deney_1a.xlsx'),
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
    
    # --- Prepare to start Routine "CA1000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CA1000
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(1000 / FRate)
    frame = 0
    # keep track of which components have finished
    CA1000msComponents = [PA1000]
    for thisComponent in CA1000msComponents:
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
    
    # --- Run Routine "CA1000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PA1000* updates
        
        # if PA1000 is starting this frame...
        if PA1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PA1000.frameNStart = frameN  # exact frame index
            PA1000.tStart = t  # local t and not account for scr refresh
            PA1000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PA1000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PA1000.started')
            # update status
            PA1000.status = STARTED
            PA1000.setAutoDraw(True)
        
        # if PA1000 is active this frame...
        if PA1000.status == STARTED:
            # update params
            pass
        
        # if PA1000 is stopping this frame...
        if PA1000.status == STARTED:
            if frameN >= (PA1000.frameNStart + FrameN):
                # keep track of stop time/frame for later
                PA1000.tStop = t  # not accounting for scr refresh
                PA1000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PA1000.stopped')
                # update status
                PA1000.status = FINISHED
                PA1000.setAutoDraw(False)
        # Run 'Each Frame' code from CA1000
        frame = frame + 1
        requirement = 1000 / FRate
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
        for thisComponent in CA1000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CA1000ms" ---
    for thisComponent in CA1000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from CA1000
    counter = counter + 1
    # the Routine "CA1000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LaFA150msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IABackgroundL.setImage(pozisyonhedef)
    TAHedefL.setPos(pozisyonharf)
    TAHedefL.setText(hedef)
    TACeldiriciL.setPos(pozisyonceldirici)
    TACeldiriciL.setText(celdirici)
    TALoadL.setText(yuk)
    IA1L.setColor('', colorSpace='rgb')
    IA2L.setColor('', colorSpace='rgb')
    IA3L.setColor('', colorSpace='rgb')
    IA4L.setColor('', colorSpace='rgb')
    IA5L.setColor('', colorSpace='rgb')
    IA6L.setColor('', colorSpace='rgb')
    IA7L.setColor('', colorSpace='rgb')
    IA8L.setColor('', colorSpace='rgb')
    IA9L.setColor('', colorSpace='rgb')
    # Run 'Begin Routine' code from CALaFL
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(150 / FRate)
    frame = 0
    
    YanitD = 0
    YanitY = 0
    
    IA1L.size = (0,0)
    IA2L.size = (0,0)
    IA3L.size = (0,0)
    IA4L.size = (0,0)
    IA5L.size = (0,0)
    IA6L.size = (0,0)
    IA7L.size = (0,0)
    IA8L.size = (0,0)
    IA9L.size = (0,0)
    
    renkler = ["black","blue","cyan","green","magenta","pink","red","white","yellow"]
    shuffle(renkler)
    IA1L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA2L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA3L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA4L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA5L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA6L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA7L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA8L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    IA9L.color = renkler[0]
    renkler.pop(0)
    
    kutucuklar = [1,2,3,4,5,6,7,8,9]
    shuffle(kutucuklar)
    kutu1 = kutucuklar[0]
    kutucuklar.pop(0)
    
    shuffle(kutucuklar)
    kutu2 = kutucuklar[0]
    kutucuklar.pop(0)
    
    shuffle(kutucuklar)
    kutu3 = kutucuklar[0]
    kutucuklar.pop(0)
    
    shuffle(kutucuklar)
    kutu4 = kutucuklar[0]
    kutucuklar.pop(0)
    
    if TALoadL.text == "low":
        if kutu1 == 1:
            IA1L.size = (0.022, 0.04)
        elif kutu1 == 2:
            IA2L.size = (0.022, 0.04)
        elif kutu1 == 3:
            IA3L.size = (0.022, 0.04)
        elif kutu1 == 4:
            IA4L.size = (0.022, 0.04)
        elif kutu1 == 5:
            IA5L.size = (0.022, 0.04)
        elif kutu1 == 6:
            IA6L.size = (0.022, 0.04)
        elif kutu1 == 7:
            IA7L.size = (0.022, 0.04)
        elif kutu1 == 8:
            IA8L.size = (0.022, 0.04)
        elif kutu1 == 9:
            IA9L.size = (0.022, 0.04)
    
    else:
        if kutu1 == 1:
            IA1L.size = (0.022, 0.04)
        elif kutu1 == 2:
            IA2L.size = (0.022, 0.04)
        elif kutu1 == 3:
            IA3L.size = (0.022, 0.04)
        elif kutu1 == 4:
            IA4L.size = (0.022, 0.04)
        elif kutu1 == 5:
            IA5L.size = (0.022, 0.04)
        elif kutu1 == 6:
            IA6L.size = (0.022, 0.04)
        elif kutu1 == 7:
            IA7L.size = (0.022, 0.04)
        elif kutu1 == 8:
            IA8L.size = (0.022, 0.04)
        elif kutu1 == 9:
            IA9L.size = (0.022, 0.04)
        if kutu2 == 1:
            IA1L.size = (0.022, 0.04)
        elif kutu2 == 2:
            IA2L.size = (0.022, 0.04)
        elif kutu2 == 3:
            IA3L.size = (0.022, 0.04)
        elif kutu2 == 4:
            IA4L.size = (0.022, 0.04)
        elif kutu2 == 5:
            IA5L.size = (0.022, 0.04)
        elif kutu2 == 6:
            IA6L.size = (0.022, 0.04)
        elif kutu2 == 7:
            IA7L.size = (0.022, 0.04)
        elif kutu2 == 8:
            IA8L.size = (0.022, 0.04)
        elif kutu2 == 9:
            IA9L.size = (0.022, 0.04)
        if kutu3 == 1:
            IA1L.size = (0.022, 0.04)
        elif kutu3 == 2:
            IA2L.size = (0.022, 0.04)
        elif kutu3 == 3:
            IA3L.size = (0.022, 0.04)
        elif kutu3 == 4:
            IA4L.size = (0.022, 0.04)
        elif kutu3 == 5:
            IA5L.size = (0.022, 0.04)
        elif kutu3 == 6:
            IA6L.size = (0.022, 0.04)
        elif kutu3 == 7:
            IA7L.size = (0.022, 0.04)
        elif kutu3 == 8:
            IA8L.size = (0.022, 0.04)
        elif kutu3 == 9:
            IA9L.size = (0.022, 0.04)
        if kutu4 == 1:
            IA1L.size = (0.022, 0.04)
        elif kutu4 == 2:
            IA2L.size = (0.022, 0.04)
        elif kutu4 == 3:
            IA3L.size = (0.022, 0.04)
        elif kutu4 == 4:
            IA4L.size = (0.022, 0.04)
        elif kutu4 == 5:
            IA5L.size = (0.022, 0.04)
        elif kutu4 == 6:
            IA6L.size = (0.022, 0.04)
        elif kutu4 == 7:
            IA7L.size = (0.022, 0.04)
        elif kutu4 == 8:
            IA8L.size = (0.022, 0.04)
        elif kutu4 == 9:
            IA9L.size = (0.022, 0.04)
    # keep track of which components have finished
    LaFA150msLComponents = [IABackgroundL, TAHedefL, TACeldiriciL, TALoadL, IA1L, IA2L, IA3L, IA4L, IA5L, IA6L, IA7L, IA8L, IA9L]
    for thisComponent in LaFA150msLComponents:
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
    
    # --- Run Routine "LaFA150msL" ---
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
        
        # *IA7L* updates
        
        # if IA7L is starting this frame...
        if IA7L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA7L.frameNStart = frameN  # exact frame index
            IA7L.tStart = t  # local t and not account for scr refresh
            IA7L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA7L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA7L.started')
            # update status
            IA7L.status = STARTED
            IA7L.setAutoDraw(True)
        
        # if IA7L is active this frame...
        if IA7L.status == STARTED:
            # update params
            pass
        
        # if IA7L is stopping this frame...
        if IA7L.status == STARTED:
            if frameN >= (IA7L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA7L.tStop = t  # not accounting for scr refresh
                IA7L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA7L.stopped')
                # update status
                IA7L.status = FINISHED
                IA7L.setAutoDraw(False)
        
        # *IA8L* updates
        
        # if IA8L is starting this frame...
        if IA8L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA8L.frameNStart = frameN  # exact frame index
            IA8L.tStart = t  # local t and not account for scr refresh
            IA8L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA8L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA8L.started')
            # update status
            IA8L.status = STARTED
            IA8L.setAutoDraw(True)
        
        # if IA8L is active this frame...
        if IA8L.status == STARTED:
            # update params
            pass
        
        # if IA8L is stopping this frame...
        if IA8L.status == STARTED:
            if frameN >= (IA8L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA8L.tStop = t  # not accounting for scr refresh
                IA8L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA8L.stopped')
                # update status
                IA8L.status = FINISHED
                IA8L.setAutoDraw(False)
        
        # *IA9L* updates
        
        # if IA9L is starting this frame...
        if IA9L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA9L.frameNStart = frameN  # exact frame index
            IA9L.tStart = t  # local t and not account for scr refresh
            IA9L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA9L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA9L.started')
            # update status
            IA9L.status = STARTED
            IA9L.setAutoDraw(True)
        
        # if IA9L is active this frame...
        if IA9L.status == STARTED:
            # update params
            pass
        
        # if IA9L is stopping this frame...
        if IA9L.status == STARTED:
            if frameN >= (IA9L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA9L.tStop = t  # not accounting for scr refresh
                IA9L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA9L.stopped')
                # update status
                IA9L.status = FINISHED
                IA9L.setAutoDraw(False)
        # Run 'Each Frame' code from CALaFL
        frame = frame + 1
        requirement = 150 / FRate
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
        for thisComponent in LaFA150msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LaFA150msL" ---
    for thisComponent in LaFA150msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LaFA150msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FA1850msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    KAFlankerR.keys = []
    KAFlankerR.rt = []
    _KAFlankerR_allKeys = []
    SAFlankerR.setSound('yanlis.wav', hamming=True)
    SAFlankerR.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CAFlankerR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(1850 / FRate)
    frame = 0
    # keep track of which components have finished
    FA1850msRComponents = [TAFlankerR, KAFlankerR, SAFlankerR]
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
        
        # *TAFlankerR* updates
        
        # if TAFlankerR is starting this frame...
        if TAFlankerR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TAFlankerR.frameNStart = frameN  # exact frame index
            TAFlankerR.tStart = t  # local t and not account for scr refresh
            TAFlankerR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TAFlankerR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TAFlankerR.started')
            # update status
            TAFlankerR.status = STARTED
            TAFlankerR.setAutoDraw(True)
        
        # if TAFlankerR is active this frame...
        if TAFlankerR.status == STARTED:
            # update params
            pass
        
        # if TAFlankerR is stopping this frame...
        if TAFlankerR.status == STARTED:
            if frameN >= (TAFlankerR.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TAFlankerR.tStop = t  # not accounting for scr refresh
                TAFlankerR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TAFlankerR.stopped')
                # update status
                TAFlankerR.status = FINISHED
                TAFlankerR.setAutoDraw(False)
        
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
        # start/stop SAFlankerR
        # Run 'Each Frame' code from CAFlankerR
        frame = frame + 1
        requirement = 1850 / FRate
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
    SAFlankerR.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CAFlankerR
    if KAFlankerR.corr == 0:
        SAFlankerR.play()
    # the Routine "FA1850msR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "CA2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CA2000
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(2000 / FRate)
    frame = 0
    # keep track of which components have finished
    CA2000msComponents = [PA2000]
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
        
        # *PA2000* updates
        
        # if PA2000 is starting this frame...
        if PA2000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PA2000.frameNStart = frameN  # exact frame index
            PA2000.tStart = t  # local t and not account for scr refresh
            PA2000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PA2000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PA2000.started')
            # update status
            PA2000.status = STARTED
            PA2000.setAutoDraw(True)
        
        # if PA2000 is active this frame...
        if PA2000.status == STARTED:
            # update params
            pass
        
        # if PA2000 is stopping this frame...
        if PA2000.status == STARTED:
            if frameN >= (PA2000.frameNStart + FrameN):
                # keep track of stop time/frame for later
                PA2000.tStop = t  # not accounting for scr refresh
                PA2000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PA2000.stopped')
                # update status
                PA2000.status = FINISHED
                PA2000.setAutoDraw(False)
        # Run 'Each Frame' code from CA2000
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
    
    # --- Prepare to start Routine "LA3000msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    IA1R.setColor('', colorSpace='rgb')
    IA2R.setColor('', colorSpace='rgb')
    IA3R.setColor('', colorSpace='rgb')
    IA4R.setColor('', colorSpace='rgb')
    IA5R.setColor('', colorSpace='rgb')
    IA6R.setColor('', colorSpace='rgb')
    IA7R.setColor('', colorSpace='rgb')
    IA8R.setColor('', colorSpace='rgb')
    IA9R.setColor('', colorSpace='rgb')
    TADYR.setText(taskcevap)
    KALoadR.keys = []
    KALoadR.rt = []
    _KALoadR_allKeys = []
    # Run 'Begin Routine' code from CALoadR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(3000 / FRate)
    frame = 0
    
    dizi = [kutu1,kutu2,kutu3,kutu4]
    shuffle(dizi)
    deger = dizi[0]
    
    if deger == 1:
        if TADYR.text == "s":
            IA1R.color = IA1L.color
            IA1R.size = (0.022, 0.04)
        else:
            IA1R.color = IA2L.color
            IA1R.size = (0.022, 0.04)
    elif deger == 2:
        if TADYR.text == "s":
            IA2R.color = IA2L.color
            IA2R.size = (0.022, 0.04)
        else:
            IA2R.color = IA3L.color
            IA2R.size = (0.022, 0.04)
    elif deger == 3:
        if TADYR.text == "s":
            IA3R.color = IA3L.color
            IA3R.size = (0.022, 0.04)
        else:
            IA3R.color = IA4L.color
            IA3R.size = (0.022, 0.04)
    elif deger == 4:
        if TADYR.text == "s":
            IA4R.color = IA4L.color
            IA4R.size = (0.022, 0.04)
        else:
            IA4R.color = IA5L.color
            IA4R.size = (0.022, 0.04)
    elif deger ==5:
        if TADYR.text == "s":
            IA5R.color = IA5L.color
            IA5R.size = (0.022, 0.04)
        else:
            IA5R.color = IA6L.color
            IA5R.size = (0.022, 0.04)
    elif deger == 6:
        if TADYR.text == "s":
            IA6R.color = IA6L.color
            IA6R.size = (0.022, 0.04)
        else:
            IA6R.color = IA7L.color
            IA6R.size = (0.022, 0.04)
    elif deger == 7:
        if TADYR.text == "s":
            IA7R.color = IA7L.color
            IA7R.size = (0.022, 0.04)
        else: 
            IA7R.color = IA8L.color
            IA7R.size = (0.022, 0.04)
    elif deger == 8:
        if TADYR.text == "s":
            IA8R.color = IA8L.color
            IA8R.size = (0.022, 0.04)
        else: 
            IA8R.color = IA9L.color
            IA8R.size = (0.022, 0.04)
    elif deger == 9:
        if TADYR.text == "s":
            IA9R.color = IA9L.color
            IA9R.size = (0.022, 0.04)
        else:
            IA9R.color = IA1L.color
            IA9R.size = (0.022, 0.04)
    # keep track of which components have finished
    LA3000msRComponents = [IA1R, IA2R, IA3R, IA4R, IA5R, IA6R, IA7R, IA8R, IA9R, TADYR, KALoadR]
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
        
        # *IA7R* updates
        
        # if IA7R is starting this frame...
        if IA7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA7R.frameNStart = frameN  # exact frame index
            IA7R.tStart = t  # local t and not account for scr refresh
            IA7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA7R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA7R.started')
            # update status
            IA7R.status = STARTED
            IA7R.setAutoDraw(True)
        
        # if IA7R is active this frame...
        if IA7R.status == STARTED:
            # update params
            pass
        
        # if IA7R is stopping this frame...
        if IA7R.status == STARTED:
            if frameN >= (IA7R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA7R.tStop = t  # not accounting for scr refresh
                IA7R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA7R.stopped')
                # update status
                IA7R.status = FINISHED
                IA7R.setAutoDraw(False)
        
        # *IA8R* updates
        
        # if IA8R is starting this frame...
        if IA8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA8R.frameNStart = frameN  # exact frame index
            IA8R.tStart = t  # local t and not account for scr refresh
            IA8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA8R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA8R.started')
            # update status
            IA8R.status = STARTED
            IA8R.setAutoDraw(True)
        
        # if IA8R is active this frame...
        if IA8R.status == STARTED:
            # update params
            pass
        
        # if IA8R is stopping this frame...
        if IA8R.status == STARTED:
            if frameN >= (IA8R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA8R.tStop = t  # not accounting for scr refresh
                IA8R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA8R.stopped')
                # update status
                IA8R.status = FINISHED
                IA8R.setAutoDraw(False)
        
        # *IA9R* updates
        
        # if IA9R is starting this frame...
        if IA9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IA9R.frameNStart = frameN  # exact frame index
            IA9R.tStart = t  # local t and not account for scr refresh
            IA9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IA9R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IA9R.started')
            # update status
            IA9R.status = STARTED
            IA9R.setAutoDraw(True)
        
        # if IA9R is active this frame...
        if IA9R.status == STARTED:
            # update params
            pass
        
        # if IA9R is stopping this frame...
        if IA9R.status == STARTED:
            if frameN >= (IA9R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IA9R.tStop = t  # not accounting for scr refresh
                IA9R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IA9R.stopped')
                # update status
                IA9R.status = FINISHED
                IA9R.setAutoDraw(False)
        
        # *TADYR* updates
        
        # if TADYR is starting this frame...
        if TADYR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if frameN >= FrameN:
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
        if KALoadR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if frameN >= (KALoadR.frameNStart + FrameN):
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
    # Run 'End Routine' code from CALoadR
    if counter == 2:
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
    trialList=data.importConditions('deney_1a.xlsx'),
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
    
    # --- Prepare to start Routine "CD1000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CD1000
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(1000 / FRate)
    frame = 0
    # keep track of which components have finished
    CD1000msComponents = [PD1000]
    for thisComponent in CD1000msComponents:
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
    
    # --- Run Routine "CD1000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PD1000* updates
        
        # if PD1000 is starting this frame...
        if PD1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PD1000.frameNStart = frameN  # exact frame index
            PD1000.tStart = t  # local t and not account for scr refresh
            PD1000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PD1000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PD1000.started')
            # update status
            PD1000.status = STARTED
            PD1000.setAutoDraw(True)
        
        # if PD1000 is active this frame...
        if PD1000.status == STARTED:
            # update params
            pass
        
        # if PD1000 is stopping this frame...
        if PD1000.status == STARTED:
            if frameN >= (PD1000.frameNStart + FrameN):
                # keep track of stop time/frame for later
                PD1000.tStop = t  # not accounting for scr refresh
                PD1000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PD1000.stopped')
                # update status
                PD1000.status = FINISHED
                PD1000.setAutoDraw(False)
        # Run 'Each Frame' code from CD1000
        frame = frame + 1
        requirement = 1000 / FRate #16.66667 * 111 = 1850.00037 ms (requirement = 111)
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
        for thisComponent in CD1000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CD1000ms" ---
    for thisComponent in CD1000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "CD1000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LaFD150msL" ---
    continueRoutine = True
    # update component parameters for each repeat
    IDBackgroundL.setImage(pozisyonhedef)
    TDHedefL.setPos(pozisyonharf)
    TDHedefL.setText(hedef)
    TDCeldiriciL.setPos(pozisyonceldirici)
    TDCeldiriciL.setText(celdirici)
    TDLoadL.setText(yuk)
    ID1L.setColor('', colorSpace='rgb')
    ID2L.setColor('', colorSpace='rgb')
    ID3L.setColor('', colorSpace='rgb')
    ID4L.setColor('', colorSpace='rgb')
    ID5L.setColor('', colorSpace='rgb')
    ID6L.setColor('', colorSpace='rgb')
    ID7L.setColor('', colorSpace='rgb')
    ID8L.setColor('', colorSpace='rgb')
    ID9L.setColor('', colorSpace='rgb')
    # Run 'Begin Routine' code from CDLaFL
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(150 / FRate)
    frame = 0
    
    YanitD = 0
    YanitY = 0
    
    ID1L.size = (0,0)
    ID2L.size = (0,0)
    ID3L.size = (0,0)
    ID4L.size = (0,0)
    ID5L.size = (0,0)
    ID6L.size = (0,0)
    ID7L.size = (0,0)
    ID8L.size = (0,0)
    ID9L.size = (0,0)
    
    renkler = ["black","blue","cyan","green","magenta","pink","red","white","yellow"]
    shuffle(renkler)
    ID1L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID2L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID3L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID4L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID5L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID6L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID7L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID8L.color = renkler[0]
    renkler.pop(0)
    
    shuffle(renkler)
    ID9L.color = renkler[0]
    renkler.pop(0)
    
    kutucuklar = [1,2,3,4,5,6,7,8,9]
    shuffle(kutucuklar)
    kutu1 = kutucuklar[0]
    kutucuklar.pop(0)
    
    shuffle(kutucuklar)
    kutu2 = kutucuklar[0]
    kutucuklar.pop(0)
    
    shuffle(kutucuklar)
    kutu3 = kutucuklar[0]
    kutucuklar.pop(0)
    
    shuffle(kutucuklar)
    kutu4 = kutucuklar[0]
    kutucuklar.pop(0)
    
    if TDLoadL.text == "low":
        if kutu1 == 1:
            ID1L.size = (0.022, 0.04)
        elif kutu1 == 2:
            ID2L.size = (0.022, 0.04)
        elif kutu1 == 3:
            ID3L.size = (0.022, 0.04)
        elif kutu1 == 4:
            ID4L.size = (0.022, 0.04)
        elif kutu1 == 5:
            ID5L.size = (0.022, 0.04)
        elif kutu1 == 6:
            ID6L.size = (0.022, 0.04)
        elif kutu1 == 7:
            ID7L.size = (0.022, 0.04)
        elif kutu1 == 8:
            ID8L.size = (0.022, 0.04)
        elif kutu1 == 9:
            ID9L.size = (0.022, 0.04)
    
    else:
        if kutu1 == 1:
            ID1L.size = (0.022, 0.04)
        elif kutu1 == 2:
            ID2L.size = (0.022, 0.04)
        elif kutu1 == 3:
            ID3L.size = (0.022, 0.04)
        elif kutu1 == 4:
            ID4L.size = (0.022, 0.04)
        elif kutu1 == 5:
            ID5L.size = (0.022, 0.04)
        elif kutu1 == 6:
            ID6L.size = (0.022, 0.04)
        elif kutu1 == 7:
            ID7L.size = (0.022, 0.04)
        elif kutu1 == 8:
            ID8L.size = (0.022, 0.04)
        elif kutu1 == 9:
            ID9L.size = (0.022, 0.04)
        if kutu2 == 1:
            ID1L.size = (0.022, 0.04)
        elif kutu2 == 2:
            ID2L.size = (0.022, 0.04)
        elif kutu2 == 3:
            ID3L.size = (0.022, 0.04)
        elif kutu2 == 4:
            ID4L.size = (0.022, 0.04)
        elif kutu2 == 5:
            ID5L.size = (0.022, 0.04)
        elif kutu2 == 6:
            ID6L.size = (0.022, 0.04)
        elif kutu2 == 7:
            ID7L.size = (0.022, 0.04)
        elif kutu2 == 8:
            ID8L.size = (0.022, 0.04)
        elif kutu2 == 9:
            ID9L.size = (0.022, 0.04)
        if kutu3 == 1:
            ID1L.size = (0.022, 0.04)
        elif kutu3 == 2:
            ID2L.size = (0.022, 0.04)
        elif kutu3 == 3:
            ID3L.size = (0.022, 0.04)
        elif kutu3 == 4:
            ID4L.size = (0.022, 0.04)
        elif kutu3 == 5:
            ID5L.size = (0.022, 0.04)
        elif kutu3 == 6:
            ID6L.size = (0.022, 0.04)
        elif kutu3 == 7:
            ID7L.size = (0.022, 0.04)
        elif kutu3 == 8:
            ID8L.size = (0.022, 0.04)
        elif kutu3 == 9:
            ID9L.size = (0.022, 0.04)
        if kutu4 == 1:
            ID1L.size = (0.022, 0.04)
        elif kutu4 == 2:
            ID2L.size = (0.022, 0.04)
        elif kutu4 == 3:
            ID3L.size = (0.022, 0.04)
        elif kutu4 == 4:
            ID4L.size = (0.022, 0.04)
        elif kutu4 == 5:
            ID5L.size = (0.022, 0.04)
        elif kutu4 == 6:
            ID6L.size = (0.022, 0.04)
        elif kutu4 == 7:
            ID7L.size = (0.022, 0.04)
        elif kutu4 == 8:
            ID8L.size = (0.022, 0.04)
        elif kutu4 == 9:
            ID9L.size = (0.022, 0.04)
    # keep track of which components have finished
    LaFD150msLComponents = [IDBackgroundL, TDHedefL, TDCeldiriciL, TDLoadL, ID1L, ID2L, ID3L, ID4L, ID5L, ID6L, ID7L, ID8L, ID9L]
    for thisComponent in LaFD150msLComponents:
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
    
    # --- Run Routine "LaFD150msL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IDBackgroundL* updates
        
        # if IDBackgroundL is starting this frame...
        if IDBackgroundL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IDBackgroundL.frameNStart = frameN  # exact frame index
            IDBackgroundL.tStart = t  # local t and not account for scr refresh
            IDBackgroundL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IDBackgroundL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IDBackgroundL.started')
            # update status
            IDBackgroundL.status = STARTED
            IDBackgroundL.setAutoDraw(True)
        
        # if IDBackgroundL is active this frame...
        if IDBackgroundL.status == STARTED:
            # update params
            pass
        
        # if IDBackgroundL is stopping this frame...
        if IDBackgroundL.status == STARTED:
            if frameN >= (IDBackgroundL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                IDBackgroundL.tStop = t  # not accounting for scr refresh
                IDBackgroundL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IDBackgroundL.stopped')
                # update status
                IDBackgroundL.status = FINISHED
                IDBackgroundL.setAutoDraw(False)
        
        # *TDHedefL* updates
        
        # if TDHedefL is starting this frame...
        if TDHedefL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if frameN >= (TDHedefL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TDHedefL.tStop = t  # not accounting for scr refresh
                TDHedefL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDHedefL.stopped')
                # update status
                TDHedefL.status = FINISHED
                TDHedefL.setAutoDraw(False)
        
        # *TDCeldiriciL* updates
        
        # if TDCeldiriciL is starting this frame...
        if TDCeldiriciL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TDCeldiriciL.frameNStart = frameN  # exact frame index
            TDCeldiriciL.tStart = t  # local t and not account for scr refresh
            TDCeldiriciL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDCeldiriciL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDCeldiriciL.started')
            # update status
            TDCeldiriciL.status = STARTED
            TDCeldiriciL.setAutoDraw(True)
        
        # if TDCeldiriciL is active this frame...
        if TDCeldiriciL.status == STARTED:
            # update params
            pass
        
        # if TDCeldiriciL is stopping this frame...
        if TDCeldiriciL.status == STARTED:
            if frameN >= (TDCeldiriciL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TDCeldiriciL.tStop = t  # not accounting for scr refresh
                TDCeldiriciL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDCeldiriciL.stopped')
                # update status
                TDCeldiriciL.status = FINISHED
                TDCeldiriciL.setAutoDraw(False)
        
        # *TDLoadL* updates
        
        # if TDLoadL is starting this frame...
        if TDLoadL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if frameN >= (TDLoadL.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TDLoadL.tStop = t  # not accounting for scr refresh
                TDLoadL.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDLoadL.stopped')
                # update status
                TDLoadL.status = FINISHED
                TDLoadL.setAutoDraw(False)
        
        # *ID1L* updates
        
        # if ID1L is starting this frame...
        if ID1L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID1L.frameNStart = frameN  # exact frame index
            ID1L.tStart = t  # local t and not account for scr refresh
            ID1L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID1L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID1L.started')
            # update status
            ID1L.status = STARTED
            ID1L.setAutoDraw(True)
        
        # if ID1L is active this frame...
        if ID1L.status == STARTED:
            # update params
            pass
        
        # if ID1L is stopping this frame...
        if ID1L.status == STARTED:
            if frameN >= (ID1L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID1L.tStop = t  # not accounting for scr refresh
                ID1L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID1L.stopped')
                # update status
                ID1L.status = FINISHED
                ID1L.setAutoDraw(False)
        
        # *ID2L* updates
        
        # if ID2L is starting this frame...
        if ID2L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID2L.frameNStart = frameN  # exact frame index
            ID2L.tStart = t  # local t and not account for scr refresh
            ID2L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID2L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID2L.started')
            # update status
            ID2L.status = STARTED
            ID2L.setAutoDraw(True)
        
        # if ID2L is active this frame...
        if ID2L.status == STARTED:
            # update params
            pass
        
        # if ID2L is stopping this frame...
        if ID2L.status == STARTED:
            if frameN >= (ID2L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID2L.tStop = t  # not accounting for scr refresh
                ID2L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID2L.stopped')
                # update status
                ID2L.status = FINISHED
                ID2L.setAutoDraw(False)
        
        # *ID3L* updates
        
        # if ID3L is starting this frame...
        if ID3L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID3L.frameNStart = frameN  # exact frame index
            ID3L.tStart = t  # local t and not account for scr refresh
            ID3L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID3L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID3L.started')
            # update status
            ID3L.status = STARTED
            ID3L.setAutoDraw(True)
        
        # if ID3L is active this frame...
        if ID3L.status == STARTED:
            # update params
            pass
        
        # if ID3L is stopping this frame...
        if ID3L.status == STARTED:
            if frameN >= (ID3L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID3L.tStop = t  # not accounting for scr refresh
                ID3L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID3L.stopped')
                # update status
                ID3L.status = FINISHED
                ID3L.setAutoDraw(False)
        
        # *ID4L* updates
        
        # if ID4L is starting this frame...
        if ID4L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID4L.frameNStart = frameN  # exact frame index
            ID4L.tStart = t  # local t and not account for scr refresh
            ID4L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID4L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID4L.started')
            # update status
            ID4L.status = STARTED
            ID4L.setAutoDraw(True)
        
        # if ID4L is active this frame...
        if ID4L.status == STARTED:
            # update params
            pass
        
        # if ID4L is stopping this frame...
        if ID4L.status == STARTED:
            if frameN >= (ID4L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID4L.tStop = t  # not accounting for scr refresh
                ID4L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID4L.stopped')
                # update status
                ID4L.status = FINISHED
                ID4L.setAutoDraw(False)
        
        # *ID5L* updates
        
        # if ID5L is starting this frame...
        if ID5L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID5L.frameNStart = frameN  # exact frame index
            ID5L.tStart = t  # local t and not account for scr refresh
            ID5L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID5L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID5L.started')
            # update status
            ID5L.status = STARTED
            ID5L.setAutoDraw(True)
        
        # if ID5L is active this frame...
        if ID5L.status == STARTED:
            # update params
            pass
        
        # if ID5L is stopping this frame...
        if ID5L.status == STARTED:
            if frameN >= (ID5L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID5L.tStop = t  # not accounting for scr refresh
                ID5L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID5L.stopped')
                # update status
                ID5L.status = FINISHED
                ID5L.setAutoDraw(False)
        
        # *ID6L* updates
        
        # if ID6L is starting this frame...
        if ID6L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID6L.frameNStart = frameN  # exact frame index
            ID6L.tStart = t  # local t and not account for scr refresh
            ID6L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID6L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID6L.started')
            # update status
            ID6L.status = STARTED
            ID6L.setAutoDraw(True)
        
        # if ID6L is active this frame...
        if ID6L.status == STARTED:
            # update params
            pass
        
        # if ID6L is stopping this frame...
        if ID6L.status == STARTED:
            if frameN >= (ID6L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID6L.tStop = t  # not accounting for scr refresh
                ID6L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID6L.stopped')
                # update status
                ID6L.status = FINISHED
                ID6L.setAutoDraw(False)
        
        # *ID7L* updates
        
        # if ID7L is starting this frame...
        if ID7L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID7L.frameNStart = frameN  # exact frame index
            ID7L.tStart = t  # local t and not account for scr refresh
            ID7L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID7L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID7L.started')
            # update status
            ID7L.status = STARTED
            ID7L.setAutoDraw(True)
        
        # if ID7L is active this frame...
        if ID7L.status == STARTED:
            # update params
            pass
        
        # if ID7L is stopping this frame...
        if ID7L.status == STARTED:
            if frameN >= (ID7L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID7L.tStop = t  # not accounting for scr refresh
                ID7L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID7L.stopped')
                # update status
                ID7L.status = FINISHED
                ID7L.setAutoDraw(False)
        
        # *ID8L* updates
        
        # if ID8L is starting this frame...
        if ID8L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID8L.frameNStart = frameN  # exact frame index
            ID8L.tStart = t  # local t and not account for scr refresh
            ID8L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID8L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID8L.started')
            # update status
            ID8L.status = STARTED
            ID8L.setAutoDraw(True)
        
        # if ID8L is active this frame...
        if ID8L.status == STARTED:
            # update params
            pass
        
        # if ID8L is stopping this frame...
        if ID8L.status == STARTED:
            if frameN >= (ID8L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID8L.tStop = t  # not accounting for scr refresh
                ID8L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID8L.stopped')
                # update status
                ID8L.status = FINISHED
                ID8L.setAutoDraw(False)
        
        # *ID9L* updates
        
        # if ID9L is starting this frame...
        if ID9L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID9L.frameNStart = frameN  # exact frame index
            ID9L.tStart = t  # local t and not account for scr refresh
            ID9L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID9L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID9L.started')
            # update status
            ID9L.status = STARTED
            ID9L.setAutoDraw(True)
        
        # if ID9L is active this frame...
        if ID9L.status == STARTED:
            # update params
            pass
        
        # if ID9L is stopping this frame...
        if ID9L.status == STARTED:
            if frameN >= (ID9L.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID9L.tStop = t  # not accounting for scr refresh
                ID9L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID9L.stopped')
                # update status
                ID9L.status = FINISHED
                ID9L.setAutoDraw(False)
        # Run 'Each Frame' code from CDLaFL
        frame = frame + 1
        requirement = 150 / FRate #16.66667 * 111 = 1850.00037 ms (requirement = 111)
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
        for thisComponent in LaFD150msLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LaFD150msL" ---
    for thisComponent in LaFD150msLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LaFD150msL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FD1850msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    KDFlankerR.keys = []
    KDFlankerR.rt = []
    _KDFlankerR_allKeys = []
    SDFlankerR.setSound('yanlis.wav', hamming=True)
    SDFlankerR.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CDFlankerR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(1850 / FRate)
    frame = 0
    # keep track of which components have finished
    FD1850msRComponents = [TDFlankerR, KDFlankerR, SDFlankerR]
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
        
        # *TDFlankerR* updates
        
        # if TDFlankerR is starting this frame...
        if TDFlankerR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TDFlankerR.frameNStart = frameN  # exact frame index
            TDFlankerR.tStart = t  # local t and not account for scr refresh
            TDFlankerR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDFlankerR, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDFlankerR.started')
            # update status
            TDFlankerR.status = STARTED
            TDFlankerR.setAutoDraw(True)
        
        # if TDFlankerR is active this frame...
        if TDFlankerR.status == STARTED:
            # update params
            pass
        
        # if TDFlankerR is stopping this frame...
        if TDFlankerR.status == STARTED:
            if frameN >= (TDFlankerR.frameNStart + FrameN):
                # keep track of stop time/frame for later
                TDFlankerR.tStop = t  # not accounting for scr refresh
                TDFlankerR.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDFlankerR.stopped')
                # update status
                TDFlankerR.status = FINISHED
                TDFlankerR.setAutoDraw(False)
        
        # *KDFlankerR* updates
        waitOnFlip = False
        
        # if KDFlankerR is starting this frame...
        if KDFlankerR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
            if frameN >= (KDFlankerR.frameNStart + FrameN):
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
        # start/stop SDFlankerR
        # Run 'Each Frame' code from CDFlankerR
        frame = frame + 1
        requirement = 1850 / FRate #16.66667 * 111 = 1850.00037 ms (requirement = 111)
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
    SDFlankerR.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CDFlankerR
    if KDFlankerR.corr == 0:
        SDFlankerR.play()
    # the Routine "FD1850msR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "CD2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from CD2000
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(2000 / FRate)
    frame = 0
    # keep track of which components have finished
    CD2000msComponents = [PD2000]
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
        
        # *PD2000* updates
        
        # if PD2000 is starting this frame...
        if PD2000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PD2000.frameNStart = frameN  # exact frame index
            PD2000.tStart = t  # local t and not account for scr refresh
            PD2000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PD2000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PD2000.started')
            # update status
            PD2000.status = STARTED
            PD2000.setAutoDraw(True)
        
        # if PD2000 is active this frame...
        if PD2000.status == STARTED:
            # update params
            pass
        
        # if PD2000 is stopping this frame...
        if PD2000.status == STARTED:
            if frameN >= (PD2000.frameNStart + FrameN):
                # keep track of stop time/frame for later
                PD2000.tStop = t  # not accounting for scr refresh
                PD2000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PD2000.stopped')
                # update status
                PD2000.status = FINISHED
                PD2000.setAutoDraw(False)
        # Run 'Each Frame' code from CD2000
        frame = frame + 1
        requirement = 2000 / FRate #16.66667 * 111 = 1850.00037 ms (requirement = 111)
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
    
    # --- Prepare to start Routine "LD3000msR" ---
    continueRoutine = True
    # update component parameters for each repeat
    ID1R.setColor('', colorSpace='rgb')
    ID2R.setColor('', colorSpace='rgb')
    ID3R.setColor('', colorSpace='rgb')
    ID4R.setColor('', colorSpace='rgb')
    ID5R.setColor('', colorSpace='rgb')
    ID6R.setColor('', colorSpace='rgb')
    ID7R.setColor('', colorSpace='rgb')
    ID8R.setColor('', colorSpace='rgb')
    ID9R.setColor('', colorSpace='rgb')
    TDDYR.setText(taskcevap)
    KDLoadR.keys = []
    KDLoadR.rt = []
    _KDLoadR_allKeys = []
    # Run 'Begin Routine' code from CDLoadR
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(3000 / FRate)
    frame = 0
    
    dizi = [kutu1,kutu2,kutu3,kutu4]
    shuffle(dizi)
    deger = dizi[0]
    
    if deger == 1:
        if TDDYR.text == "s":
            ID1R.color = ID1L.color
            ID1R.size = (0.022, 0.04)
        else:
            ID1R.color = ID2L.color
            ID1R.size = (0.022, 0.04)
    elif deger == 2:
        if TDDYR.text == "s":
            ID2R.color = ID2L.color
            ID2R.size = (0.022, 0.04)
        else:
            ID2R.color = ID3L.color
            ID2R.size = (0.022, 0.04)
    elif deger == 3:
        if TDDYR.text == "s":
            ID3R.color = ID3L.color
            ID3R.size = (0.022, 0.04)
        else:
            ID3R.color = ID4L.color
            ID3R.size = (0.022, 0.04)
    elif deger == 4:
        if TDDYR.text == "s":
            ID4R.color = ID4L.color
            ID4R.size = (0.022, 0.04)
        else:
            ID4R.color = ID5L.color
            ID4R.size = (0.022, 0.04)
    elif deger ==5:
        if TDDYR.text == "s":
            ID5R.color = ID5L.color
            ID5R.size = (0.022, 0.04)
        else:
            ID5R.color = ID6L.color
            ID5R.size = (0.022, 0.04)
    elif deger == 6:
        if TDDYR.text == "s":
            ID6R.color = ID6L.color
            ID6R.size = (0.022, 0.04)
        else:
            ID6R.color = ID7L.color
            ID6R.size = (0.022, 0.04)
    elif deger == 7:
        if TDDYR.text == "s":
            ID7R.color = ID7L.color
            ID7R.size = (0.022, 0.04)
        else: 
            ID7R.color = ID8L.color
            ID7R.size = (0.022, 0.04)
    elif deger == 8:
        if TDDYR.text == "s":
            ID8R.color = ID8L.color
            ID8R.size = (0.022, 0.04)
        else: 
            ID8R.color = ID9L.color
            ID8R.size = (0.022, 0.04)
    elif deger == 9:
        if TDDYR.text == "s":
            ID9R.color = ID9L.color
            ID9R.size = (0.022, 0.04)
        else:
            ID9R.color = ID1L.color
            ID9R.size = (0.022, 0.04)
    # keep track of which components have finished
    LD3000msRComponents = [ID1R, ID2R, ID3R, ID4R, ID5R, ID6R, ID7R, ID8R, ID9R, TDDYR, KDLoadR]
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
        
        # *ID1R* updates
        
        # if ID1R is starting this frame...
        if ID1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID1R.frameNStart = frameN  # exact frame index
            ID1R.tStart = t  # local t and not account for scr refresh
            ID1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID1R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID1R.started')
            # update status
            ID1R.status = STARTED
            ID1R.setAutoDraw(True)
        
        # if ID1R is active this frame...
        if ID1R.status == STARTED:
            # update params
            pass
        
        # if ID1R is stopping this frame...
        if ID1R.status == STARTED:
            if frameN >= (ID1R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID1R.tStop = t  # not accounting for scr refresh
                ID1R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID1R.stopped')
                # update status
                ID1R.status = FINISHED
                ID1R.setAutoDraw(False)
        
        # *ID2R* updates
        
        # if ID2R is starting this frame...
        if ID2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID2R.frameNStart = frameN  # exact frame index
            ID2R.tStart = t  # local t and not account for scr refresh
            ID2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID2R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID2R.started')
            # update status
            ID2R.status = STARTED
            ID2R.setAutoDraw(True)
        
        # if ID2R is active this frame...
        if ID2R.status == STARTED:
            # update params
            pass
        
        # if ID2R is stopping this frame...
        if ID2R.status == STARTED:
            if frameN >= (ID2R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID2R.tStop = t  # not accounting for scr refresh
                ID2R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID2R.stopped')
                # update status
                ID2R.status = FINISHED
                ID2R.setAutoDraw(False)
        
        # *ID3R* updates
        
        # if ID3R is starting this frame...
        if ID3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID3R.frameNStart = frameN  # exact frame index
            ID3R.tStart = t  # local t and not account for scr refresh
            ID3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID3R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID3R.started')
            # update status
            ID3R.status = STARTED
            ID3R.setAutoDraw(True)
        
        # if ID3R is active this frame...
        if ID3R.status == STARTED:
            # update params
            pass
        
        # if ID3R is stopping this frame...
        if ID3R.status == STARTED:
            if frameN >= (ID3R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID3R.tStop = t  # not accounting for scr refresh
                ID3R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID3R.stopped')
                # update status
                ID3R.status = FINISHED
                ID3R.setAutoDraw(False)
        
        # *ID4R* updates
        
        # if ID4R is starting this frame...
        if ID4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID4R.frameNStart = frameN  # exact frame index
            ID4R.tStart = t  # local t and not account for scr refresh
            ID4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID4R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID4R.started')
            # update status
            ID4R.status = STARTED
            ID4R.setAutoDraw(True)
        
        # if ID4R is active this frame...
        if ID4R.status == STARTED:
            # update params
            pass
        
        # if ID4R is stopping this frame...
        if ID4R.status == STARTED:
            if frameN >= (ID4R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID4R.tStop = t  # not accounting for scr refresh
                ID4R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID4R.stopped')
                # update status
                ID4R.status = FINISHED
                ID4R.setAutoDraw(False)
        
        # *ID5R* updates
        
        # if ID5R is starting this frame...
        if ID5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID5R.frameNStart = frameN  # exact frame index
            ID5R.tStart = t  # local t and not account for scr refresh
            ID5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID5R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID5R.started')
            # update status
            ID5R.status = STARTED
            ID5R.setAutoDraw(True)
        
        # if ID5R is active this frame...
        if ID5R.status == STARTED:
            # update params
            pass
        
        # if ID5R is stopping this frame...
        if ID5R.status == STARTED:
            if frameN >= (ID5R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID5R.tStop = t  # not accounting for scr refresh
                ID5R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID5R.stopped')
                # update status
                ID5R.status = FINISHED
                ID5R.setAutoDraw(False)
        
        # *ID6R* updates
        
        # if ID6R is starting this frame...
        if ID6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID6R.frameNStart = frameN  # exact frame index
            ID6R.tStart = t  # local t and not account for scr refresh
            ID6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID6R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID6R.started')
            # update status
            ID6R.status = STARTED
            ID6R.setAutoDraw(True)
        
        # if ID6R is active this frame...
        if ID6R.status == STARTED:
            # update params
            pass
        
        # if ID6R is stopping this frame...
        if ID6R.status == STARTED:
            if frameN >= (ID6R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID6R.tStop = t  # not accounting for scr refresh
                ID6R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID6R.stopped')
                # update status
                ID6R.status = FINISHED
                ID6R.setAutoDraw(False)
        
        # *ID7R* updates
        
        # if ID7R is starting this frame...
        if ID7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID7R.frameNStart = frameN  # exact frame index
            ID7R.tStart = t  # local t and not account for scr refresh
            ID7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID7R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID7R.started')
            # update status
            ID7R.status = STARTED
            ID7R.setAutoDraw(True)
        
        # if ID7R is active this frame...
        if ID7R.status == STARTED:
            # update params
            pass
        
        # if ID7R is stopping this frame...
        if ID7R.status == STARTED:
            if frameN >= (ID7R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID7R.tStop = t  # not accounting for scr refresh
                ID7R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID7R.stopped')
                # update status
                ID7R.status = FINISHED
                ID7R.setAutoDraw(False)
        
        # *ID8R* updates
        
        # if ID8R is starting this frame...
        if ID8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID8R.frameNStart = frameN  # exact frame index
            ID8R.tStart = t  # local t and not account for scr refresh
            ID8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID8R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID8R.started')
            # update status
            ID8R.status = STARTED
            ID8R.setAutoDraw(True)
        
        # if ID8R is active this frame...
        if ID8R.status == STARTED:
            # update params
            pass
        
        # if ID8R is stopping this frame...
        if ID8R.status == STARTED:
            if frameN >= (ID8R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID8R.tStop = t  # not accounting for scr refresh
                ID8R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID8R.stopped')
                # update status
                ID8R.status = FINISHED
                ID8R.setAutoDraw(False)
        
        # *ID9R* updates
        
        # if ID9R is starting this frame...
        if ID9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ID9R.frameNStart = frameN  # exact frame index
            ID9R.tStart = t  # local t and not account for scr refresh
            ID9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ID9R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ID9R.started')
            # update status
            ID9R.status = STARTED
            ID9R.setAutoDraw(True)
        
        # if ID9R is active this frame...
        if ID9R.status == STARTED:
            # update params
            pass
        
        # if ID9R is stopping this frame...
        if ID9R.status == STARTED:
            if frameN >= (ID9R.frameNStart + FrameN):
                # keep track of stop time/frame for later
                ID9R.tStop = t  # not accounting for scr refresh
                ID9R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ID9R.stopped')
                # update status
                ID9R.status = FINISHED
                ID9R.setAutoDraw(False)
        
        # *TDDYR* updates
        
        # if TDDYR is starting this frame...
        if TDDYR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if frameN >= FrameN:
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
        if KDLoadR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if frameN >= (KDLoadR.frameNStart + FrameN):
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
