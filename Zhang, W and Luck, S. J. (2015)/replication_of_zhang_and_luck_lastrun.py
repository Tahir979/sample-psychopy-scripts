#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on July 21, 2023, at 13:47
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
expName = 'replication_of_zhang_and_luck'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\wasd0\\Desktop\\Psychopy\\Zhang, W and Luck, S. J. (2015)\\replication_of_zhang_and_luck_lastrun.py',
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

# --- Initialize components for Routine "Yonerge" ---
KAYonerge = keyboard.Keyboard()
TAYonerge = visual.TextStim(win=win, name='TAYonerge',
    text='Çalışmamıza hoş geldiniz.\n\nBirazdan ekranınıza bazı renkli kutucuklar sunulacaktır. Sizden, ekranınıza gelen kutucukları, renk ve konum bilgileriyle beraber aklınızda tutmanız beklenmektedir. \n\nBunun ardından ekranınıza iki adet harf (X,Z ve N) sunumu gerçekleştirilecek olup yatay hizada bulunan harf hangisi ise ilgili o tuşa basmanız beklenmektedir, ardından ise ilk ekranda sunulan kutucuklardan bir tanesi sunularak renk ve konum bilgisinin doğru olup olmadığına dair bir cevaplama (eşleşme varsa Ö,eşleşme yoksa Ç) yapmanız beklenmektedir.\n\nİlk 16 deneme alıştırma niteliğinde olup, 16. denemenin ardından deneye başlanacaktır.\n\nAlıştırma aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Fixation800ms" ---
A_image800 = visual.ImageStim(
    win=win,
    name='A_image800', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
A_kosul = visual.TextStim(win=win, name='A_kosul',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
A_cevap = visual.TextStim(win=win, name='A_cevap',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from A_code800
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

# --- Initialize components for Routine "VWMLoad200ms" ---
A_Background1 = visual.ImageStim(
    win=win,
    name='A_Background1', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
A_image1 = visual.ImageStim(
    win=win,
    name='A_image1', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
A_image2 = visual.ImageStim(
    win=win,
    name='A_image2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
A_image3 = visual.ImageStim(
    win=win,
    name='A_image3', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
A_image4 = visual.ImageStim(
    win=win,
    name='A_image4', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
A_image5 = visual.ImageStim(
    win=win,
    name='A_image5', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
A_image6 = visual.ImageStim(
    win=win,
    name='A_image6', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "BlankScreen2000ms" ---
A_image = visual.ImageStim(
    win=win,
    name='A_image', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Flanker2000ms" ---
A_Background2 = visual.ImageStim(
    win=win,
    name='A_Background2', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
A_Hedef = visual.TextStim(win=win, name='A_Hedef',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.13, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
A_Celdirici = visual.TextStim(win=win, name='A_Celdirici',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.186, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
A_Key = keyboard.Keyboard()
A_Sound = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='A_Sound')
A_Sound.setVolume(1.0)

# --- Initialize components for Routine "FlankerFixation500ms" ---
A_500 = visual.ImageStim(
    win=win,
    name='A_500', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "VWMLoadTask" ---
A_Background1_2 = visual.ImageStim(
    win=win,
    name='A_Background1_2', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
A_image1_2 = visual.ImageStim(
    win=win,
    name='A_image1_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
A_image2_2 = visual.ImageStim(
    win=win,
    name='A_image2_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
A_image3_2 = visual.ImageStim(
    win=win,
    name='A_image3_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
A_image4_2 = visual.ImageStim(
    win=win,
    name='A_image4_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
A_image5_2 = visual.ImageStim(
    win=win,
    name='A_image5_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
A_image6_2 = visual.ImageStim(
    win=win,
    name='A_image6_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
A_Poli1 = visual.Rect(
    win=win, name='A_Poli1',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.176, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
A_Poli2 = visual.Rect(
    win=win, name='A_Poli2',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.118, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
A_Poli3 = visual.Rect(
    win=win, name='A_Poli3',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.118, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
A_Poli4 = visual.Rect(
    win=win, name='A_Poli4',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.176, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
A_Poli5 = visual.Rect(
    win=win, name='A_Poli5',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.147, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
A_Poli6 = visual.Rect(
    win=win, name='A_Poli6',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.147, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)
A_Key_2 = keyboard.Keyboard()
A_Sound_2 = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='A_Sound_2')
A_Sound_2.setVolume(1.0)

# --- Initialize components for Routine "DeneyGecis" ---
KDYonerge = keyboard.Keyboard()
TDYonerge = visual.TextStim(win=win, name='TDYonerge',
    text='Deney aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "D_Fixation800ms" ---
D_image800 = visual.ImageStim(
    win=win,
    name='D_image800', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
D_kosul = visual.TextStim(win=win, name='D_kosul',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
D_cevap = visual.TextStim(win=win, name='D_cevap',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from D_code800
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

# --- Initialize components for Routine "D_VWMLoad200ms" ---
D_Background1 = visual.ImageStim(
    win=win,
    name='D_Background1', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
D_image1 = visual.ImageStim(
    win=win,
    name='D_image1', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
D_image2 = visual.ImageStim(
    win=win,
    name='D_image2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
D_image3 = visual.ImageStim(
    win=win,
    name='D_image3', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
D_image4 = visual.ImageStim(
    win=win,
    name='D_image4', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
D_image5 = visual.ImageStim(
    win=win,
    name='D_image5', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
D_image6 = visual.ImageStim(
    win=win,
    name='D_image6', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "D_BlankScreen2000ms" ---
D_image = visual.ImageStim(
    win=win,
    name='D_image', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "D_Flanker2000ms" ---
D_Background2 = visual.ImageStim(
    win=win,
    name='D_Background2', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
D_Hedef = visual.TextStim(win=win, name='D_Hedef',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.13, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
D_Celdirici = visual.TextStim(win=win, name='D_Celdirici',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.186, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
D_Key = keyboard.Keyboard()
D_Sound = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='D_Sound')
D_Sound.setVolume(1.0)

# --- Initialize components for Routine "D_FlankerFixation500ms" ---
D_500 = visual.ImageStim(
    win=win,
    name='D_500', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "D_VWMLoadTask" ---
D_Background1_2 = visual.ImageStim(
    win=win,
    name='D_Background1_2', units='norm', 
    image='fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2.0, 2.0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
D_image1_2 = visual.ImageStim(
    win=win,
    name='D_image1_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
D_image2_2 = visual.ImageStim(
    win=win,
    name='D_image2_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
D_image3_2 = visual.ImageStim(
    win=win,
    name='D_image3_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.118, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
D_image4_2 = visual.ImageStim(
    win=win,
    name='D_image4_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.176, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
D_image5_2 = visual.ImageStim(
    win=win,
    name='D_image5_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
D_image6_2 = visual.ImageStim(
    win=win,
    name='D_image6_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.147, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
D_Poli1 = visual.Rect(
    win=win, name='D_Poli1',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.176, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
D_Poli2 = visual.Rect(
    win=win, name='D_Poli2',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.118, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
D_Poli3 = visual.Rect(
    win=win, name='D_Poli3',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.118, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
D_Poli4 = visual.Rect(
    win=win, name='D_Poli4',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.176, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
D_Poli5 = visual.Rect(
    win=win, name='D_Poli5',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.147, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
D_Poli6 = visual.Rect(
    win=win, name='D_Poli6',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.147, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)
D_Key_2 = keyboard.Keyboard()
D_Sound_2 = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='D_Sound_2')
D_Sound_2.setVolume(1.0)

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
    trialList=data.importConditions('replication_of_zhang_and_luck.xlsx'),
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
    
    # --- Prepare to start Routine "Fixation800ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    A_kosul.setText(condition)
    A_cevap.setText(taskcevap)
    # keep track of which components have finished
    Fixation800msComponents = [A_image800, A_kosul, A_cevap]
    for thisComponent in Fixation800msComponents:
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
    
    # --- Run Routine "Fixation800ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A_image800* updates
        
        # if A_image800 is starting this frame...
        if A_image800.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image800.frameNStart = frameN  # exact frame index
            A_image800.tStart = t  # local t and not account for scr refresh
            A_image800.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image800, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image800.started')
            # update status
            A_image800.status = STARTED
            A_image800.setAutoDraw(True)
        
        # if A_image800 is active this frame...
        if A_image800.status == STARTED:
            # update params
            pass
        
        # if A_image800 is stopping this frame...
        if A_image800.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                A_image800.tStop = t  # not accounting for scr refresh
                A_image800.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image800.stopped')
                # update status
                A_image800.status = FINISHED
                A_image800.setAutoDraw(False)
        
        # *A_kosul* updates
        
        # if A_kosul is starting this frame...
        if A_kosul.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_kosul.frameNStart = frameN  # exact frame index
            A_kosul.tStart = t  # local t and not account for scr refresh
            A_kosul.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_kosul, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_kosul.started')
            # update status
            A_kosul.status = STARTED
            A_kosul.setAutoDraw(True)
        
        # if A_kosul is active this frame...
        if A_kosul.status == STARTED:
            # update params
            pass
        
        # if A_kosul is stopping this frame...
        if A_kosul.status == STARTED:
            if frameN >= (A_kosul.frameNStart + 48):
                # keep track of stop time/frame for later
                A_kosul.tStop = t  # not accounting for scr refresh
                A_kosul.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_kosul.stopped')
                # update status
                A_kosul.status = FINISHED
                A_kosul.setAutoDraw(False)
        
        # *A_cevap* updates
        
        # if A_cevap is starting this frame...
        if A_cevap.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            A_cevap.frameNStart = frameN  # exact frame index
            A_cevap.tStart = t  # local t and not account for scr refresh
            A_cevap.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_cevap, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_cevap.started')
            # update status
            A_cevap.status = STARTED
            A_cevap.setAutoDraw(True)
        
        # if A_cevap is active this frame...
        if A_cevap.status == STARTED:
            # update params
            pass
        
        # if A_cevap is stopping this frame...
        if A_cevap.status == STARTED:
            if frameN >= (A_cevap.frameNStart + 48):
                # keep track of stop time/frame for later
                A_cevap.tStop = t  # not accounting for scr refresh
                A_cevap.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_cevap.stopped')
                # update status
                A_cevap.status = FINISHED
                A_cevap.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation800msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation800ms" ---
    for thisComponent in Fixation800msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from A_code800
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
    # the Routine "Fixation800ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "VWMLoad200ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    A_image1.setColor([r1,g1,b1], colorSpace='rgb')
    A_image2.setColor([r2,g2,b2], colorSpace='rgb')
    A_image3.setColor([r3,g3,b3], colorSpace='rgb')
    A_image4.setColor([r4,g4,b4], colorSpace='rgb')
    A_image5.setColor([r5,g5,b5], colorSpace='rgb')
    A_image6.setColor([r6,g6,b6], colorSpace='rgb')
    # Run 'Begin Routine' code from A_code200
    if A_kosul.text == "LL":
        A_image5.size = (0.053, 0.093)
        A_image6.size = (0.053, 0.093)
    elif A_kosul.text == "HL": 
        A_image1.size = (0.053, 0.093)
        A_image2.size = (0.053, 0.093)
        A_image3.size = (0.053, 0.093)
        A_image4.size = (0.053, 0.093)
    elif A_kosul.text == "LS": 
        A_image5.size = (0.053, 0.093)
        A_image6.size = (0.053, 0.093)
    # keep track of which components have finished
    VWMLoad200msComponents = [A_Background1, A_image1, A_image2, A_image3, A_image4, A_image5, A_image6]
    for thisComponent in VWMLoad200msComponents:
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
    
    # --- Run Routine "VWMLoad200ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A_Background1* updates
        
        # if A_Background1 is starting this frame...
        if A_Background1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Background1.frameNStart = frameN  # exact frame index
            A_Background1.tStart = t  # local t and not account for scr refresh
            A_Background1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Background1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Background1.started')
            # update status
            A_Background1.status = STARTED
            A_Background1.setAutoDraw(True)
        
        # if A_Background1 is active this frame...
        if A_Background1.status == STARTED:
            # update params
            pass
        
        # if A_Background1 is stopping this frame...
        if A_Background1.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_Background1.tStop = t  # not accounting for scr refresh
                A_Background1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_Background1.stopped')
                # update status
                A_Background1.status = FINISHED
                A_Background1.setAutoDraw(False)
        
        # *A_image1* updates
        
        # if A_image1 is starting this frame...
        if A_image1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image1.frameNStart = frameN  # exact frame index
            A_image1.tStart = t  # local t and not account for scr refresh
            A_image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image1.started')
            # update status
            A_image1.status = STARTED
            A_image1.setAutoDraw(True)
        
        # if A_image1 is active this frame...
        if A_image1.status == STARTED:
            # update params
            pass
        
        # if A_image1 is stopping this frame...
        if A_image1.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_image1.tStop = t  # not accounting for scr refresh
                A_image1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image1.stopped')
                # update status
                A_image1.status = FINISHED
                A_image1.setAutoDraw(False)
        
        # *A_image2* updates
        
        # if A_image2 is starting this frame...
        if A_image2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image2.frameNStart = frameN  # exact frame index
            A_image2.tStart = t  # local t and not account for scr refresh
            A_image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image2.started')
            # update status
            A_image2.status = STARTED
            A_image2.setAutoDraw(True)
        
        # if A_image2 is active this frame...
        if A_image2.status == STARTED:
            # update params
            pass
        
        # if A_image2 is stopping this frame...
        if A_image2.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_image2.tStop = t  # not accounting for scr refresh
                A_image2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image2.stopped')
                # update status
                A_image2.status = FINISHED
                A_image2.setAutoDraw(False)
        
        # *A_image3* updates
        
        # if A_image3 is starting this frame...
        if A_image3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image3.frameNStart = frameN  # exact frame index
            A_image3.tStart = t  # local t and not account for scr refresh
            A_image3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image3.started')
            # update status
            A_image3.status = STARTED
            A_image3.setAutoDraw(True)
        
        # if A_image3 is active this frame...
        if A_image3.status == STARTED:
            # update params
            pass
        
        # if A_image3 is stopping this frame...
        if A_image3.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_image3.tStop = t  # not accounting for scr refresh
                A_image3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image3.stopped')
                # update status
                A_image3.status = FINISHED
                A_image3.setAutoDraw(False)
        
        # *A_image4* updates
        
        # if A_image4 is starting this frame...
        if A_image4.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image4.frameNStart = frameN  # exact frame index
            A_image4.tStart = t  # local t and not account for scr refresh
            A_image4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image4.started')
            # update status
            A_image4.status = STARTED
            A_image4.setAutoDraw(True)
        
        # if A_image4 is active this frame...
        if A_image4.status == STARTED:
            # update params
            pass
        
        # if A_image4 is stopping this frame...
        if A_image4.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_image4.tStop = t  # not accounting for scr refresh
                A_image4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image4.stopped')
                # update status
                A_image4.status = FINISHED
                A_image4.setAutoDraw(False)
        
        # *A_image5* updates
        
        # if A_image5 is starting this frame...
        if A_image5.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image5.frameNStart = frameN  # exact frame index
            A_image5.tStart = t  # local t and not account for scr refresh
            A_image5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image5.started')
            # update status
            A_image5.status = STARTED
            A_image5.setAutoDraw(True)
        
        # if A_image5 is active this frame...
        if A_image5.status == STARTED:
            # update params
            pass
        
        # if A_image5 is stopping this frame...
        if A_image5.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_image5.tStop = t  # not accounting for scr refresh
                A_image5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image5.stopped')
                # update status
                A_image5.status = FINISHED
                A_image5.setAutoDraw(False)
        
        # *A_image6* updates
        
        # if A_image6 is starting this frame...
        if A_image6.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image6.frameNStart = frameN  # exact frame index
            A_image6.tStart = t  # local t and not account for scr refresh
            A_image6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image6.started')
            # update status
            A_image6.status = STARTED
            A_image6.setAutoDraw(True)
        
        # if A_image6 is active this frame...
        if A_image6.status == STARTED:
            # update params
            pass
        
        # if A_image6 is stopping this frame...
        if A_image6.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                A_image6.tStop = t  # not accounting for scr refresh
                A_image6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image6.stopped')
                # update status
                A_image6.status = FINISHED
                A_image6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VWMLoad200msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VWMLoad200ms" ---
    for thisComponent in VWMLoad200msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "VWMLoad200ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "BlankScreen2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankScreen2000msComponents = [A_image]
    for thisComponent in BlankScreen2000msComponents:
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
    
    # --- Run Routine "BlankScreen2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A_image* updates
        
        # if A_image is starting this frame...
        if A_image.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image.frameNStart = frameN  # exact frame index
            A_image.tStart = t  # local t and not account for scr refresh
            A_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image.started')
            # update status
            A_image.status = STARTED
            A_image.setAutoDraw(True)
        
        # if A_image is active this frame...
        if A_image.status == STARTED:
            # update params
            pass
        
        # if A_image is stopping this frame...
        if A_image.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                A_image.tStop = t  # not accounting for scr refresh
                A_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_image.stopped')
                # update status
                A_image.status = FINISHED
                A_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreen2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen2000ms" ---
    for thisComponent in BlankScreen2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BlankScreen2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Flanker2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    A_Hedef.setPos(pozisyonhedef)
    A_Hedef.setText(hedef)
    A_Celdirici.setPos(pozisyonceldirici)
    A_Celdirici.setText(celdirici)
    A_Key.keys = []
    A_Key.rt = []
    _A_Key_allKeys = []
    A_Sound.setSound('yanlis.wav', hamming=True)
    A_Sound.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from A_code2000_flanker
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(2000 / FRate)
    frame = 0
    # keep track of which components have finished
    Flanker2000msComponents = [A_Background2, A_Hedef, A_Celdirici, A_Key, A_Sound]
    for thisComponent in Flanker2000msComponents:
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
    
    # --- Run Routine "Flanker2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A_Background2* updates
        
        # if A_Background2 is starting this frame...
        if A_Background2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Background2.frameNStart = frameN  # exact frame index
            A_Background2.tStart = t  # local t and not account for scr refresh
            A_Background2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Background2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Background2.started')
            # update status
            A_Background2.status = STARTED
            A_Background2.setAutoDraw(True)
        
        # if A_Background2 is active this frame...
        if A_Background2.status == STARTED:
            # update params
            pass
        
        # if A_Background2 is stopping this frame...
        if A_Background2.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                A_Background2.tStop = t  # not accounting for scr refresh
                A_Background2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_Background2.stopped')
                # update status
                A_Background2.status = FINISHED
                A_Background2.setAutoDraw(False)
        
        # *A_Hedef* updates
        
        # if A_Hedef is starting this frame...
        if A_Hedef.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Hedef.frameNStart = frameN  # exact frame index
            A_Hedef.tStart = t  # local t and not account for scr refresh
            A_Hedef.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Hedef, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Hedef.started')
            # update status
            A_Hedef.status = STARTED
            A_Hedef.setAutoDraw(True)
        
        # if A_Hedef is active this frame...
        if A_Hedef.status == STARTED:
            # update params
            pass
        
        # if A_Hedef is stopping this frame...
        if A_Hedef.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                A_Hedef.tStop = t  # not accounting for scr refresh
                A_Hedef.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_Hedef.stopped')
                # update status
                A_Hedef.status = FINISHED
                A_Hedef.setAutoDraw(False)
        
        # *A_Celdirici* updates
        
        # if A_Celdirici is starting this frame...
        if A_Celdirici.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Celdirici.frameNStart = frameN  # exact frame index
            A_Celdirici.tStart = t  # local t and not account for scr refresh
            A_Celdirici.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Celdirici, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Celdirici.started')
            # update status
            A_Celdirici.status = STARTED
            A_Celdirici.setAutoDraw(True)
        
        # if A_Celdirici is active this frame...
        if A_Celdirici.status == STARTED:
            # update params
            pass
        
        # if A_Celdirici is stopping this frame...
        if A_Celdirici.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                A_Celdirici.tStop = t  # not accounting for scr refresh
                A_Celdirici.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_Celdirici.stopped')
                # update status
                A_Celdirici.status = FINISHED
                A_Celdirici.setAutoDraw(False)
        
        # *A_Key* updates
        waitOnFlip = False
        
        # if A_Key is starting this frame...
        if A_Key.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Key.frameNStart = frameN  # exact frame index
            A_Key.tStart = t  # local t and not account for scr refresh
            A_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Key.started')
            # update status
            A_Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(A_Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(A_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if A_Key is stopping this frame...
        if A_Key.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                A_Key.tStop = t  # not accounting for scr refresh
                A_Key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_Key.stopped')
                # update status
                A_Key.status = FINISHED
                A_Key.status = FINISHED
        if A_Key.status == STARTED and not waitOnFlip:
            theseKeys = A_Key.getKeys(keyList=['x','z','n'], waitRelease=False)
            _A_Key_allKeys.extend(theseKeys)
            if len(_A_Key_allKeys):
                A_Key.keys = _A_Key_allKeys[-1].name  # just the last key pressed
                A_Key.rt = _A_Key_allKeys[-1].rt
                # was this correct?
                if (A_Key.keys == str(flankercevap)) or (A_Key.keys == flankercevap):
                    A_Key.corr = 1
                else:
                    A_Key.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop A_Sound
        # Run 'Each Frame' code from A_code2000_flanker
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
        for thisComponent in Flanker2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Flanker2000ms" ---
    for thisComponent in Flanker2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if A_Key.keys in ['', [], None]:  # No response was made
        A_Key.keys = None
        # was no response the correct answer?!
        if str(flankercevap).lower() == 'none':
           A_Key.corr = 1;  # correct non-response
        else:
           A_Key.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopAlistirma (TrialHandler)
    LoopAlistirma.addData('A_Key.keys',A_Key.keys)
    LoopAlistirma.addData('A_Key.corr', A_Key.corr)
    if A_Key.keys != None:  # we had a response
        LoopAlistirma.addData('A_Key.rt', A_Key.rt)
    A_Sound.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from A_code2000_flanker
    if A_Key.keys == None:
        A_Sound.play()
    # the Routine "Flanker2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FlankerFixation500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    FlankerFixation500msComponents = [A_500]
    for thisComponent in FlankerFixation500msComponents:
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
    
    # --- Run Routine "FlankerFixation500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A_500* updates
        
        # if A_500 is starting this frame...
        if A_500.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_500.frameNStart = frameN  # exact frame index
            A_500.tStart = t  # local t and not account for scr refresh
            A_500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_500.started')
            # update status
            A_500.status = STARTED
            A_500.setAutoDraw(True)
        
        # if A_500 is active this frame...
        if A_500.status == STARTED:
            # update params
            pass
        
        # if A_500 is stopping this frame...
        if A_500.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                A_500.tStop = t  # not accounting for scr refresh
                A_500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'A_500.stopped')
                # update status
                A_500.status = FINISHED
                A_500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FlankerFixation500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FlankerFixation500ms" ---
    for thisComponent in FlankerFixation500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "FlankerFixation500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "VWMLoadTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    A_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
    A_image2_2.setColor([r2,g2,b2], colorSpace='rgb')
    A_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
    A_image4_2.setColor([r4,g4,b4], colorSpace='rgb')
    A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
    A_image6_2.setColor([r6,g6,b6], colorSpace='rgb')
    A_Key_2.keys = []
    A_Key_2.rt = []
    _A_Key_2_allKeys = []
    A_Sound_2.setSound('yanlis.wav', hamming=True)
    A_Sound_2.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from A_Code_VWM
    A_image1_2.size = (0, 0)
    A_image2_2.size = (0, 0)
    A_image3_2.size = (0, 0)
    A_image4_2.size = (0, 0)
    A_image5_2.size = (0, 0)
    A_image6_2.size = (0, 0)
    A_Poli1.size = (0, 0)
    A_Poli2.size = (0, 0)
    A_Poli3.size = (0, 0)
    A_Poli4.size = (0, 0)
    A_Poli5.size = (0, 0)
    A_Poli6.size = (0, 0)
    
    if A_kosul.text == "LL":
        if A_cevap.text == "ö":
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0.053, 0.093)
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0, 0)
                A_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0.053, 0.093)
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0, 0)
                A_Poli5.size = (0.053, 0.093)
        
        if A_cevap.text == "ç":
            r5 = float(round(r5,4)) + 0.5333
            g5 = float(round(g5,4)) + 0.5333
            b5 = float(round(b5,4)) + 0.5333
            
            r6 = float(round(r6,4)) + 0.5333
            g6 = float(round(g6,4)) + 0.5333
            b6 = float(round(b6,4)) + 0.5333
            
            if r5 > 1:
                r5 = r5 - 0.5333
                p1 = 1 - r5
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r5 = -float(round(p4,4))
                
            if g5 > 1:
                g5 = g5 - 0.5333
                p1 = 1 - g5
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g5 = -float(round(p4,4))
                
            if b5 > 1:
                b5 = b5 - 0.5333
                p1 = 1 - b5
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b5 = -float(round(p4,4))
                
            if r6 > 1:
                r6 = r6 - 0.5333
                p1 = 1 - r6
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r6 = -float(round(p4,4))
                
            if g6 > 1:
                g6 = g6 - 0.5333
                p1 = 1 - g6
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g6 = -float(round(p4,4))
                
            if b6 > 1:
                b6 = b6 - 0.5333
                p1 = 1 - b6
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b6 = -float(round(p4,4))
            
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0.053, 0.093)
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0, 0)
                A_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0.053, 0.093)
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0, 0)
                A_Poli5.size = (0.053, 0.093)
                
    
    elif A_kosul.text == "HL": 
        if A_cevap.text == "ö":
            dizi = [1,2,3,4]
            shuffle(dizi)
            if dizi[0] == 1:
                A_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                A_image1_2.size = (0.053, 0.093)
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0, 0)
                A_Poli2.size = (0.053, 0.093)
                A_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                A_image3_2.size = (0, 0)
                A_Poli3.size = (0.053, 0.093)
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0, 0)
                A_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 2:
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0.053, 0.093)
                A_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                A_image1_2.size = (0, 0)
                A_Poli1.size = (0.053, 0.093)
                A_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                A_image3_2.size = (0, 0)
                A_Poli3.size = (0.053, 0.093)
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0, 0)
                A_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 3:
                A_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                A_image3_2.size = (0.053, 0.093)
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0, 0)
                A_Poli4.size = (0.053, 0.093)
                A_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                A_image1_2.size = (0, 0)
                A_Poli1.size = (0.053, 0.093)
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0, 0)
                A_Poli2.size = (0.053, 0.093)
            elif dizi[0] == 4:
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0.053, 0.093)
                A_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                A_image3_2.size = (0, 0)
                A_Poli3.size = (0.053, 0.093)
                A_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                A_image1_2.size = (0, 0)
                A_Poli1.size = (0.053, 0.093)
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0, 0)
                A_Poli2.size = (0.053, 0.093)
        
        if A_cevap.text == "ç":
            r1 = float(round(r1,4)) + 0.5333
            g1 = float(round(g1,4)) + 0.5333
            b1 = float(round(b1,4)) + 0.5333
            
            r2 = float(round(r2,4)) + 0.5333
            g2 = float(round(g2,4)) + 0.5333
            b2 = float(round(b2,4)) + 0.5333
            
            r3 = float(round(r3,4)) + 0.5333
            g3 = float(round(g3,4)) + 0.5333
            b3 = float(round(b3,4)) + 0.5333
            
            r4 = float(round(r4,4)) + 0.5333
            g4 = float(round(g4,4)) + 0.5333
            b4 = float(round(b4,4)) + 0.5333
            
            if r1 > 1:
                r1 = r1 - 0.5333
                p1 = 1 - r1
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r1 = -float(round(p4,4))
                
            if g1 > 1:
                g1 = g1 - 0.5333
                p1 = 1 - g1
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g1 = -float(round(p4,4))
                
            if b1 > 1:
                b1 = b1 - 0.5333
                p1 = 1 - b1
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b1 = -float(round(p4,4))
                
            if r2 > 1:
                r2 = r2 - 0.5333
                p1 = 1 - r2
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r2 = -float(round(p4,4))
                
            if g2 > 1:
                g2 = g2 - 0.5333
                p1 = 1 - g2
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g2 = -float(round(p4,4))
                
            if b2 > 1:
                b2 = b2 - 0.5333
                p1 = 1 - b2
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b2 = -float(round(p4,4))
                
            if r3 > 1:
                r3 = r3 - 0.5333
                p1 = 1 - r3
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r3 = -float(round(p4,4))
                
            if g3 > 1:
                g3 = g3 - 0.5333
                p1 = 1 - g3
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g3 = -float(round(p4,4))
                
            if b3 > 1:
                b3 = b3 - 0.5333
                p1 = 1 - b3
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b3 = -float(round(p4,4))
                
            if r4 > 1:
                r4 = r4 - 0.5333
                p1 = 1 - r4
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r4 = -float(round(p4,4))
                
            if g4 > 1:
                g4 = g4 - 0.5333
                p1 = 1 - g4
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g4 = -float(round(p4,4))
                
            if b4 > 1:
                b4 = b4 - 0.5333
                p1 = 1 - b4
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b4 = -float(round(p4,4))
    
            dizi = [1,2,3,4]
            shuffle(dizi)
            if dizi[0] == 1:
                A_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                A_image1_2.size = (0.053, 0.093)
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0, 0)
                A_Poli2.size = (0.053, 0.093)
                A_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                A_image3_2.size = (0, 0)
                A_Poli3.size = (0.053, 0.093)
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0, 0)
                A_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 2:
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0.053, 0.093)
                A_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                A_image1_2.size = (0, 0)
                A_Poli1.size = (0.053, 0.093)
                A_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                A_image3_2.size = (0, 0)
                A_Poli3.size = (0.053, 0.093)
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0, 0)
                A_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 3:
                A_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                A_image3_2.size = (0.053, 0.093)
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0, 0)
                A_Poli4.size = (0.053, 0.093)
                A_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                A_image1_2.size = (0, 0)
                A_Poli1.size = (0.053, 0.093)
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0, 0)
                A_Poli2.size = (0.053, 0.093)
            elif dizi[0] == 4:
                A_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                A_image4_2.size = (0.053, 0.093)
                A_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                A_image3_2.size = (0, 0)
                A_Poli3.size = (0.053, 0.093)
                A_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                A_image1_2.size = (0, 0)
                A_Poli1.size = (0.053, 0.093)
                A_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                A_image2_2.size = (0, 0)
                A_Poli2.size = (0.053, 0.093)
    
    elif A_kosul.text == "LS": 
        if A_cevap.text == "ö":
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0.053, 0.093)
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0, 0)
                A_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0.053, 0.093)
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0, 0)
                A_Poli5.size = (0.053, 0.093)
    
        if A_cevap.text == "ç":
            r5 = float(round(r5,4)) + 0.1333
            g5 = float(round(g5,4)) + 0.1333
            b5 = float(round(b5,4)) + 0.1333
            
            r6 = float(round(r6,4)) + 0.1333
            g6 = float(round(g6,4)) + 0.1333
            b6 = float(round(b6,4)) + 0.1333
            
            if r5 > 1:
                r5 = r5 - 0.1333
                p1 = 1 - r5
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r5 = -float(round(p4,4))
                
            if g5 > 1:
                g5 = g5 - 0.1333
                p1 = 1 - g5
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g5 = -float(round(p4,4))
                
            if b5 > 1:
                b5 = b5 - 0.1333
                p1 = 1 - b5
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b5 = -float(round(p4,4))
                
            if r6 > 1:
                r6 = r6 - 0.1333
                p1 = 1 - r6
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r6 = -float(round(p4,4))
                
            if g6 > 1:
                g6 = g6 - 0.1333
                p1 = 1 - g6
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g6 = -float(round(p4,4))
                
            if b6 > 1:
                b6 = b6 - 0.1333
                p1 = 1 - b6
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b6 = -float(round(p4,4))
    
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0.053, 0.093)
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0, 0)
                A_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                A_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                A_image6_2.size = (0.053, 0.093)
                A_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                A_image5_2.size = (0, 0)
                A_Poli5.size = (0.053, 0.093)
    # keep track of which components have finished
    VWMLoadTaskComponents = [A_Background1_2, A_image1_2, A_image2_2, A_image3_2, A_image4_2, A_image5_2, A_image6_2, A_Poli1, A_Poli2, A_Poli3, A_Poli4, A_Poli5, A_Poli6, A_Key_2, A_Sound_2]
    for thisComponent in VWMLoadTaskComponents:
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
    
    # --- Run Routine "VWMLoadTask" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A_Background1_2* updates
        
        # if A_Background1_2 is starting this frame...
        if A_Background1_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Background1_2.frameNStart = frameN  # exact frame index
            A_Background1_2.tStart = t  # local t and not account for scr refresh
            A_Background1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Background1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Background1_2.started')
            # update status
            A_Background1_2.status = STARTED
            A_Background1_2.setAutoDraw(True)
        
        # if A_Background1_2 is active this frame...
        if A_Background1_2.status == STARTED:
            # update params
            pass
        
        # *A_image1_2* updates
        
        # if A_image1_2 is starting this frame...
        if A_image1_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image1_2.frameNStart = frameN  # exact frame index
            A_image1_2.tStart = t  # local t and not account for scr refresh
            A_image1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image1_2.started')
            # update status
            A_image1_2.status = STARTED
            A_image1_2.setAutoDraw(True)
        
        # if A_image1_2 is active this frame...
        if A_image1_2.status == STARTED:
            # update params
            pass
        
        # *A_image2_2* updates
        
        # if A_image2_2 is starting this frame...
        if A_image2_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image2_2.frameNStart = frameN  # exact frame index
            A_image2_2.tStart = t  # local t and not account for scr refresh
            A_image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image2_2.started')
            # update status
            A_image2_2.status = STARTED
            A_image2_2.setAutoDraw(True)
        
        # if A_image2_2 is active this frame...
        if A_image2_2.status == STARTED:
            # update params
            pass
        
        # *A_image3_2* updates
        
        # if A_image3_2 is starting this frame...
        if A_image3_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image3_2.frameNStart = frameN  # exact frame index
            A_image3_2.tStart = t  # local t and not account for scr refresh
            A_image3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image3_2.started')
            # update status
            A_image3_2.status = STARTED
            A_image3_2.setAutoDraw(True)
        
        # if A_image3_2 is active this frame...
        if A_image3_2.status == STARTED:
            # update params
            pass
        
        # *A_image4_2* updates
        
        # if A_image4_2 is starting this frame...
        if A_image4_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image4_2.frameNStart = frameN  # exact frame index
            A_image4_2.tStart = t  # local t and not account for scr refresh
            A_image4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image4_2.started')
            # update status
            A_image4_2.status = STARTED
            A_image4_2.setAutoDraw(True)
        
        # if A_image4_2 is active this frame...
        if A_image4_2.status == STARTED:
            # update params
            pass
        
        # *A_image5_2* updates
        
        # if A_image5_2 is starting this frame...
        if A_image5_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image5_2.frameNStart = frameN  # exact frame index
            A_image5_2.tStart = t  # local t and not account for scr refresh
            A_image5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image5_2.started')
            # update status
            A_image5_2.status = STARTED
            A_image5_2.setAutoDraw(True)
        
        # if A_image5_2 is active this frame...
        if A_image5_2.status == STARTED:
            # update params
            pass
        
        # *A_image6_2* updates
        
        # if A_image6_2 is starting this frame...
        if A_image6_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_image6_2.frameNStart = frameN  # exact frame index
            A_image6_2.tStart = t  # local t and not account for scr refresh
            A_image6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_image6_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_image6_2.started')
            # update status
            A_image6_2.status = STARTED
            A_image6_2.setAutoDraw(True)
        
        # if A_image6_2 is active this frame...
        if A_image6_2.status == STARTED:
            # update params
            pass
        
        # *A_Poli1* updates
        
        # if A_Poli1 is starting this frame...
        if A_Poli1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Poli1.frameNStart = frameN  # exact frame index
            A_Poli1.tStart = t  # local t and not account for scr refresh
            A_Poli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Poli1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Poli1.started')
            # update status
            A_Poli1.status = STARTED
            A_Poli1.setAutoDraw(True)
        
        # if A_Poli1 is active this frame...
        if A_Poli1.status == STARTED:
            # update params
            pass
        
        # *A_Poli2* updates
        
        # if A_Poli2 is starting this frame...
        if A_Poli2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Poli2.frameNStart = frameN  # exact frame index
            A_Poli2.tStart = t  # local t and not account for scr refresh
            A_Poli2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Poli2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Poli2.started')
            # update status
            A_Poli2.status = STARTED
            A_Poli2.setAutoDraw(True)
        
        # if A_Poli2 is active this frame...
        if A_Poli2.status == STARTED:
            # update params
            pass
        
        # *A_Poli3* updates
        
        # if A_Poli3 is starting this frame...
        if A_Poli3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Poli3.frameNStart = frameN  # exact frame index
            A_Poli3.tStart = t  # local t and not account for scr refresh
            A_Poli3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Poli3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Poli3.started')
            # update status
            A_Poli3.status = STARTED
            A_Poli3.setAutoDraw(True)
        
        # if A_Poli3 is active this frame...
        if A_Poli3.status == STARTED:
            # update params
            pass
        
        # *A_Poli4* updates
        
        # if A_Poli4 is starting this frame...
        if A_Poli4.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Poli4.frameNStart = frameN  # exact frame index
            A_Poli4.tStart = t  # local t and not account for scr refresh
            A_Poli4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Poli4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Poli4.started')
            # update status
            A_Poli4.status = STARTED
            A_Poli4.setAutoDraw(True)
        
        # if A_Poli4 is active this frame...
        if A_Poli4.status == STARTED:
            # update params
            pass
        
        # *A_Poli5* updates
        
        # if A_Poli5 is starting this frame...
        if A_Poli5.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Poli5.frameNStart = frameN  # exact frame index
            A_Poli5.tStart = t  # local t and not account for scr refresh
            A_Poli5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Poli5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Poli5.started')
            # update status
            A_Poli5.status = STARTED
            A_Poli5.setAutoDraw(True)
        
        # if A_Poli5 is active this frame...
        if A_Poli5.status == STARTED:
            # update params
            pass
        
        # *A_Poli6* updates
        
        # if A_Poli6 is starting this frame...
        if A_Poli6.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Poli6.frameNStart = frameN  # exact frame index
            A_Poli6.tStart = t  # local t and not account for scr refresh
            A_Poli6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Poli6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Poli6.started')
            # update status
            A_Poli6.status = STARTED
            A_Poli6.setAutoDraw(True)
        
        # if A_Poli6 is active this frame...
        if A_Poli6.status == STARTED:
            # update params
            pass
        
        # *A_Key_2* updates
        waitOnFlip = False
        
        # if A_Key_2 is starting this frame...
        if A_Key_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            A_Key_2.frameNStart = frameN  # exact frame index
            A_Key_2.tStart = t  # local t and not account for scr refresh
            A_Key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_Key_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'A_Key_2.started')
            # update status
            A_Key_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(A_Key_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(A_Key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if A_Key_2.status == STARTED and not waitOnFlip:
            theseKeys = A_Key_2.getKeys(keyList=['ö','ç'], waitRelease=False)
            _A_Key_2_allKeys.extend(theseKeys)
            if len(_A_Key_2_allKeys):
                A_Key_2.keys = _A_Key_2_allKeys[-1].name  # just the last key pressed
                A_Key_2.rt = _A_Key_2_allKeys[-1].rt
                # was this correct?
                if (A_Key_2.keys == str(taskcevap)) or (A_Key_2.keys == taskcevap):
                    A_Key_2.corr = 1
                else:
                    A_Key_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop A_Sound_2
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VWMLoadTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VWMLoadTask" ---
    for thisComponent in VWMLoadTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if A_Key_2.keys in ['', [], None]:  # No response was made
        A_Key_2.keys = None
        # was no response the correct answer?!
        if str(taskcevap).lower() == 'none':
           A_Key_2.corr = 1;  # correct non-response
        else:
           A_Key_2.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopAlistirma (TrialHandler)
    LoopAlistirma.addData('A_Key_2.keys',A_Key_2.keys)
    LoopAlistirma.addData('A_Key_2.corr', A_Key_2.corr)
    if A_Key_2.keys != None:  # we had a response
        LoopAlistirma.addData('A_Key_2.rt', A_Key_2.rt)
    A_Sound_2.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from A_Code_VWM
    if A_Key_2.corr == 0:
        A_Sound_2.play()
        
    if counter == 16:
        LoopAlistirma.finished = True
    # the Routine "VWMLoadTask" was not non-slip safe, so reset the non-slip timer
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

# --- Prepare to start Routine "DeneyGecis" ---
continueRoutine = True
# update component parameters for each repeat
KDYonerge.keys = []
KDYonerge.rt = []
_KDYonerge_allKeys = []
# keep track of which components have finished
DeneyGecisComponents = [KDYonerge, TDYonerge]
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
    
    # *KDYonerge* updates
    waitOnFlip = False
    
    # if KDYonerge is starting this frame...
    if KDYonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KDYonerge.frameNStart = frameN  # exact frame index
        KDYonerge.tStart = t  # local t and not account for scr refresh
        KDYonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KDYonerge, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KDYonerge.started')
        # update status
        KDYonerge.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KDYonerge.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KDYonerge.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KDYonerge.status == STARTED and not waitOnFlip:
        theseKeys = KDYonerge.getKeys(keyList=None, waitRelease=False)
        _KDYonerge_allKeys.extend(theseKeys)
        if len(_KDYonerge_allKeys):
            KDYonerge.keys = _KDYonerge_allKeys[-1].name  # just the last key pressed
            KDYonerge.rt = _KDYonerge_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *TDYonerge* updates
    
    # if TDYonerge is starting this frame...
    if TDYonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TDYonerge.frameNStart = frameN  # exact frame index
        TDYonerge.tStart = t  # local t and not account for scr refresh
        TDYonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TDYonerge, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TDYonerge.started')
        # update status
        TDYonerge.status = STARTED
        TDYonerge.setAutoDraw(True)
    
    # if TDYonerge is active this frame...
    if TDYonerge.status == STARTED:
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
if KDYonerge.keys in ['', [], None]:  # No response was made
    KDYonerge.keys = None
thisExp.addData('KDYonerge.keys',KDYonerge.keys)
if KDYonerge.keys != None:  # we had a response
    thisExp.addData('KDYonerge.rt', KDYonerge.rt)
thisExp.nextEntry()
# the Routine "DeneyGecis" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopDeney = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('replication_of_zhang_and_luck.xlsx'),
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
    
    # --- Prepare to start Routine "D_Fixation800ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    D_kosul.setText(condition)
    D_cevap.setText(taskcevap)
    # keep track of which components have finished
    D_Fixation800msComponents = [D_image800, D_kosul, D_cevap]
    for thisComponent in D_Fixation800msComponents:
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
    
    # --- Run Routine "D_Fixation800ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *D_image800* updates
        
        # if D_image800 is starting this frame...
        if D_image800.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image800.frameNStart = frameN  # exact frame index
            D_image800.tStart = t  # local t and not account for scr refresh
            D_image800.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image800, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image800.started')
            # update status
            D_image800.status = STARTED
            D_image800.setAutoDraw(True)
        
        # if D_image800 is active this frame...
        if D_image800.status == STARTED:
            # update params
            pass
        
        # if D_image800 is stopping this frame...
        if D_image800.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                D_image800.tStop = t  # not accounting for scr refresh
                D_image800.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image800.stopped')
                # update status
                D_image800.status = FINISHED
                D_image800.setAutoDraw(False)
        
        # *D_kosul* updates
        
        # if D_kosul is starting this frame...
        if D_kosul.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_kosul.frameNStart = frameN  # exact frame index
            D_kosul.tStart = t  # local t and not account for scr refresh
            D_kosul.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_kosul, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_kosul.started')
            # update status
            D_kosul.status = STARTED
            D_kosul.setAutoDraw(True)
        
        # if D_kosul is active this frame...
        if D_kosul.status == STARTED:
            # update params
            pass
        
        # if D_kosul is stopping this frame...
        if D_kosul.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                D_kosul.tStop = t  # not accounting for scr refresh
                D_kosul.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_kosul.stopped')
                # update status
                D_kosul.status = FINISHED
                D_kosul.setAutoDraw(False)
        
        # *D_cevap* updates
        
        # if D_cevap is starting this frame...
        if D_cevap.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_cevap.frameNStart = frameN  # exact frame index
            D_cevap.tStart = t  # local t and not account for scr refresh
            D_cevap.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_cevap, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_cevap.started')
            # update status
            D_cevap.status = STARTED
            D_cevap.setAutoDraw(True)
        
        # if D_cevap is active this frame...
        if D_cevap.status == STARTED:
            # update params
            pass
        
        # if D_cevap is stopping this frame...
        if D_cevap.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                D_cevap.tStop = t  # not accounting for scr refresh
                D_cevap.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_cevap.stopped')
                # update status
                D_cevap.status = FINISHED
                D_cevap.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in D_Fixation800msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "D_Fixation800ms" ---
    for thisComponent in D_Fixation800msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from D_code800
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
    # the Routine "D_Fixation800ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "D_VWMLoad200ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    D_image1.setColor([r1,g1,b1], colorSpace='rgb')
    D_image2.setColor([r2,g2,b2], colorSpace='rgb')
    D_image3.setColor([r3,g3,b3], colorSpace='rgb')
    D_image4.setColor([r4,g4,b4], colorSpace='rgb')
    D_image5.setColor([r5,g5,b5], colorSpace='rgb')
    D_image6.setColor([r6,g6,b6], colorSpace='rgb')
    # Run 'Begin Routine' code from D_code200
    if D_kosul.text == "LL": #LOW LOAD LARGE COLOR CHANGE
        D_image5.size = (0.053, 0.093)
        D_image6.size = (0.053, 0.093)
    elif D_kosul.text == "HL": #HİGH LOAD LARGE COLOR CHANGE
        D_image1.size = (0.053, 0.093)
        D_image2.size = (0.053, 0.093)
        D_image3.size = (0.053, 0.093)
        D_image4.size = (0.053, 0.093)
    elif D_kosul.text == "LS": # LOW LOAD SMALL COLOR CHANGE
        D_image5.size = (0.053, 0.093)
        D_image6.size = (0.053, 0.093)
    # keep track of which components have finished
    D_VWMLoad200msComponents = [D_Background1, D_image1, D_image2, D_image3, D_image4, D_image5, D_image6]
    for thisComponent in D_VWMLoad200msComponents:
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
    
    # --- Run Routine "D_VWMLoad200ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *D_Background1* updates
        
        # if D_Background1 is starting this frame...
        if D_Background1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Background1.frameNStart = frameN  # exact frame index
            D_Background1.tStart = t  # local t and not account for scr refresh
            D_Background1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Background1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Background1.started')
            # update status
            D_Background1.status = STARTED
            D_Background1.setAutoDraw(True)
        
        # if D_Background1 is active this frame...
        if D_Background1.status == STARTED:
            # update params
            pass
        
        # if D_Background1 is stopping this frame...
        if D_Background1.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_Background1.tStop = t  # not accounting for scr refresh
                D_Background1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_Background1.stopped')
                # update status
                D_Background1.status = FINISHED
                D_Background1.setAutoDraw(False)
        
        # *D_image1* updates
        
        # if D_image1 is starting this frame...
        if D_image1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image1.frameNStart = frameN  # exact frame index
            D_image1.tStart = t  # local t and not account for scr refresh
            D_image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image1.started')
            # update status
            D_image1.status = STARTED
            D_image1.setAutoDraw(True)
        
        # if D_image1 is active this frame...
        if D_image1.status == STARTED:
            # update params
            pass
        
        # if D_image1 is stopping this frame...
        if D_image1.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_image1.tStop = t  # not accounting for scr refresh
                D_image1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image1.stopped')
                # update status
                D_image1.status = FINISHED
                D_image1.setAutoDraw(False)
        
        # *D_image2* updates
        
        # if D_image2 is starting this frame...
        if D_image2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image2.frameNStart = frameN  # exact frame index
            D_image2.tStart = t  # local t and not account for scr refresh
            D_image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image2.started')
            # update status
            D_image2.status = STARTED
            D_image2.setAutoDraw(True)
        
        # if D_image2 is active this frame...
        if D_image2.status == STARTED:
            # update params
            pass
        
        # if D_image2 is stopping this frame...
        if D_image2.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_image2.tStop = t  # not accounting for scr refresh
                D_image2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image2.stopped')
                # update status
                D_image2.status = FINISHED
                D_image2.setAutoDraw(False)
        
        # *D_image3* updates
        
        # if D_image3 is starting this frame...
        if D_image3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image3.frameNStart = frameN  # exact frame index
            D_image3.tStart = t  # local t and not account for scr refresh
            D_image3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image3.started')
            # update status
            D_image3.status = STARTED
            D_image3.setAutoDraw(True)
        
        # if D_image3 is active this frame...
        if D_image3.status == STARTED:
            # update params
            pass
        
        # if D_image3 is stopping this frame...
        if D_image3.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_image3.tStop = t  # not accounting for scr refresh
                D_image3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image3.stopped')
                # update status
                D_image3.status = FINISHED
                D_image3.setAutoDraw(False)
        
        # *D_image4* updates
        
        # if D_image4 is starting this frame...
        if D_image4.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image4.frameNStart = frameN  # exact frame index
            D_image4.tStart = t  # local t and not account for scr refresh
            D_image4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image4.started')
            # update status
            D_image4.status = STARTED
            D_image4.setAutoDraw(True)
        
        # if D_image4 is active this frame...
        if D_image4.status == STARTED:
            # update params
            pass
        
        # if D_image4 is stopping this frame...
        if D_image4.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_image4.tStop = t  # not accounting for scr refresh
                D_image4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image4.stopped')
                # update status
                D_image4.status = FINISHED
                D_image4.setAutoDraw(False)
        
        # *D_image5* updates
        
        # if D_image5 is starting this frame...
        if D_image5.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image5.frameNStart = frameN  # exact frame index
            D_image5.tStart = t  # local t and not account for scr refresh
            D_image5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image5.started')
            # update status
            D_image5.status = STARTED
            D_image5.setAutoDraw(True)
        
        # if D_image5 is active this frame...
        if D_image5.status == STARTED:
            # update params
            pass
        
        # if D_image5 is stopping this frame...
        if D_image5.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_image5.tStop = t  # not accounting for scr refresh
                D_image5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image5.stopped')
                # update status
                D_image5.status = FINISHED
                D_image5.setAutoDraw(False)
        
        # *D_image6* updates
        
        # if D_image6 is starting this frame...
        if D_image6.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image6.frameNStart = frameN  # exact frame index
            D_image6.tStart = t  # local t and not account for scr refresh
            D_image6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image6.started')
            # update status
            D_image6.status = STARTED
            D_image6.setAutoDraw(True)
        
        # if D_image6 is active this frame...
        if D_image6.status == STARTED:
            # update params
            pass
        
        # if D_image6 is stopping this frame...
        if D_image6.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                D_image6.tStop = t  # not accounting for scr refresh
                D_image6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image6.stopped')
                # update status
                D_image6.status = FINISHED
                D_image6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in D_VWMLoad200msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "D_VWMLoad200ms" ---
    for thisComponent in D_VWMLoad200msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "D_VWMLoad200ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "D_BlankScreen2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    D_BlankScreen2000msComponents = [D_image]
    for thisComponent in D_BlankScreen2000msComponents:
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
    
    # --- Run Routine "D_BlankScreen2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *D_image* updates
        
        # if D_image is starting this frame...
        if D_image.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image.frameNStart = frameN  # exact frame index
            D_image.tStart = t  # local t and not account for scr refresh
            D_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image.started')
            # update status
            D_image.status = STARTED
            D_image.setAutoDraw(True)
        
        # if D_image is active this frame...
        if D_image.status == STARTED:
            # update params
            pass
        
        # if D_image is stopping this frame...
        if D_image.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                D_image.tStop = t  # not accounting for scr refresh
                D_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_image.stopped')
                # update status
                D_image.status = FINISHED
                D_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in D_BlankScreen2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "D_BlankScreen2000ms" ---
    for thisComponent in D_BlankScreen2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "D_BlankScreen2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "D_Flanker2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    D_Hedef.setPos(pozisyonhedef)
    D_Hedef.setText(hedef)
    D_Celdirici.setPos(pozisyonceldirici)
    D_Celdirici.setText(celdirici)
    D_Key.keys = []
    D_Key.rt = []
    _D_Key_allKeys = []
    D_Sound.setSound('yanlis.wav', hamming=True)
    D_Sound.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from D_code2000_flanker
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(2000 / FRate)
    frame = 0
    # keep track of which components have finished
    D_Flanker2000msComponents = [D_Background2, D_Hedef, D_Celdirici, D_Key, D_Sound]
    for thisComponent in D_Flanker2000msComponents:
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
    
    # --- Run Routine "D_Flanker2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *D_Background2* updates
        
        # if D_Background2 is starting this frame...
        if D_Background2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Background2.frameNStart = frameN  # exact frame index
            D_Background2.tStart = t  # local t and not account for scr refresh
            D_Background2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Background2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Background2.started')
            # update status
            D_Background2.status = STARTED
            D_Background2.setAutoDraw(True)
        
        # if D_Background2 is active this frame...
        if D_Background2.status == STARTED:
            # update params
            pass
        
        # if D_Background2 is stopping this frame...
        if D_Background2.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                D_Background2.tStop = t  # not accounting for scr refresh
                D_Background2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_Background2.stopped')
                # update status
                D_Background2.status = FINISHED
                D_Background2.setAutoDraw(False)
        
        # *D_Hedef* updates
        
        # if D_Hedef is starting this frame...
        if D_Hedef.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Hedef.frameNStart = frameN  # exact frame index
            D_Hedef.tStart = t  # local t and not account for scr refresh
            D_Hedef.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Hedef, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Hedef.started')
            # update status
            D_Hedef.status = STARTED
            D_Hedef.setAutoDraw(True)
        
        # if D_Hedef is active this frame...
        if D_Hedef.status == STARTED:
            # update params
            pass
        
        # if D_Hedef is stopping this frame...
        if D_Hedef.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                D_Hedef.tStop = t  # not accounting for scr refresh
                D_Hedef.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_Hedef.stopped')
                # update status
                D_Hedef.status = FINISHED
                D_Hedef.setAutoDraw(False)
        
        # *D_Celdirici* updates
        
        # if D_Celdirici is starting this frame...
        if D_Celdirici.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Celdirici.frameNStart = frameN  # exact frame index
            D_Celdirici.tStart = t  # local t and not account for scr refresh
            D_Celdirici.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Celdirici, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Celdirici.started')
            # update status
            D_Celdirici.status = STARTED
            D_Celdirici.setAutoDraw(True)
        
        # if D_Celdirici is active this frame...
        if D_Celdirici.status == STARTED:
            # update params
            pass
        
        # if D_Celdirici is stopping this frame...
        if D_Celdirici.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                D_Celdirici.tStop = t  # not accounting for scr refresh
                D_Celdirici.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_Celdirici.stopped')
                # update status
                D_Celdirici.status = FINISHED
                D_Celdirici.setAutoDraw(False)
        
        # *D_Key* updates
        waitOnFlip = False
        
        # if D_Key is starting this frame...
        if D_Key.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Key.frameNStart = frameN  # exact frame index
            D_Key.tStart = t  # local t and not account for scr refresh
            D_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Key.started')
            # update status
            D_Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(D_Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(D_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if D_Key is stopping this frame...
        if D_Key.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                D_Key.tStop = t  # not accounting for scr refresh
                D_Key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_Key.stopped')
                # update status
                D_Key.status = FINISHED
                D_Key.status = FINISHED
        if D_Key.status == STARTED and not waitOnFlip:
            theseKeys = D_Key.getKeys(keyList=['x','z','n'], waitRelease=False)
            _D_Key_allKeys.extend(theseKeys)
            if len(_D_Key_allKeys):
                D_Key.keys = _D_Key_allKeys[-1].name  # just the last key pressed
                D_Key.rt = _D_Key_allKeys[-1].rt
                # was this correct?
                if (D_Key.keys == str(flankercevap)) or (D_Key.keys == flankercevap):
                    D_Key.corr = 1
                else:
                    D_Key.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop D_Sound
        # Run 'Each Frame' code from D_code2000_flanker
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
        for thisComponent in D_Flanker2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "D_Flanker2000ms" ---
    for thisComponent in D_Flanker2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if D_Key.keys in ['', [], None]:  # No response was made
        D_Key.keys = None
        # was no response the correct answer?!
        if str(flankercevap).lower() == 'none':
           D_Key.corr = 1;  # correct non-response
        else:
           D_Key.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopDeney (TrialHandler)
    LoopDeney.addData('D_Key.keys',D_Key.keys)
    LoopDeney.addData('D_Key.corr', D_Key.corr)
    if D_Key.keys != None:  # we had a response
        LoopDeney.addData('D_Key.rt', D_Key.rt)
    D_Sound.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from D_code2000_flanker
    if D_Key.keys == None:
        D_Sound.play()
    # the Routine "D_Flanker2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "D_FlankerFixation500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    D_FlankerFixation500msComponents = [D_500]
    for thisComponent in D_FlankerFixation500msComponents:
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
    
    # --- Run Routine "D_FlankerFixation500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *D_500* updates
        
        # if D_500 is starting this frame...
        if D_500.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_500.frameNStart = frameN  # exact frame index
            D_500.tStart = t  # local t and not account for scr refresh
            D_500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_500.started')
            # update status
            D_500.status = STARTED
            D_500.setAutoDraw(True)
        
        # if D_500 is active this frame...
        if D_500.status == STARTED:
            # update params
            pass
        
        # if D_500 is stopping this frame...
        if D_500.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                D_500.tStop = t  # not accounting for scr refresh
                D_500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D_500.stopped')
                # update status
                D_500.status = FINISHED
                D_500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in D_FlankerFixation500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "D_FlankerFixation500ms" ---
    for thisComponent in D_FlankerFixation500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "D_FlankerFixation500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "D_VWMLoadTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    D_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
    D_image2_2.setColor([r2,g2,b2], colorSpace='rgb')
    D_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
    D_image4_2.setColor([r4,g4,b4], colorSpace='rgb')
    D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
    D_image6_2.setColor([r6,g6,b6], colorSpace='rgb')
    D_Key_2.keys = []
    D_Key_2.rt = []
    _D_Key_2_allKeys = []
    D_Sound_2.setSound('yanlis.wav', hamming=True)
    D_Sound_2.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from D_Code_VWM
    D_image1_2.size = (0, 0)
    D_image2_2.size = (0, 0)
    D_image3_2.size = (0, 0)
    D_image4_2.size = (0, 0)
    D_image5_2.size = (0, 0)
    D_image6_2.size = (0, 0)
    D_Poli1.size = (0, 0)
    D_Poli2.size = (0, 0)
    D_Poli3.size = (0, 0)
    D_Poli4.size = (0, 0)
    D_Poli5.size = (0, 0)
    D_Poli6.size = (0, 0)
    
    if D_kosul.text == "LL":
        if D_cevap.text == "ö":
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0.053, 0.093)
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0, 0)
                D_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0.053, 0.093)
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0, 0)
                D_Poli5.size = (0.053, 0.093)
        
        if D_cevap.text == "ç":
            r5 = float(round(r5,4)) + 0.5333
            g5 = float(round(g5,4)) + 0.5333
            b5 = float(round(b5,4)) + 0.5333
            
            r6 = float(round(r6,4)) + 0.5333
            g6 = float(round(g6,4)) + 0.5333
            b6 = float(round(b6,4)) + 0.5333
            
            if r5 > 1:
                r5 = r5 - 0.5333
                p1 = 1 - r5
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r5 = -float(round(p4,4))
                
            if g5 > 1:
                g5 = g5 - 0.5333
                p1 = 1 - g5
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g5 = -float(round(p4,4))
                
            if b5 > 1:
                b5 = b5 - 0.5333
                p1 = 1 - b5
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b5 = -float(round(p4,4))
                
            if r6 > 1:
                r6 = r6 - 0.5333
                p1 = 1 - r6
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r6 = -float(round(p4,4))
                
            if g6 > 1:
                g6 = g6 - 0.5333
                p1 = 1 - g6
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g6 = -float(round(p4,4))
                
            if b6 > 1:
                b6 = b6 - 0.5333
                p1 = 1 - b6
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b6 = -float(round(p4,4))
            
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0.053, 0.093)
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0, 0)
                D_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0.053, 0.093)
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0, 0)
                D_Poli5.size = (0.053, 0.093)
                
    
    elif D_kosul.text == "HL": 
        if D_cevap.text == "ö":
            dizi = [1,2,3,4]
            shuffle(dizi)
            if dizi[0] == 1:
                D_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                D_image1_2.size = (0.053, 0.093)
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0, 0)
                D_Poli2.size = (0.053, 0.093)
                D_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                D_image3_2.size = (0, 0)
                D_Poli3.size = (0.053, 0.093)
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0, 0)
                D_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 2:
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0.053, 0.093)
                D_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                D_image1_2.size = (0, 0)
                D_Poli1.size = (0.053, 0.093)
                D_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                D_image3_2.size = (0, 0)
                D_Poli3.size = (0.053, 0.093)
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0, 0)
                D_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 3:
                D_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                D_image3_2.size = (0.053, 0.093)
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0, 0)
                D_Poli4.size = (0.053, 0.093)
                D_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                D_image1_2.size = (0, 0)
                D_Poli1.size = (0.053, 0.093)
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0, 0)
                D_Poli2.size = (0.053, 0.093)
            elif dizi[0] == 4:
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0.053, 0.093)
                D_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                D_image3_2.size = (0, 0)
                D_Poli3.size = (0.053, 0.093)
                D_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                D_image1_2.size = (0, 0)
                D_Poli1.size = (0.053, 0.093)
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0, 0)
                D_Poli2.size = (0.053, 0.093)
        
        if D_cevap.text == "ç":
            r1 = float(round(r1,4)) + 0.5333
            g1 = float(round(g1,4)) + 0.5333
            b1 = float(round(b1,4)) + 0.5333
            
            r2 = float(round(r2,4)) + 0.5333
            g2 = float(round(g2,4)) + 0.5333
            b2 = float(round(b2,4)) + 0.5333
            
            r3 = float(round(r3,4)) + 0.5333
            g3 = float(round(g3,4)) + 0.5333
            b3 = float(round(b3,4)) + 0.5333
            
            r4 = float(round(r4,4)) + 0.5333
            g4 = float(round(g4,4)) + 0.5333
            b4 = float(round(b4,4)) + 0.5333
            
            if r1 > 1:
                r1 = r1 - 0.5333
                p1 = 1 - r1
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r1 = -float(round(p4,4))
                
            if g1 > 1:
                g1 = g1 - 0.5333
                p1 = 1 - g1
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g1 = -float(round(p4,4))
                
            if b1 > 1:
                b1 = b1 - 0.5333
                p1 = 1 - b1
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b1 = -float(round(p4,4))
                
            if r2 > 1:
                r2 = r2 - 0.5333
                p1 = 1 - r2
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r2 = -float(round(p4,4))
                
            if g2 > 1:
                g2 = g2 - 0.5333
                p1 = 1 - g2
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g2 = -float(round(p4,4))
                
            if b2 > 1:
                b2 = b2 - 0.5333
                p1 = 1 - b2
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b2 = -float(round(p4,4))
                
            if r3 > 1:
                r3 = r3 - 0.5333
                p1 = 1 - r3
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r3 = -float(round(p4,4))
                
            if g3 > 1:
                g3 = g3 - 0.5333
                p1 = 1 - g3
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g3 = -float(round(p4,4))
                
            if b3 > 1:
                b3 = b3 - 0.5333
                p1 = 1 - b3
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b3 = -float(round(p4,4))
                
            if r4 > 1:
                r4 = r4 - 0.5333
                p1 = 1 - r4
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r4 = -float(round(p4,4))
                
            if g4 > 1:
                g4 = g4 - 0.5333
                p1 = 1 - g4
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g4 = -float(round(p4,4))
                
            if b4 > 1:
                b4 = b4 - 0.5333
                p1 = 1 - b4
                p2 = 0.5333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b4 = -float(round(p4,4))
    
            dizi = [1,2,3,4]
            shuffle(dizi)
            if dizi[0] == 1:
                D_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                D_image1_2.size = (0.053, 0.093)
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0, 0)
                D_Poli2.size = (0.053, 0.093)
                D_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                D_image3_2.size = (0, 0)
                D_Poli3.size = (0.053, 0.093)
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0, 0)
                D_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 2:
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0.053, 0.093)
                D_image1_2.setColor([r1,g1,b1], colorSpace='rgb')
                D_image1_2.size = (0, 0)
                D_Poli1.size = (0.053, 0.093)
                D_image3_2.setColor([r3,g3,g3], colorSpace='rgb')
                D_image3_2.size = (0, 0)
                D_Poli3.size = (0.053, 0.093)
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0, 0)
                D_Poli4.size = (0.053, 0.093)
            elif dizi[0] == 3:
                D_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                D_image3_2.size = (0.053, 0.093)
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0, 0)
                D_Poli4.size = (0.053, 0.093)
                D_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                D_image1_2.size = (0, 0)
                D_Poli1.size = (0.053, 0.093)
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0, 0)
                D_Poli2.size = (0.053, 0.093)
            elif dizi[0] == 4:
                D_image4_2.setColor([r4,g4,g4], colorSpace='rgb')
                D_image4_2.size = (0.053, 0.093)
                D_image3_2.setColor([r3,g3,b3], colorSpace='rgb')
                D_image3_2.size = (0, 0)
                D_Poli3.size = (0.053, 0.093)
                D_image1_2.setColor([r1,g1,g1], colorSpace='rgb')
                D_image1_2.size = (0, 0)
                D_Poli1.size = (0.053, 0.093)
                D_image2_2.setColor([r2,g2,g2], colorSpace='rgb')
                D_image2_2.size = (0, 0)
                D_Poli2.size = (0.053, 0.093)
    
    elif D_kosul.text == "LS": 
        if D_cevap.text == "ö":
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0.053, 0.093)
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0, 0)
                D_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0.053, 0.093)
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0, 0)
                D_Poli5.size = (0.053, 0.093)
    
        if D_cevap.text == "ç":
            r5 = float(round(r5,4)) + 0.1333
            g5 = float(round(g5,4)) + 0.1333
            b5 = float(round(b5,4)) + 0.1333
            
            r6 = float(round(r6,4)) + 0.1333
            g6 = float(round(g6,4)) + 0.1333
            b6 = float(round(b6,4)) + 0.1333
            
            if r5 > 1:
                r5 = r5 - 0.1333
                p1 = 1 - r5
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r5 = -float(round(p4,4))
                
            if g5 > 1:
                g5 = g5 - 0.1333
                p1 = 1 - g5
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g5 = -float(round(p4,4))
                
            if b5 > 1:
                b5 = b5 - 0.1333
                p1 = 1 - b5
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b5 = -float(round(p4,4))
                
            if r6 > 1:
                r6 = r6 - 0.1333
                p1 = 1 - r6
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                r6 = -float(round(p4,4))
                
            if g6 > 1:
                g6 = g6 - 0.1333
                p1 = 1 - g6
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                g6 = -float(round(p4,4))
                
            if b6 > 1:
                b6 = b6 - 0.1333
                p1 = 1 - b6
                p2 = 0.1333 - float(round(p1,4))
                p3 = abs(float(round(p2,4)) - float(round(p1,4)))
                p4 = 1 - float(round(p3,4))
                b6 = -float(round(p4,4))
    
            dizi = [5,6]
            shuffle(dizi)
            if dizi[0] == 5:
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0.053, 0.093)
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0, 0)
                D_Poli6.size = (0.053, 0.093)
            elif dizi[0] == 6:
                D_image6_2.setColor([r6,g6,g6], colorSpace='rgb')
                D_image6_2.size = (0.053, 0.093)
                D_image5_2.setColor([r5,g5,b5], colorSpace='rgb')
                D_image5_2.size = (0, 0)
                D_Poli5.size = (0.053, 0.093)
    # keep track of which components have finished
    D_VWMLoadTaskComponents = [D_Background1_2, D_image1_2, D_image2_2, D_image3_2, D_image4_2, D_image5_2, D_image6_2, D_Poli1, D_Poli2, D_Poli3, D_Poli4, D_Poli5, D_Poli6, D_Key_2, D_Sound_2]
    for thisComponent in D_VWMLoadTaskComponents:
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
    
    # --- Run Routine "D_VWMLoadTask" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *D_Background1_2* updates
        
        # if D_Background1_2 is starting this frame...
        if D_Background1_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Background1_2.frameNStart = frameN  # exact frame index
            D_Background1_2.tStart = t  # local t and not account for scr refresh
            D_Background1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Background1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Background1_2.started')
            # update status
            D_Background1_2.status = STARTED
            D_Background1_2.setAutoDraw(True)
        
        # if D_Background1_2 is active this frame...
        if D_Background1_2.status == STARTED:
            # update params
            pass
        
        # *D_image1_2* updates
        
        # if D_image1_2 is starting this frame...
        if D_image1_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image1_2.frameNStart = frameN  # exact frame index
            D_image1_2.tStart = t  # local t and not account for scr refresh
            D_image1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image1_2.started')
            # update status
            D_image1_2.status = STARTED
            D_image1_2.setAutoDraw(True)
        
        # if D_image1_2 is active this frame...
        if D_image1_2.status == STARTED:
            # update params
            pass
        
        # *D_image2_2* updates
        
        # if D_image2_2 is starting this frame...
        if D_image2_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image2_2.frameNStart = frameN  # exact frame index
            D_image2_2.tStart = t  # local t and not account for scr refresh
            D_image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image2_2.started')
            # update status
            D_image2_2.status = STARTED
            D_image2_2.setAutoDraw(True)
        
        # if D_image2_2 is active this frame...
        if D_image2_2.status == STARTED:
            # update params
            pass
        
        # *D_image3_2* updates
        
        # if D_image3_2 is starting this frame...
        if D_image3_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image3_2.frameNStart = frameN  # exact frame index
            D_image3_2.tStart = t  # local t and not account for scr refresh
            D_image3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image3_2.started')
            # update status
            D_image3_2.status = STARTED
            D_image3_2.setAutoDraw(True)
        
        # if D_image3_2 is active this frame...
        if D_image3_2.status == STARTED:
            # update params
            pass
        
        # *D_image4_2* updates
        
        # if D_image4_2 is starting this frame...
        if D_image4_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image4_2.frameNStart = frameN  # exact frame index
            D_image4_2.tStart = t  # local t and not account for scr refresh
            D_image4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image4_2.started')
            # update status
            D_image4_2.status = STARTED
            D_image4_2.setAutoDraw(True)
        
        # if D_image4_2 is active this frame...
        if D_image4_2.status == STARTED:
            # update params
            pass
        
        # *D_image5_2* updates
        
        # if D_image5_2 is starting this frame...
        if D_image5_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image5_2.frameNStart = frameN  # exact frame index
            D_image5_2.tStart = t  # local t and not account for scr refresh
            D_image5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image5_2.started')
            # update status
            D_image5_2.status = STARTED
            D_image5_2.setAutoDraw(True)
        
        # if D_image5_2 is active this frame...
        if D_image5_2.status == STARTED:
            # update params
            pass
        
        # *D_image6_2* updates
        
        # if D_image6_2 is starting this frame...
        if D_image6_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_image6_2.frameNStart = frameN  # exact frame index
            D_image6_2.tStart = t  # local t and not account for scr refresh
            D_image6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_image6_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_image6_2.started')
            # update status
            D_image6_2.status = STARTED
            D_image6_2.setAutoDraw(True)
        
        # if D_image6_2 is active this frame...
        if D_image6_2.status == STARTED:
            # update params
            pass
        
        # *D_Poli1* updates
        
        # if D_Poli1 is starting this frame...
        if D_Poli1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Poli1.frameNStart = frameN  # exact frame index
            D_Poli1.tStart = t  # local t and not account for scr refresh
            D_Poli1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Poli1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Poli1.started')
            # update status
            D_Poli1.status = STARTED
            D_Poli1.setAutoDraw(True)
        
        # if D_Poli1 is active this frame...
        if D_Poli1.status == STARTED:
            # update params
            pass
        
        # *D_Poli2* updates
        
        # if D_Poli2 is starting this frame...
        if D_Poli2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Poli2.frameNStart = frameN  # exact frame index
            D_Poli2.tStart = t  # local t and not account for scr refresh
            D_Poli2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Poli2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Poli2.started')
            # update status
            D_Poli2.status = STARTED
            D_Poli2.setAutoDraw(True)
        
        # if D_Poli2 is active this frame...
        if D_Poli2.status == STARTED:
            # update params
            pass
        
        # *D_Poli3* updates
        
        # if D_Poli3 is starting this frame...
        if D_Poli3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Poli3.frameNStart = frameN  # exact frame index
            D_Poli3.tStart = t  # local t and not account for scr refresh
            D_Poli3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Poli3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Poli3.started')
            # update status
            D_Poli3.status = STARTED
            D_Poli3.setAutoDraw(True)
        
        # if D_Poli3 is active this frame...
        if D_Poli3.status == STARTED:
            # update params
            pass
        
        # *D_Poli4* updates
        
        # if D_Poli4 is starting this frame...
        if D_Poli4.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Poli4.frameNStart = frameN  # exact frame index
            D_Poli4.tStart = t  # local t and not account for scr refresh
            D_Poli4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Poli4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Poli4.started')
            # update status
            D_Poli4.status = STARTED
            D_Poli4.setAutoDraw(True)
        
        # if D_Poli4 is active this frame...
        if D_Poli4.status == STARTED:
            # update params
            pass
        
        # *D_Poli5* updates
        
        # if D_Poli5 is starting this frame...
        if D_Poli5.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Poli5.frameNStart = frameN  # exact frame index
            D_Poli5.tStart = t  # local t and not account for scr refresh
            D_Poli5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Poli5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Poli5.started')
            # update status
            D_Poli5.status = STARTED
            D_Poli5.setAutoDraw(True)
        
        # if D_Poli5 is active this frame...
        if D_Poli5.status == STARTED:
            # update params
            pass
        
        # *D_Poli6* updates
        
        # if D_Poli6 is starting this frame...
        if D_Poli6.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Poli6.frameNStart = frameN  # exact frame index
            D_Poli6.tStart = t  # local t and not account for scr refresh
            D_Poli6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Poli6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Poli6.started')
            # update status
            D_Poli6.status = STARTED
            D_Poli6.setAutoDraw(True)
        
        # if D_Poli6 is active this frame...
        if D_Poli6.status == STARTED:
            # update params
            pass
        
        # *D_Key_2* updates
        waitOnFlip = False
        
        # if D_Key_2 is starting this frame...
        if D_Key_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            D_Key_2.frameNStart = frameN  # exact frame index
            D_Key_2.tStart = t  # local t and not account for scr refresh
            D_Key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D_Key_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'D_Key_2.started')
            # update status
            D_Key_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(D_Key_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(D_Key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if D_Key_2.status == STARTED and not waitOnFlip:
            theseKeys = D_Key_2.getKeys(keyList=['ö','ç'], waitRelease=False)
            _D_Key_2_allKeys.extend(theseKeys)
            if len(_D_Key_2_allKeys):
                D_Key_2.keys = _D_Key_2_allKeys[-1].name  # just the last key pressed
                D_Key_2.rt = _D_Key_2_allKeys[-1].rt
                # was this correct?
                if (D_Key_2.keys == str(taskcevap)) or (D_Key_2.keys == taskcevap):
                    D_Key_2.corr = 1
                else:
                    D_Key_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop D_Sound_2
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in D_VWMLoadTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "D_VWMLoadTask" ---
    for thisComponent in D_VWMLoadTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if D_Key_2.keys in ['', [], None]:  # No response was made
        D_Key_2.keys = None
        # was no response the correct answer?!
        if str(taskcevap).lower() == 'none':
           D_Key_2.corr = 1;  # correct non-response
        else:
           D_Key_2.corr = 0;  # failed to respond (incorrectly)
    # store data for LoopDeney (TrialHandler)
    LoopDeney.addData('D_Key_2.keys',D_Key_2.keys)
    LoopDeney.addData('D_Key_2.corr', D_Key_2.corr)
    if D_Key_2.keys != None:  # we had a response
        LoopDeney.addData('D_Key_2.rt', D_Key_2.rt)
    D_Sound_2.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from D_Code_VWM
    if D_Key_2.corr == 0:
        D_Sound_2.play()
    # the Routine "D_VWMLoadTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LoopDeney'

# get names of stimulus parameters
if LoopDeney.trialList in ([], [None], None):
    params = []
else:
    params = LoopDeney.trialList[0].keys()
# save data for this loop
LoopDeney.saveAsExcel(filename + '.xlsx', sheetName='LoopDeney',
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
