#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on July 21, 2023, at 13:50
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
prefs.hardware['audioLib'] = 'pygame'
prefs.hardware['audioLatencyMode'] = '4'
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
expName = 'replication_of_lee_and_jeong_exp1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\wasd0\\Desktop\\Psychopy\\Lee, H and Jeong, S. K. (2020)\\replication_of_lee_and_jeong_exp1_lastrun.py',
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
Yonergee = keyboard.Keyboard()
TextYonerge = visual.TextStim(win=win, name='TextYonerge',
    text='Çalışmamıza hoş geldiniz.\n\nBirazdan ekranınıza bir kutucuk içinde bazı renkler sunulacaktır. Sizden, ekranınıza gelen renkleri konumlarıyla beraber aklınızda tutmanız ve flanker görevini yapmanız beklenmektedir. \n\nRenk ve konum bilgilerini aklınızda tutmaya çalışırken flanker görevi kapsamında ekranınıza farklı pozisyonlarda iki adet harf (H ve S) sunulacaktır. Bu görev kapsamında sizden merkeze daha yakın olan harfin hangisi olduğuna dikkat etmeniz, elinizden geldiğince hızlı bir biçimde klavyeden ilgili tuşa basmanız ve diğer harfi reddetmeniz beklenmektedir.\n\nFlanker görevinin ardından ekranınıza bir kez daha bir kutucuk içinde bazı renkler sunulacaktır. Mevcut ekran eğer ilk gördüğünüz ekran ile renk ve konum açısından birbirleriyle tam olarak eşleşiyorsa "z", eşleşmiyorsa "x" tuşuna elinizden geldiğince hızlı bir biçimde basmanız beklenmektedir.\n\nİlk 16 deneme alıştırma niteliğinde olup, 16. denemenin ardından ana deneye geçilecektir.\n\nAlıştırma aşamasına geçmek için herhangi bir tuşa tıklayınız.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Alistirma_Fixation800ms" ---
image800Alistirma = visual.ImageStim(
    win=win,
    name='image800Alistirma', units='norm', 
    image='small circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
kosulAlistirma = visual.TextStim(win=win, name='kosulAlistirma',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
cevapAlistirma = visual.TextStim(win=win, name='cevapAlistirma',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from Code800Alistirma
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

# --- Initialize components for Routine "Alistirma_Load200ms" ---
image1Alistirma = visual.ImageStim(
    win=win,
    name='image1Alistirma', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
image2Alistirma = visual.ImageStim(
    win=win,
    name='image2Alistirma', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3Alistirma = visual.ImageStim(
    win=win,
    name='image3Alistirma', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4Alistirma = visual.ImageStim(
    win=win,
    name='image4Alistirma', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5Alistirma = visual.ImageStim(
    win=win,
    name='image5Alistirma', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
# Run 'Begin Experiment' code from CodeLoadAlistirma
degisken = 0

# --- Initialize components for Routine "Alistirma_BlankScreen2000ms" ---
BlankAlistirma = visual.ImageStim(
    win=win,
    name='BlankAlistirma', units='norm', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[0,0,0], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Alistirma_FlankerTask2000ms" ---
HedefAlistirma = visual.TextStim(win=win, name='HedefAlistirma',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
CeldiriciAlistirma = visual.TextStim(win=win, name='CeldiriciAlistirma',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.095, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyAlistirma = keyboard.Keyboard()
SoundAlistirma = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SoundAlistirma')
SoundAlistirma.setVolume(1.0)

# --- Initialize components for Routine "Alistirma_Fixation500ms" ---
FlankerAlistirmaFix = visual.ImageStim(
    win=win,
    name='FlankerAlistirmaFix', units='norm', 
    image='small circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Alistirma_ChangeDetection" ---
image1Alistirma_2 = visual.ImageStim(
    win=win,
    name='image1Alistirma_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
image2Alistirma_2 = visual.ImageStim(
    win=win,
    name='image2Alistirma_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3Alistirma_2 = visual.ImageStim(
    win=win,
    name='image3Alistirma_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4Alistirma_2 = visual.ImageStim(
    win=win,
    name='image4Alistirma_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5Alistirma_2 = visual.ImageStim(
    win=win,
    name='image5Alistirma_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Poli1Alistirma = visual.Rect(
    win=win, name='Poli1Alistirma',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.09,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-5.0, interpolate=True)
Poli2Alistirma = visual.Rect(
    win=win, name='Poli2Alistirma',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.09,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-6.0, interpolate=True)
Poli3Alistirma = visual.Rect(
    win=win, name='Poli3Alistirma',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.09,-0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-7.0, interpolate=True)
Poli4Alistirma = visual.Rect(
    win=win, name='Poli4Alistirma',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.09,-0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-8.0, interpolate=True)
Poli5Alistirma = visual.Rect(
    win=win, name='Poli5Alistirma',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-9.0, interpolate=True)
KeyAlistirma_2 = keyboard.Keyboard()
SoundAlistirma_2 = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SoundAlistirma_2')
SoundAlistirma_2.setVolume(1.0)

# --- Initialize components for Routine "ConditionLNStart" ---
KeyboardStart = keyboard.Keyboard()
TextStart = visual.TextStim(win=win, name='TextStart',
    text='Deney aşamasına geçmek için hazır olduğunuzda herhangi bir tuşa tıklayınız.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Deney_Fixation800ms" ---
image800Deney = visual.ImageStim(
    win=win,
    name='image800Deney', units='norm', 
    image='small circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
kosulDeney = visual.TextStim(win=win, name='kosulDeney',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
cevapDeney = visual.TextStim(win=win, name='cevapDeney',
    text='',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from Code800Deney
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

# --- Initialize components for Routine "Deney_Load200ms" ---
image1Deney = visual.ImageStim(
    win=win,
    name='image1Deney', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
image2Deney = visual.ImageStim(
    win=win,
    name='image2Deney', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3Deney = visual.ImageStim(
    win=win,
    name='image3Deney', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4Deney = visual.ImageStim(
    win=win,
    name='image4Deney', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5Deney = visual.ImageStim(
    win=win,
    name='image5Deney', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
# Run 'Begin Experiment' code from CodeLoadDeney
degisken = 0

# --- Initialize components for Routine "Deney_BlankScreen2000ms" ---
BlankDeney = visual.ImageStim(
    win=win,
    name='BlankDeney', units='norm', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[0,0,0], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Deney_FlankerTask2000ms" ---
HedefDeney = visual.TextStim(win=win, name='HedefDeney',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
CeldiriciDeney = visual.TextStim(win=win, name='CeldiriciDeney',
    text='',
    font='Times New Roman',
    units='norm', pos=[0,0], height=0.095, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
KeyDeney = keyboard.Keyboard()
SoundDeney = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SoundDeney')
SoundDeney.setVolume(1.0)

# --- Initialize components for Routine "Deney_Fixation500ms" ---
FlankerDeneyFix = visual.ImageStim(
    win=win,
    name='FlankerDeneyFix', units='norm', 
    image='small circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Deney_ChangeDetection" ---
image1Deney_2 = visual.ImageStim(
    win=win,
    name='image1Deney_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
image2Deney_2 = visual.ImageStim(
    win=win,
    name='image2Deney_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3Deney_2 = visual.ImageStim(
    win=win,
    name='image3Deney_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4Deney_2 = visual.ImageStim(
    win=win,
    name='image4Deney_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0.09,-0.15), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5Deney_2 = visual.ImageStim(
    win=win,
    name='image5Deney_2', units='norm', 
    image='white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0, 0),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Poli1Deney = visual.Rect(
    win=win, name='Poli1Deney',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.09,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-5.0, interpolate=True)
Poli2Deney = visual.Rect(
    win=win, name='Poli2Deney',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.09,0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-6.0, interpolate=True)
Poli3Deney = visual.Rect(
    win=win, name='Poli3Deney',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(-0.09,-0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-7.0, interpolate=True)
Poli4Deney = visual.Rect(
    win=win, name='Poli4Deney',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0.09,-0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-8.0, interpolate=True)
Poli5Deney = visual.Rect(
    win=win, name='Poli5Deney',units='norm', 
    width=(0, 0)[0], height=(0, 0)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[0,0,0],
    opacity=None, depth=-9.0, interpolate=True)
KeyDeney_2 = keyboard.Keyboard()
SoundDeney_2 = sound.Sound('yanlis.wav', secs=-1, stereo=True, hamming=True,
    name='SoundDeney_2')
SoundDeney_2.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Yonerge" ---
continueRoutine = True
# update component parameters for each repeat
Yonergee.keys = []
Yonergee.rt = []
_Yonergee_allKeys = []
# keep track of which components have finished
YonergeComponents = [Yonergee, TextYonerge]
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
    
    # *Yonergee* updates
    waitOnFlip = False
    
    # if Yonergee is starting this frame...
    if Yonergee.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Yonergee.frameNStart = frameN  # exact frame index
        Yonergee.tStart = t  # local t and not account for scr refresh
        Yonergee.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Yonergee, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Yonergee.started')
        # update status
        Yonergee.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Yonergee.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Yonergee.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Yonergee.status == STARTED and not waitOnFlip:
        theseKeys = Yonergee.getKeys(keyList=None, waitRelease=False)
        _Yonergee_allKeys.extend(theseKeys)
        if len(_Yonergee_allKeys):
            Yonergee.keys = _Yonergee_allKeys[-1].name  # just the last key pressed
            Yonergee.rt = _Yonergee_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *TextYonerge* updates
    
    # if TextYonerge is starting this frame...
    if TextYonerge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextYonerge.frameNStart = frameN  # exact frame index
        TextYonerge.tStart = t  # local t and not account for scr refresh
        TextYonerge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextYonerge, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextYonerge.started')
        # update status
        TextYonerge.status = STARTED
        TextYonerge.setAutoDraw(True)
    
    # if TextYonerge is active this frame...
    if TextYonerge.status == STARTED:
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
if Yonergee.keys in ['', [], None]:  # No response was made
    Yonergee.keys = None
thisExp.addData('Yonergee.keys',Yonergee.keys)
if Yonergee.keys != None:  # we had a response
    thisExp.addData('Yonergee.rt', Yonergee.rt)
thisExp.nextEntry()
# the Routine "Yonerge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ConditionAlistirma = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('replication_of_lee_and_jeong_exp1.xlsx'),
    seed=None, name='ConditionAlistirma')
thisExp.addLoop(ConditionAlistirma)  # add the loop to the experiment
thisConditionAlistirma = ConditionAlistirma.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConditionAlistirma.rgb)
if thisConditionAlistirma != None:
    for paramName in thisConditionAlistirma:
        exec('{} = thisConditionAlistirma[paramName]'.format(paramName))

for thisConditionAlistirma in ConditionAlistirma:
    currentLoop = ConditionAlistirma
    # abbreviate parameter names if possible (e.g. rgb = thisConditionAlistirma.rgb)
    if thisConditionAlistirma != None:
        for paramName in thisConditionAlistirma:
            exec('{} = thisConditionAlistirma[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Alistirma_Fixation800ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    kosulAlistirma.setText(condition)
    cevapAlistirma.setText(taskcevap)
    # keep track of which components have finished
    Alistirma_Fixation800msComponents = [image800Alistirma, kosulAlistirma, cevapAlistirma]
    for thisComponent in Alistirma_Fixation800msComponents:
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
    
    # --- Run Routine "Alistirma_Fixation800ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image800Alistirma* updates
        
        # if image800Alistirma is starting this frame...
        if image800Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image800Alistirma.frameNStart = frameN  # exact frame index
            image800Alistirma.tStart = t  # local t and not account for scr refresh
            image800Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image800Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image800Alistirma.started')
            # update status
            image800Alistirma.status = STARTED
            image800Alistirma.setAutoDraw(True)
        
        # if image800Alistirma is active this frame...
        if image800Alistirma.status == STARTED:
            # update params
            pass
        
        # if image800Alistirma is stopping this frame...
        if image800Alistirma.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                image800Alistirma.tStop = t  # not accounting for scr refresh
                image800Alistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image800Alistirma.stopped')
                # update status
                image800Alistirma.status = FINISHED
                image800Alistirma.setAutoDraw(False)
        
        # *kosulAlistirma* updates
        
        # if kosulAlistirma is starting this frame...
        if kosulAlistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            kosulAlistirma.frameNStart = frameN  # exact frame index
            kosulAlistirma.tStart = t  # local t and not account for scr refresh
            kosulAlistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kosulAlistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'kosulAlistirma.started')
            # update status
            kosulAlistirma.status = STARTED
            kosulAlistirma.setAutoDraw(True)
        
        # if kosulAlistirma is active this frame...
        if kosulAlistirma.status == STARTED:
            # update params
            pass
        
        # if kosulAlistirma is stopping this frame...
        if kosulAlistirma.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                kosulAlistirma.tStop = t  # not accounting for scr refresh
                kosulAlistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kosulAlistirma.stopped')
                # update status
                kosulAlistirma.status = FINISHED
                kosulAlistirma.setAutoDraw(False)
        
        # *cevapAlistirma* updates
        
        # if cevapAlistirma is starting this frame...
        if cevapAlistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            cevapAlistirma.frameNStart = frameN  # exact frame index
            cevapAlistirma.tStart = t  # local t and not account for scr refresh
            cevapAlistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cevapAlistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cevapAlistirma.started')
            # update status
            cevapAlistirma.status = STARTED
            cevapAlistirma.setAutoDraw(True)
        
        # if cevapAlistirma is active this frame...
        if cevapAlistirma.status == STARTED:
            # update params
            pass
        
        # if cevapAlistirma is stopping this frame...
        if cevapAlistirma.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                cevapAlistirma.tStop = t  # not accounting for scr refresh
                cevapAlistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cevapAlistirma.stopped')
                # update status
                cevapAlistirma.status = FINISHED
                cevapAlistirma.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Alistirma_Fixation800msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Alistirma_Fixation800ms" ---
    for thisComponent in Alistirma_Fixation800msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Code800Alistirma
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
    # the Routine "Alistirma_Fixation800ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Alistirma_Load200ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    image1Alistirma.setColor([r1,g1,b1], colorSpace='rgb')
    image2Alistirma.setColor([r2,g2,b2], colorSpace='rgb')
    image3Alistirma.setColor([r3,g3,b3], colorSpace='rgb')
    image4Alistirma.setColor([r4,g4,b4], colorSpace='rgb')
    image5Alistirma.setColor([r5,g5,b5], colorSpace='rgb')
    # Run 'Begin Routine' code from CodeLoadAlistirma
    if kosulAlistirma.text == "LN":
        image5Alistirma.size = (0.06, 0.1)
    elif kosulAlistirma.text == "HW":
        image1Alistirma.size = (0.06, 0.1)
        image2Alistirma.size = (0.06, 0.1)
        image3Alistirma.size = (0.06, 0.1)
        image4Alistirma.size = (0.06, 0.1)
    elif kosulAlistirma.text == "LW":
        dizi = [1,2,3,4]
        shuffle(dizi)
        
        if dizi[0] == 1:
            image2Alistirma.color = "white"
            image3Alistirma.color = "white"
            image4Alistirma.color = "white"
            degisken = 1
        elif dizi[0] == 2:
            image1Alistirma.color = "white"
            image3Alistirma.color = "white"
            image4Alistirma.color = "white"
            degisken = 2
        elif dizi[0] == 3:
            image1Alistirma.color = "white"
            image2Alistirma.color = "white"
            image4Alistirmacolor = "white"
            degisken = 3
        elif dizi[0] == 4:
            image1Alistirma.color = "white"
            image2Alistirma.color = "white"
            image3Alistirma.color = "white"
            degisken = 4
            
        image1Alistirma.size = (0.06, 0.1)
        image2Alistirma.size = (0.06, 0.1)
        image3Alistirma.size = (0.06, 0.1)
        image4Alistirma.size = (0.06, 0.1)
    # keep track of which components have finished
    Alistirma_Load200msComponents = [image1Alistirma, image2Alistirma, image3Alistirma, image4Alistirma, image5Alistirma]
    for thisComponent in Alistirma_Load200msComponents:
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
    
    # --- Run Routine "Alistirma_Load200ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1Alistirma* updates
        
        # if image1Alistirma is starting this frame...
        if image1Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image1Alistirma.frameNStart = frameN  # exact frame index
            image1Alistirma.tStart = t  # local t and not account for scr refresh
            image1Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image1Alistirma.started')
            # update status
            image1Alistirma.status = STARTED
            image1Alistirma.setAutoDraw(True)
        
        # if image1Alistirma is active this frame...
        if image1Alistirma.status == STARTED:
            # update params
            pass
        
        # if image1Alistirma is stopping this frame...
        if image1Alistirma.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image1Alistirma.tStop = t  # not accounting for scr refresh
                image1Alistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1Alistirma.stopped')
                # update status
                image1Alistirma.status = FINISHED
                image1Alistirma.setAutoDraw(False)
        
        # *image2Alistirma* updates
        
        # if image2Alistirma is starting this frame...
        if image2Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image2Alistirma.frameNStart = frameN  # exact frame index
            image2Alistirma.tStart = t  # local t and not account for scr refresh
            image2Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2Alistirma.started')
            # update status
            image2Alistirma.status = STARTED
            image2Alistirma.setAutoDraw(True)
        
        # if image2Alistirma is active this frame...
        if image2Alistirma.status == STARTED:
            # update params
            pass
        
        # if image2Alistirma is stopping this frame...
        if image2Alistirma.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image2Alistirma.tStop = t  # not accounting for scr refresh
                image2Alistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image2Alistirma.stopped')
                # update status
                image2Alistirma.status = FINISHED
                image2Alistirma.setAutoDraw(False)
        
        # *image3Alistirma* updates
        
        # if image3Alistirma is starting this frame...
        if image3Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image3Alistirma.frameNStart = frameN  # exact frame index
            image3Alistirma.tStart = t  # local t and not account for scr refresh
            image3Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image3Alistirma.started')
            # update status
            image3Alistirma.status = STARTED
            image3Alistirma.setAutoDraw(True)
        
        # if image3Alistirma is active this frame...
        if image3Alistirma.status == STARTED:
            # update params
            pass
        
        # if image3Alistirma is stopping this frame...
        if image3Alistirma.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image3Alistirma.tStop = t  # not accounting for scr refresh
                image3Alistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image3Alistirma.stopped')
                # update status
                image3Alistirma.status = FINISHED
                image3Alistirma.setAutoDraw(False)
        
        # *image4Alistirma* updates
        
        # if image4Alistirma is starting this frame...
        if image4Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image4Alistirma.frameNStart = frameN  # exact frame index
            image4Alistirma.tStart = t  # local t and not account for scr refresh
            image4Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image4Alistirma.started')
            # update status
            image4Alistirma.status = STARTED
            image4Alistirma.setAutoDraw(True)
        
        # if image4Alistirma is active this frame...
        if image4Alistirma.status == STARTED:
            # update params
            pass
        
        # if image4Alistirma is stopping this frame...
        if image4Alistirma.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image4Alistirma.tStop = t  # not accounting for scr refresh
                image4Alistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image4Alistirma.stopped')
                # update status
                image4Alistirma.status = FINISHED
                image4Alistirma.setAutoDraw(False)
        
        # *image5Alistirma* updates
        
        # if image5Alistirma is starting this frame...
        if image5Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image5Alistirma.frameNStart = frameN  # exact frame index
            image5Alistirma.tStart = t  # local t and not account for scr refresh
            image5Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image5Alistirma.started')
            # update status
            image5Alistirma.status = STARTED
            image5Alistirma.setAutoDraw(True)
        
        # if image5Alistirma is active this frame...
        if image5Alistirma.status == STARTED:
            # update params
            pass
        
        # if image5Alistirma is stopping this frame...
        if image5Alistirma.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image5Alistirma.tStop = t  # not accounting for scr refresh
                image5Alistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image5Alistirma.stopped')
                # update status
                image5Alistirma.status = FINISHED
                image5Alistirma.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Alistirma_Load200msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Alistirma_Load200ms" ---
    for thisComponent in Alistirma_Load200msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Alistirma_Load200ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Alistirma_BlankScreen2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Alistirma_BlankScreen2000msComponents = [BlankAlistirma]
    for thisComponent in Alistirma_BlankScreen2000msComponents:
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
    
    # --- Run Routine "Alistirma_BlankScreen2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankAlistirma* updates
        
        # if BlankAlistirma is starting this frame...
        if BlankAlistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            BlankAlistirma.frameNStart = frameN  # exact frame index
            BlankAlistirma.tStart = t  # local t and not account for scr refresh
            BlankAlistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankAlistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BlankAlistirma.started')
            # update status
            BlankAlistirma.status = STARTED
            BlankAlistirma.setAutoDraw(True)
        
        # if BlankAlistirma is active this frame...
        if BlankAlistirma.status == STARTED:
            # update params
            pass
        
        # if BlankAlistirma is stopping this frame...
        if BlankAlistirma.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                BlankAlistirma.tStop = t  # not accounting for scr refresh
                BlankAlistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BlankAlistirma.stopped')
                # update status
                BlankAlistirma.status = FINISHED
                BlankAlistirma.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Alistirma_BlankScreen2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Alistirma_BlankScreen2000ms" ---
    for thisComponent in Alistirma_BlankScreen2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Alistirma_BlankScreen2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Alistirma_FlankerTask2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    HedefAlistirma.setPos(pozisyonhedef)
    HedefAlistirma.setText(hedef)
    CeldiriciAlistirma.setPos(pozisyonceldirici)
    CeldiriciAlistirma.setText(celdirici)
    KeyAlistirma.keys = []
    KeyAlistirma.rt = []
    _KeyAlistirma_allKeys = []
    SoundAlistirma.setSound('yanlis.wav', hamming=True)
    SoundAlistirma.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CodeFlankerAlistirma
    FRate = 1000 / int(round(win.getActualFrameRate(),2))
    FrameN = int(2000 / FRate)
    frame = 0
    # keep track of which components have finished
    Alistirma_FlankerTask2000msComponents = [HedefAlistirma, CeldiriciAlistirma, KeyAlistirma, SoundAlistirma]
    for thisComponent in Alistirma_FlankerTask2000msComponents:
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
    
    # --- Run Routine "Alistirma_FlankerTask2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HedefAlistirma* updates
        
        # if HedefAlistirma is starting this frame...
        if HedefAlistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            HedefAlistirma.frameNStart = frameN  # exact frame index
            HedefAlistirma.tStart = t  # local t and not account for scr refresh
            HedefAlistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HedefAlistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HedefAlistirma.started')
            # update status
            HedefAlistirma.status = STARTED
            HedefAlistirma.setAutoDraw(True)
        
        # if HedefAlistirma is active this frame...
        if HedefAlistirma.status == STARTED:
            # update params
            pass
        
        # if HedefAlistirma is stopping this frame...
        if HedefAlistirma.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                HedefAlistirma.tStop = t  # not accounting for scr refresh
                HedefAlistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HedefAlistirma.stopped')
                # update status
                HedefAlistirma.status = FINISHED
                HedefAlistirma.setAutoDraw(False)
        
        # *CeldiriciAlistirma* updates
        
        # if CeldiriciAlistirma is starting this frame...
        if CeldiriciAlistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            CeldiriciAlistirma.frameNStart = frameN  # exact frame index
            CeldiriciAlistirma.tStart = t  # local t and not account for scr refresh
            CeldiriciAlistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CeldiriciAlistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CeldiriciAlistirma.started')
            # update status
            CeldiriciAlistirma.status = STARTED
            CeldiriciAlistirma.setAutoDraw(True)
        
        # if CeldiriciAlistirma is active this frame...
        if CeldiriciAlistirma.status == STARTED:
            # update params
            pass
        
        # if CeldiriciAlistirma is stopping this frame...
        if CeldiriciAlistirma.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                CeldiriciAlistirma.tStop = t  # not accounting for scr refresh
                CeldiriciAlistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CeldiriciAlistirma.stopped')
                # update status
                CeldiriciAlistirma.status = FINISHED
                CeldiriciAlistirma.setAutoDraw(False)
        
        # *KeyAlistirma* updates
        waitOnFlip = False
        
        # if KeyAlistirma is starting this frame...
        if KeyAlistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KeyAlistirma.frameNStart = frameN  # exact frame index
            KeyAlistirma.tStart = t  # local t and not account for scr refresh
            KeyAlistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyAlistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KeyAlistirma.started')
            # update status
            KeyAlistirma.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyAlistirma.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyAlistirma.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if KeyAlistirma is stopping this frame...
        if KeyAlistirma.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                KeyAlistirma.tStop = t  # not accounting for scr refresh
                KeyAlistirma.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeyAlistirma.stopped')
                # update status
                KeyAlistirma.status = FINISHED
                KeyAlistirma.status = FINISHED
        if KeyAlistirma.status == STARTED and not waitOnFlip:
            theseKeys = KeyAlistirma.getKeys(keyList=['h','s'], waitRelease=False)
            _KeyAlistirma_allKeys.extend(theseKeys)
            if len(_KeyAlistirma_allKeys):
                KeyAlistirma.keys = _KeyAlistirma_allKeys[0].name  # just the first key pressed
                KeyAlistirma.rt = _KeyAlistirma_allKeys[0].rt
                # was this correct?
                if (KeyAlistirma.keys == str(flankercevap)) or (KeyAlistirma.keys == flankercevap):
                    KeyAlistirma.corr = 1
                else:
                    KeyAlistirma.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SoundAlistirma
        # Run 'Each Frame' code from CodeFlankerAlistirma
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
        for thisComponent in Alistirma_FlankerTask2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Alistirma_FlankerTask2000ms" ---
    for thisComponent in Alistirma_FlankerTask2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyAlistirma.keys in ['', [], None]:  # No response was made
        KeyAlistirma.keys = None
        # was no response the correct answer?!
        if str(flankercevap).lower() == 'none':
           KeyAlistirma.corr = 1;  # correct non-response
        else:
           KeyAlistirma.corr = 0;  # failed to respond (incorrectly)
    # store data for ConditionAlistirma (TrialHandler)
    ConditionAlistirma.addData('KeyAlistirma.keys',KeyAlistirma.keys)
    ConditionAlistirma.addData('KeyAlistirma.corr', KeyAlistirma.corr)
    if KeyAlistirma.keys != None:  # we had a response
        ConditionAlistirma.addData('KeyAlistirma.rt', KeyAlistirma.rt)
    SoundAlistirma.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CodeFlankerAlistirma
    if KeyAlistirma.keys == None:
        SoundAlistirma.play()
    # the Routine "Alistirma_FlankerTask2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Alistirma_Fixation500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Alistirma_Fixation500msComponents = [FlankerAlistirmaFix]
    for thisComponent in Alistirma_Fixation500msComponents:
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
    
    # --- Run Routine "Alistirma_Fixation500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FlankerAlistirmaFix* updates
        
        # if FlankerAlistirmaFix is starting this frame...
        if FlankerAlistirmaFix.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            FlankerAlistirmaFix.frameNStart = frameN  # exact frame index
            FlankerAlistirmaFix.tStart = t  # local t and not account for scr refresh
            FlankerAlistirmaFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FlankerAlistirmaFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FlankerAlistirmaFix.started')
            # update status
            FlankerAlistirmaFix.status = STARTED
            FlankerAlistirmaFix.setAutoDraw(True)
        
        # if FlankerAlistirmaFix is active this frame...
        if FlankerAlistirmaFix.status == STARTED:
            # update params
            pass
        
        # if FlankerAlistirmaFix is stopping this frame...
        if FlankerAlistirmaFix.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                FlankerAlistirmaFix.tStop = t  # not accounting for scr refresh
                FlankerAlistirmaFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FlankerAlistirmaFix.stopped')
                # update status
                FlankerAlistirmaFix.status = FINISHED
                FlankerAlistirmaFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Alistirma_Fixation500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Alistirma_Fixation500ms" ---
    for thisComponent in Alistirma_Fixation500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Alistirma_Fixation500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Alistirma_ChangeDetection" ---
    continueRoutine = True
    # update component parameters for each repeat
    image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
    image2Alistirma_2.setColor([r2,g2,b2], colorSpace='rgb')
    image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
    image4Alistirma_2.setColor([r4,g4,b4], colorSpace='rgb')
    image5Alistirma_2.setColor([r5,g5,b5], colorSpace='rgb')
    KeyAlistirma_2.keys = []
    KeyAlistirma_2.rt = []
    _KeyAlistirma_2_allKeys = []
    SoundAlistirma_2.setSound('yanlis.wav', hamming=True)
    SoundAlistirma_2.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CodeTaskAlistirma
    image1Alistirma_2.size = (0, 0)
    image2Alistirma_2.size = (0, 0)
    image3Alistirma_2.size = (0, 0)
    image4Alistirma_2.size = (0, 0)
    image5Alistirma_2.size = (0, 0)
    Poli1Alistirma.size = (0, 0)
    Poli2Alistirma.size = (0, 0)
    Poli3Alistirma.size = (0, 0)
    Poli4Alistirma.size = (0, 0)
    Poli5Alistirma.size = (0, 0)
    
    if kosulAlistirma.text == "LN":
        if cevapAlistirma.text == "z":
            image5Alistirma_2.setColor([r5,g5,b5], colorSpace='rgb')
            image5Alistirma_2.size = (0.06, 0.1)
    
        if cevapAlistirma.text == "x":
            r5 = float(round(r5,4)) + 0.5333
            g5 = float(round(g5,4)) + 0.5333
            b5 = float(round(b5,4)) + 0.5333
           
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
                
            image5Alistirma_2.setColor([r5,g5,b5], colorSpace='rgb')
            image5Alistirma_2.size = (0.06, 0.1)
    
    elif kosulAlistirma.text == "HW": 
        if cevapAlistirma.text == "z":
            dizi = [1,2,3,4]
            shuffle(dizi)
            if dizi[0] == 1:
                image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Alistirma_2.size = (0.06, 0.1)
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0, 0)
                Poli2Alistirma.size = (0.06, 0.1)
                image3Alistirma_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Alistirma_2.size = (0, 0)
                Poli3Alistirma.size = (0.06, 0.1)
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0, 0)
                Poli4Alistirma.size = (0.06, 0.1)
            elif dizi[0] == 2:
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0.06, 0.1)
                image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Alistirma_2.size = (0, 0)
                Poli1Alistirma.size = (0.06, 0.1)
                image3Alistirma_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Alistirma_2.size = (0, 0)
                Poli3Alistirma.size = (0.06, 0.1)
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0, 0)
                Poli4Alistirma.size = (0.06, 0.1)
            elif dizi[0] == 3:
                image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Alistirma_2.size = (0.06, 0.1)
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0, 0)
                Poli4Alistirma.size = (0.06, 0.1)
                image1Alistirma_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Alistirma_2.size = (0, 0)
                Poli1Alistirma.size = (0.06, 0.1)
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0, 0)
                Poli2Alistirma.size = (0.06, 0.1)
            elif dizi[0] == 4:
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0.06, 0.1)
                image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Alistirma_2.size = (0, 0)
                Poli3Alistirma.size = (0.06, 0.1)
                image1Alistirma_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Alistirma_2.size = (0, 0)
                Poli1Alistirma.size = (0.06, 0.1)
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0, 0)
                Poli2Alistirma.size = (0.06, 0.1)
        
        if cevapAlistirma.text == "x":
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
                image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Alistirma_2.size = (0.06, 0.1)
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0, 0)
                Poli2Alistirma.size = (0.06, 0.1)
                image3Alistirma_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Alistirma_2.size = (0, 0)
                Poli3Alistirma.size = (0.06, 0.1)
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0, 0)
                Poli4Alistirma.size = (0.06, 0.1)
            elif dizi[0] == 2:
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0.06, 0.1)
                image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Alistirma_2.size = (0, 0)
                Poli1Alistirma.size = (0.06, 0.1)
                image3Alistirma_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Alistirma_2.size = (0, 0)
                Poli3Alistirma.size = (0.06, 0.1)
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0, 0)
                Poli4Alistirma.size = (0.06, 0.1)
            elif dizi[0] == 3:
                image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Alistirma_2.size = (0.06, 0.1)
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0, 0)
                Poli4Alistirma.size = (0.06, 0.1)
                image1Alistirma_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Alistirma_2.size = (0, 0)
                Poli1Alistirma.size = (0.06, 0.1)
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0, 0)
                Poli2Alistirma.size = (0.06, 0.1)
            elif dizi[0] == 4:
                image4Alistirma_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Alistirma_2.size = (0.06, 0.1)
                image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Alistirma_2.size = (0, 0)
                Poli3Alistirma.size = (0.06, 0.1)
                image1Alistirma_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Alistirma_2.size = (0, 0)
                Poli1Alistirma.size = (0.06, 0.1)
                image2Alistirma_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Alistirma_2.size = (0, 0)
                Poli2Alistirma.size = (0.06, 0.1)
    
    elif kosulAlistirma.text == "LW":
        if cevapAlistirma.text == "z":
            if degisken == 1:
                image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Alistirma_2.size = (0.06, 0.1)
                Poli2Alistirma.size = (0.06, 0.1)
                Poli3Alistirma.size = (0.06, 0.1)
                Poli4Alistirma.size = (0.06, 0.1)
            elif degisken == 2:
                image2Alistirma_2.setColor([r2,g2,b2], colorSpace='rgb')
                image2Alistirma_2.size = (0.06, 0.1)
                Poli1Alistirma.size = (0.06, 0.1)
                Poli3Alistirma.size = (0.06, 0.1)
                Poli4Alistirma.size = (0.06, 0.1)
            elif degisken == 3:
                image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Alistirma_2.size = (0.06, 0.1)
                Poli1Alistirma.size = (0.06, 0.1)
                Poli2Alistirma.size = (0.06, 0.1)
                Poli4Alistirma.size = (0.06, 0.1)
            elif degisken == 4:
                image4Alistirma_2.setColor([r4,g4,b4], colorSpace='rgb')
                image4Alistirma_2.size = (0.06, 0.1)
                Poli1Alistirma.size = (0.06, 0.1)
                Poli2Alistirma.size = (0.06, 0.1)
                Poli3Alistirma.size = (0.06, 0.1)
    
        if cevapAlistirma.text == "x":
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
                
                
            if degisken == 1:
                image1Alistirma_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Alistirma_2.size = (0.06, 0.1)
                Poli2Alistirma.size = (0.06, 0.1)
                Poli3Alistirma.size = (0.06, 0.1)
                Poli4Alistirma.size = (0.06, 0.1)
            elif degisken == 2:
                image2Alistirma_2.setColor([r2,g2,b2], colorSpace='rgb')
                image2Alistirma_2.size = (0.06, 0.1)
                Poli1Alistirma.size = (0.06, 0.1)
                Poli3Alistirma.size = (0.06, 0.1)
                Poli4Alistirma.size = (0.06, 0.1)
            elif degisken == 3:
                image3Alistirma_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Alistirma_2.size = (0.06, 0.1)
                Poli1Alistirma.size = (0.06, 0.1)
                Poli2Alistirma.size = (0.06, 0.1)
                Poli4Alistirma.size = (0.06, 0.1)
            elif degisken == 4:
                image4Alistirma_2.setColor([r4,g4,b4], colorSpace='rgb')
                image4Alistirma_2.size = (0.06, 0.1)
                Poli1Alistirma.size = (0.06, 0.1)
                Poli2Alistirma.size = (0.06, 0.1)
                Poli3Alistirma.size = (0.06, 0.1)
    # keep track of which components have finished
    Alistirma_ChangeDetectionComponents = [image1Alistirma_2, image2Alistirma_2, image3Alistirma_2, image4Alistirma_2, image5Alistirma_2, Poli1Alistirma, Poli2Alistirma, Poli3Alistirma, Poli4Alistirma, Poli5Alistirma, KeyAlistirma_2, SoundAlistirma_2]
    for thisComponent in Alistirma_ChangeDetectionComponents:
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
    
    # --- Run Routine "Alistirma_ChangeDetection" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1Alistirma_2* updates
        
        # if image1Alistirma_2 is starting this frame...
        if image1Alistirma_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image1Alistirma_2.frameNStart = frameN  # exact frame index
            image1Alistirma_2.tStart = t  # local t and not account for scr refresh
            image1Alistirma_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1Alistirma_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image1Alistirma_2.started')
            # update status
            image1Alistirma_2.status = STARTED
            image1Alistirma_2.setAutoDraw(True)
        
        # if image1Alistirma_2 is active this frame...
        if image1Alistirma_2.status == STARTED:
            # update params
            pass
        
        # *image2Alistirma_2* updates
        
        # if image2Alistirma_2 is starting this frame...
        if image2Alistirma_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image2Alistirma_2.frameNStart = frameN  # exact frame index
            image2Alistirma_2.tStart = t  # local t and not account for scr refresh
            image2Alistirma_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2Alistirma_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2Alistirma_2.started')
            # update status
            image2Alistirma_2.status = STARTED
            image2Alistirma_2.setAutoDraw(True)
        
        # if image2Alistirma_2 is active this frame...
        if image2Alistirma_2.status == STARTED:
            # update params
            pass
        
        # *image3Alistirma_2* updates
        
        # if image3Alistirma_2 is starting this frame...
        if image3Alistirma_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image3Alistirma_2.frameNStart = frameN  # exact frame index
            image3Alistirma_2.tStart = t  # local t and not account for scr refresh
            image3Alistirma_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3Alistirma_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image3Alistirma_2.started')
            # update status
            image3Alistirma_2.status = STARTED
            image3Alistirma_2.setAutoDraw(True)
        
        # if image3Alistirma_2 is active this frame...
        if image3Alistirma_2.status == STARTED:
            # update params
            pass
        
        # *image4Alistirma_2* updates
        
        # if image4Alistirma_2 is starting this frame...
        if image4Alistirma_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image4Alistirma_2.frameNStart = frameN  # exact frame index
            image4Alistirma_2.tStart = t  # local t and not account for scr refresh
            image4Alistirma_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4Alistirma_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image4Alistirma_2.started')
            # update status
            image4Alistirma_2.status = STARTED
            image4Alistirma_2.setAutoDraw(True)
        
        # if image4Alistirma_2 is active this frame...
        if image4Alistirma_2.status == STARTED:
            # update params
            pass
        
        # *image5Alistirma_2* updates
        
        # if image5Alistirma_2 is starting this frame...
        if image5Alistirma_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image5Alistirma_2.frameNStart = frameN  # exact frame index
            image5Alistirma_2.tStart = t  # local t and not account for scr refresh
            image5Alistirma_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5Alistirma_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image5Alistirma_2.started')
            # update status
            image5Alistirma_2.status = STARTED
            image5Alistirma_2.setAutoDraw(True)
        
        # if image5Alistirma_2 is active this frame...
        if image5Alistirma_2.status == STARTED:
            # update params
            pass
        
        # *Poli1Alistirma* updates
        
        # if Poli1Alistirma is starting this frame...
        if Poli1Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli1Alistirma.frameNStart = frameN  # exact frame index
            Poli1Alistirma.tStart = t  # local t and not account for scr refresh
            Poli1Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli1Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli1Alistirma.started')
            # update status
            Poli1Alistirma.status = STARTED
            Poli1Alistirma.setAutoDraw(True)
        
        # if Poli1Alistirma is active this frame...
        if Poli1Alistirma.status == STARTED:
            # update params
            pass
        
        # *Poli2Alistirma* updates
        
        # if Poli2Alistirma is starting this frame...
        if Poli2Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli2Alistirma.frameNStart = frameN  # exact frame index
            Poli2Alistirma.tStart = t  # local t and not account for scr refresh
            Poli2Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli2Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli2Alistirma.started')
            # update status
            Poli2Alistirma.status = STARTED
            Poli2Alistirma.setAutoDraw(True)
        
        # if Poli2Alistirma is active this frame...
        if Poli2Alistirma.status == STARTED:
            # update params
            pass
        
        # *Poli3Alistirma* updates
        
        # if Poli3Alistirma is starting this frame...
        if Poli3Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli3Alistirma.frameNStart = frameN  # exact frame index
            Poli3Alistirma.tStart = t  # local t and not account for scr refresh
            Poli3Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli3Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli3Alistirma.started')
            # update status
            Poli3Alistirma.status = STARTED
            Poli3Alistirma.setAutoDraw(True)
        
        # if Poli3Alistirma is active this frame...
        if Poli3Alistirma.status == STARTED:
            # update params
            pass
        
        # *Poli4Alistirma* updates
        
        # if Poli4Alistirma is starting this frame...
        if Poli4Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli4Alistirma.frameNStart = frameN  # exact frame index
            Poli4Alistirma.tStart = t  # local t and not account for scr refresh
            Poli4Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli4Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli4Alistirma.started')
            # update status
            Poli4Alistirma.status = STARTED
            Poli4Alistirma.setAutoDraw(True)
        
        # if Poli4Alistirma is active this frame...
        if Poli4Alistirma.status == STARTED:
            # update params
            pass
        
        # *Poli5Alistirma* updates
        
        # if Poli5Alistirma is starting this frame...
        if Poli5Alistirma.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli5Alistirma.frameNStart = frameN  # exact frame index
            Poli5Alistirma.tStart = t  # local t and not account for scr refresh
            Poli5Alistirma.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli5Alistirma, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli5Alistirma.started')
            # update status
            Poli5Alistirma.status = STARTED
            Poli5Alistirma.setAutoDraw(True)
        
        # if Poli5Alistirma is active this frame...
        if Poli5Alistirma.status == STARTED:
            # update params
            pass
        
        # *KeyAlistirma_2* updates
        waitOnFlip = False
        
        # if KeyAlistirma_2 is starting this frame...
        if KeyAlistirma_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KeyAlistirma_2.frameNStart = frameN  # exact frame index
            KeyAlistirma_2.tStart = t  # local t and not account for scr refresh
            KeyAlistirma_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyAlistirma_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KeyAlistirma_2.started')
            # update status
            KeyAlistirma_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyAlistirma_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyAlistirma_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyAlistirma_2.status == STARTED and not waitOnFlip:
            theseKeys = KeyAlistirma_2.getKeys(keyList=['z','x'], waitRelease=False)
            _KeyAlistirma_2_allKeys.extend(theseKeys)
            if len(_KeyAlistirma_2_allKeys):
                KeyAlistirma_2.keys = _KeyAlistirma_2_allKeys[-1].name  # just the last key pressed
                KeyAlistirma_2.rt = _KeyAlistirma_2_allKeys[-1].rt
                # was this correct?
                if (KeyAlistirma_2.keys == str(taskcevap)) or (KeyAlistirma_2.keys == taskcevap):
                    KeyAlistirma_2.corr = 1
                else:
                    KeyAlistirma_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SoundAlistirma_2
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Alistirma_ChangeDetectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Alistirma_ChangeDetection" ---
    for thisComponent in Alistirma_ChangeDetectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyAlistirma_2.keys in ['', [], None]:  # No response was made
        KeyAlistirma_2.keys = None
        # was no response the correct answer?!
        if str(taskcevap).lower() == 'none':
           KeyAlistirma_2.corr = 1;  # correct non-response
        else:
           KeyAlistirma_2.corr = 0;  # failed to respond (incorrectly)
    # store data for ConditionAlistirma (TrialHandler)
    ConditionAlistirma.addData('KeyAlistirma_2.keys',KeyAlistirma_2.keys)
    ConditionAlistirma.addData('KeyAlistirma_2.corr', KeyAlistirma_2.corr)
    if KeyAlistirma_2.keys != None:  # we had a response
        ConditionAlistirma.addData('KeyAlistirma_2.rt', KeyAlistirma_2.rt)
    SoundAlistirma_2.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CodeTaskAlistirma
    if KeyAlistirma_2.corr == 0:
        SoundAlistirma_2.play()
        
    if counter == 16:
        ConditionAlistirma.finished = True
    # the Routine "Alistirma_ChangeDetection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'ConditionAlistirma'


# --- Prepare to start Routine "ConditionLNStart" ---
continueRoutine = True
# update component parameters for each repeat
KeyboardStart.keys = []
KeyboardStart.rt = []
_KeyboardStart_allKeys = []
# keep track of which components have finished
ConditionLNStartComponents = [KeyboardStart, TextStart]
for thisComponent in ConditionLNStartComponents:
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

# --- Run Routine "ConditionLNStart" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *KeyboardStart* updates
    waitOnFlip = False
    
    # if KeyboardStart is starting this frame...
    if KeyboardStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KeyboardStart.frameNStart = frameN  # exact frame index
        KeyboardStart.tStart = t  # local t and not account for scr refresh
        KeyboardStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KeyboardStart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'KeyboardStart.started')
        # update status
        KeyboardStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KeyboardStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KeyboardStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KeyboardStart.status == STARTED and not waitOnFlip:
        theseKeys = KeyboardStart.getKeys(keyList=None, waitRelease=False)
        _KeyboardStart_allKeys.extend(theseKeys)
        if len(_KeyboardStart_allKeys):
            KeyboardStart.keys = _KeyboardStart_allKeys[-1].name  # just the last key pressed
            KeyboardStart.rt = _KeyboardStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *TextStart* updates
    
    # if TextStart is starting this frame...
    if TextStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextStart.frameNStart = frameN  # exact frame index
        TextStart.tStart = t  # local t and not account for scr refresh
        TextStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextStart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextStart.started')
        # update status
        TextStart.status = STARTED
        TextStart.setAutoDraw(True)
    
    # if TextStart is active this frame...
    if TextStart.status == STARTED:
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
    for thisComponent in ConditionLNStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ConditionLNStart" ---
for thisComponent in ConditionLNStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if KeyboardStart.keys in ['', [], None]:  # No response was made
    KeyboardStart.keys = None
thisExp.addData('KeyboardStart.keys',KeyboardStart.keys)
if KeyboardStart.keys != None:  # we had a response
    thisExp.addData('KeyboardStart.rt', KeyboardStart.rt)
thisExp.nextEntry()
# the Routine "ConditionLNStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ConditionDeney = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('replication_of_lee_and_jeong_exp1.xlsx'),
    seed=None, name='ConditionDeney')
thisExp.addLoop(ConditionDeney)  # add the loop to the experiment
thisConditionDeney = ConditionDeney.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConditionDeney.rgb)
if thisConditionDeney != None:
    for paramName in thisConditionDeney:
        exec('{} = thisConditionDeney[paramName]'.format(paramName))

for thisConditionDeney in ConditionDeney:
    currentLoop = ConditionDeney
    # abbreviate parameter names if possible (e.g. rgb = thisConditionDeney.rgb)
    if thisConditionDeney != None:
        for paramName in thisConditionDeney:
            exec('{} = thisConditionDeney[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Deney_Fixation800ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    kosulDeney.setText(condition)
    cevapDeney.setText(taskcevap)
    # keep track of which components have finished
    Deney_Fixation800msComponents = [image800Deney, kosulDeney, cevapDeney]
    for thisComponent in Deney_Fixation800msComponents:
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
    
    # --- Run Routine "Deney_Fixation800ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image800Deney* updates
        
        # if image800Deney is starting this frame...
        if image800Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image800Deney.frameNStart = frameN  # exact frame index
            image800Deney.tStart = t  # local t and not account for scr refresh
            image800Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image800Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image800Deney.started')
            # update status
            image800Deney.status = STARTED
            image800Deney.setAutoDraw(True)
        
        # if image800Deney is active this frame...
        if image800Deney.status == STARTED:
            # update params
            pass
        
        # if image800Deney is stopping this frame...
        if image800Deney.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                image800Deney.tStop = t  # not accounting for scr refresh
                image800Deney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image800Deney.stopped')
                # update status
                image800Deney.status = FINISHED
                image800Deney.setAutoDraw(False)
        
        # *kosulDeney* updates
        
        # if kosulDeney is starting this frame...
        if kosulDeney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            kosulDeney.frameNStart = frameN  # exact frame index
            kosulDeney.tStart = t  # local t and not account for scr refresh
            kosulDeney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kosulDeney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'kosulDeney.started')
            # update status
            kosulDeney.status = STARTED
            kosulDeney.setAutoDraw(True)
        
        # if kosulDeney is active this frame...
        if kosulDeney.status == STARTED:
            # update params
            pass
        
        # if kosulDeney is stopping this frame...
        if kosulDeney.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                kosulDeney.tStop = t  # not accounting for scr refresh
                kosulDeney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kosulDeney.stopped')
                # update status
                kosulDeney.status = FINISHED
                kosulDeney.setAutoDraw(False)
        
        # *cevapDeney* updates
        
        # if cevapDeney is starting this frame...
        if cevapDeney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            cevapDeney.frameNStart = frameN  # exact frame index
            cevapDeney.tStart = t  # local t and not account for scr refresh
            cevapDeney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cevapDeney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cevapDeney.started')
            # update status
            cevapDeney.status = STARTED
            cevapDeney.setAutoDraw(True)
        
        # if cevapDeney is active this frame...
        if cevapDeney.status == STARTED:
            # update params
            pass
        
        # if cevapDeney is stopping this frame...
        if cevapDeney.status == STARTED:
            if frameN >= 48:
                # keep track of stop time/frame for later
                cevapDeney.tStop = t  # not accounting for scr refresh
                cevapDeney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cevapDeney.stopped')
                # update status
                cevapDeney.status = FINISHED
                cevapDeney.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Deney_Fixation800msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deney_Fixation800ms" ---
    for thisComponent in Deney_Fixation800msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Code800Deney
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
    # the Routine "Deney_Fixation800ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Deney_Load200ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    image1Deney.setColor([r1,g1,b1], colorSpace='rgb')
    image2Deney.setColor([r2,g2,b2], colorSpace='rgb')
    image3Deney.setColor([r3,g3,b3], colorSpace='rgb')
    image4Deney.setColor([r4,g4,b4], colorSpace='rgb')
    image5Deney.setColor([r5,g5,b5], colorSpace='rgb')
    # Run 'Begin Routine' code from CodeLoadDeney
    if kosulDeney.text == "LN":
        image5Deney.size = (0.06, 0.1)
    elif kosulDeney.text == "HW":
        image1Deney.size = (0.06, 0.1)
        image2Deney.size = (0.06, 0.1)
        image3Deney.size = (0.06, 0.1)
        image4Deney.size = (0.06, 0.1)
    elif kosulDeney.text == "LW":
        dizi = [1,2,3,4]
        shuffle(dizi)
        
        if dizi[0] == 1:
            image2Deney.color = "white"
            image3Deney.color = "white"
            image4Deney.color = "white"
            degisken = 1
        elif dizi[0] == 2:
            image1Deney.color = "white"
            image3Deney.color = "white"
            image4Deney.color = "white"
            degisken = 2
        elif dizi[0] == 3:
            image1Deney.color = "white"
            image2Deney.color = "white"
            image4Deneycolor = "white"
            degisken = 3
        elif dizi[0] == 4:
            image1Deney.color = "white"
            image2Deney.color = "white"
            image3Deney.color = "white"
            degisken = 4
            
        image1Deney.size = (0.06, 0.1)
        image2Deney.size = (0.06, 0.1)
        image3Deney.size = (0.06, 0.1)
        image4Deney.size = (0.06, 0.1)
    # keep track of which components have finished
    Deney_Load200msComponents = [image1Deney, image2Deney, image3Deney, image4Deney, image5Deney]
    for thisComponent in Deney_Load200msComponents:
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
    
    # --- Run Routine "Deney_Load200ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1Deney* updates
        
        # if image1Deney is starting this frame...
        if image1Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image1Deney.frameNStart = frameN  # exact frame index
            image1Deney.tStart = t  # local t and not account for scr refresh
            image1Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image1Deney.started')
            # update status
            image1Deney.status = STARTED
            image1Deney.setAutoDraw(True)
        
        # if image1Deney is active this frame...
        if image1Deney.status == STARTED:
            # update params
            pass
        
        # if image1Deney is stopping this frame...
        if image1Deney.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image1Deney.tStop = t  # not accounting for scr refresh
                image1Deney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1Deney.stopped')
                # update status
                image1Deney.status = FINISHED
                image1Deney.setAutoDraw(False)
        
        # *image2Deney* updates
        
        # if image2Deney is starting this frame...
        if image2Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image2Deney.frameNStart = frameN  # exact frame index
            image2Deney.tStart = t  # local t and not account for scr refresh
            image2Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2Deney.started')
            # update status
            image2Deney.status = STARTED
            image2Deney.setAutoDraw(True)
        
        # if image2Deney is active this frame...
        if image2Deney.status == STARTED:
            # update params
            pass
        
        # if image2Deney is stopping this frame...
        if image2Deney.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image2Deney.tStop = t  # not accounting for scr refresh
                image2Deney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image2Deney.stopped')
                # update status
                image2Deney.status = FINISHED
                image2Deney.setAutoDraw(False)
        
        # *image3Deney* updates
        
        # if image3Deney is starting this frame...
        if image3Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image3Deney.frameNStart = frameN  # exact frame index
            image3Deney.tStart = t  # local t and not account for scr refresh
            image3Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image3Deney.started')
            # update status
            image3Deney.status = STARTED
            image3Deney.setAutoDraw(True)
        
        # if image3Deney is active this frame...
        if image3Deney.status == STARTED:
            # update params
            pass
        
        # if image3Deney is stopping this frame...
        if image3Deney.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image3Deney.tStop = t  # not accounting for scr refresh
                image3Deney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image3Deney.stopped')
                # update status
                image3Deney.status = FINISHED
                image3Deney.setAutoDraw(False)
        
        # *image4Deney* updates
        
        # if image4Deney is starting this frame...
        if image4Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image4Deney.frameNStart = frameN  # exact frame index
            image4Deney.tStart = t  # local t and not account for scr refresh
            image4Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image4Deney.started')
            # update status
            image4Deney.status = STARTED
            image4Deney.setAutoDraw(True)
        
        # if image4Deney is active this frame...
        if image4Deney.status == STARTED:
            # update params
            pass
        
        # if image4Deney is stopping this frame...
        if image4Deney.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image4Deney.tStop = t  # not accounting for scr refresh
                image4Deney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image4Deney.stopped')
                # update status
                image4Deney.status = FINISHED
                image4Deney.setAutoDraw(False)
        
        # *image5Deney* updates
        
        # if image5Deney is starting this frame...
        if image5Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image5Deney.frameNStart = frameN  # exact frame index
            image5Deney.tStart = t  # local t and not account for scr refresh
            image5Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image5Deney.started')
            # update status
            image5Deney.status = STARTED
            image5Deney.setAutoDraw(True)
        
        # if image5Deney is active this frame...
        if image5Deney.status == STARTED:
            # update params
            pass
        
        # if image5Deney is stopping this frame...
        if image5Deney.status == STARTED:
            if frameN >= 12:
                # keep track of stop time/frame for later
                image5Deney.tStop = t  # not accounting for scr refresh
                image5Deney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image5Deney.stopped')
                # update status
                image5Deney.status = FINISHED
                image5Deney.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Deney_Load200msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deney_Load200ms" ---
    for thisComponent in Deney_Load200msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Deney_Load200ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Deney_BlankScreen2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Deney_BlankScreen2000msComponents = [BlankDeney]
    for thisComponent in Deney_BlankScreen2000msComponents:
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
    
    # --- Run Routine "Deney_BlankScreen2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankDeney* updates
        
        # if BlankDeney is starting this frame...
        if BlankDeney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            BlankDeney.frameNStart = frameN  # exact frame index
            BlankDeney.tStart = t  # local t and not account for scr refresh
            BlankDeney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankDeney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BlankDeney.started')
            # update status
            BlankDeney.status = STARTED
            BlankDeney.setAutoDraw(True)
        
        # if BlankDeney is active this frame...
        if BlankDeney.status == STARTED:
            # update params
            pass
        
        # if BlankDeney is stopping this frame...
        if BlankDeney.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                BlankDeney.tStop = t  # not accounting for scr refresh
                BlankDeney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BlankDeney.stopped')
                # update status
                BlankDeney.status = FINISHED
                BlankDeney.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Deney_BlankScreen2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deney_BlankScreen2000ms" ---
    for thisComponent in Deney_BlankScreen2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Deney_BlankScreen2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Deney_FlankerTask2000ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    HedefDeney.setPos(pozisyonhedef)
    HedefDeney.setText(hedef)
    CeldiriciDeney.setPos(pozisyonceldirici)
    CeldiriciDeney.setText(celdirici)
    KeyDeney.keys = []
    KeyDeney.rt = []
    _KeyDeney_allKeys = []
    SoundDeney.setSound('yanlis.wav', hamming=True)
    SoundDeney.setVolume(1.0, log=False)
    # keep track of which components have finished
    Deney_FlankerTask2000msComponents = [HedefDeney, CeldiriciDeney, KeyDeney, SoundDeney]
    for thisComponent in Deney_FlankerTask2000msComponents:
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
    
    # --- Run Routine "Deney_FlankerTask2000ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HedefDeney* updates
        
        # if HedefDeney is starting this frame...
        if HedefDeney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            HedefDeney.frameNStart = frameN  # exact frame index
            HedefDeney.tStart = t  # local t and not account for scr refresh
            HedefDeney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HedefDeney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HedefDeney.started')
            # update status
            HedefDeney.status = STARTED
            HedefDeney.setAutoDraw(True)
        
        # if HedefDeney is active this frame...
        if HedefDeney.status == STARTED:
            # update params
            pass
        
        # if HedefDeney is stopping this frame...
        if HedefDeney.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                HedefDeney.tStop = t  # not accounting for scr refresh
                HedefDeney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HedefDeney.stopped')
                # update status
                HedefDeney.status = FINISHED
                HedefDeney.setAutoDraw(False)
        
        # *CeldiriciDeney* updates
        
        # if CeldiriciDeney is starting this frame...
        if CeldiriciDeney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            CeldiriciDeney.frameNStart = frameN  # exact frame index
            CeldiriciDeney.tStart = t  # local t and not account for scr refresh
            CeldiriciDeney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CeldiriciDeney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CeldiriciDeney.started')
            # update status
            CeldiriciDeney.status = STARTED
            CeldiriciDeney.setAutoDraw(True)
        
        # if CeldiriciDeney is active this frame...
        if CeldiriciDeney.status == STARTED:
            # update params
            pass
        
        # if CeldiriciDeney is stopping this frame...
        if CeldiriciDeney.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                CeldiriciDeney.tStop = t  # not accounting for scr refresh
                CeldiriciDeney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CeldiriciDeney.stopped')
                # update status
                CeldiriciDeney.status = FINISHED
                CeldiriciDeney.setAutoDraw(False)
        
        # *KeyDeney* updates
        waitOnFlip = False
        
        # if KeyDeney is starting this frame...
        if KeyDeney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KeyDeney.frameNStart = frameN  # exact frame index
            KeyDeney.tStart = t  # local t and not account for scr refresh
            KeyDeney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyDeney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KeyDeney.started')
            # update status
            KeyDeney.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyDeney.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyDeney.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if KeyDeney is stopping this frame...
        if KeyDeney.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                KeyDeney.tStop = t  # not accounting for scr refresh
                KeyDeney.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'KeyDeney.stopped')
                # update status
                KeyDeney.status = FINISHED
                KeyDeney.status = FINISHED
        if KeyDeney.status == STARTED and not waitOnFlip:
            theseKeys = KeyDeney.getKeys(keyList=['h','s'], waitRelease=False)
            _KeyDeney_allKeys.extend(theseKeys)
            if len(_KeyDeney_allKeys):
                KeyDeney.keys = _KeyDeney_allKeys[0].name  # just the first key pressed
                KeyDeney.rt = _KeyDeney_allKeys[0].rt
                # was this correct?
                if (KeyDeney.keys == str(flankercevap)) or (KeyDeney.keys == flankercevap):
                    KeyDeney.corr = 1
                else:
                    KeyDeney.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SoundDeney
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Deney_FlankerTask2000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deney_FlankerTask2000ms" ---
    for thisComponent in Deney_FlankerTask2000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyDeney.keys in ['', [], None]:  # No response was made
        KeyDeney.keys = None
        # was no response the correct answer?!
        if str(flankercevap).lower() == 'none':
           KeyDeney.corr = 1;  # correct non-response
        else:
           KeyDeney.corr = 0;  # failed to respond (incorrectly)
    # store data for ConditionDeney (TrialHandler)
    ConditionDeney.addData('KeyDeney.keys',KeyDeney.keys)
    ConditionDeney.addData('KeyDeney.corr', KeyDeney.corr)
    if KeyDeney.keys != None:  # we had a response
        ConditionDeney.addData('KeyDeney.rt', KeyDeney.rt)
    SoundDeney.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CodeFlankerDeney
    if KeyDeney.keys == None:
        SoundDeney.play()
    # the Routine "Deney_FlankerTask2000ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Deney_Fixation500ms" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Deney_Fixation500msComponents = [FlankerDeneyFix]
    for thisComponent in Deney_Fixation500msComponents:
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
    
    # --- Run Routine "Deney_Fixation500ms" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FlankerDeneyFix* updates
        
        # if FlankerDeneyFix is starting this frame...
        if FlankerDeneyFix.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            FlankerDeneyFix.frameNStart = frameN  # exact frame index
            FlankerDeneyFix.tStart = t  # local t and not account for scr refresh
            FlankerDeneyFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FlankerDeneyFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FlankerDeneyFix.started')
            # update status
            FlankerDeneyFix.status = STARTED
            FlankerDeneyFix.setAutoDraw(True)
        
        # if FlankerDeneyFix is active this frame...
        if FlankerDeneyFix.status == STARTED:
            # update params
            pass
        
        # if FlankerDeneyFix is stopping this frame...
        if FlankerDeneyFix.status == STARTED:
            if frameN >= 30:
                # keep track of stop time/frame for later
                FlankerDeneyFix.tStop = t  # not accounting for scr refresh
                FlankerDeneyFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FlankerDeneyFix.stopped')
                # update status
                FlankerDeneyFix.status = FINISHED
                FlankerDeneyFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Deney_Fixation500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deney_Fixation500ms" ---
    for thisComponent in Deney_Fixation500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Deney_Fixation500ms" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Deney_ChangeDetection" ---
    continueRoutine = True
    # update component parameters for each repeat
    image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
    image2Deney_2.setColor([r2,g2,b2], colorSpace='rgb')
    image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
    image4Deney_2.setColor([r4,g4,b4], colorSpace='rgb')
    image5Deney_2.setColor([r5,g5,b5], colorSpace='rgb')
    KeyDeney_2.keys = []
    KeyDeney_2.rt = []
    _KeyDeney_2_allKeys = []
    SoundDeney_2.setSound('yanlis.wav', hamming=True)
    SoundDeney_2.setVolume(1.0, log=False)
    # Run 'Begin Routine' code from CodeTaskDeney
    image1Deney_2.size = (0, 0)
    image2Deney_2.size = (0, 0)
    image3Deney_2.size = (0, 0)
    image4Deney_2.size = (0, 0)
    image5Deney_2.size = (0, 0)
    Poli1Deney.size = (0, 0)
    Poli2Deney.size = (0, 0)
    Poli3Deney.size = (0, 0)
    Poli4Deney.size = (0, 0)
    Poli5Deney.size = (0, 0)
    
    if kosulDeney.text == "LN":
        if cevapDeney.text == "z":
            image5Deney_2.setColor([r5,g5,b5], colorSpace='rgb')
            image5Deney_2.size = (0.06, 0.1)
    
        if cevapDeney.text == "x":
            r5 = float(round(r5,4)) + 0.5333
            g5 = float(round(g5,4)) + 0.5333
            b5 = float(round(b5,4)) + 0.5333
           
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
                
            image5Deney_2.setColor([r5,g5,b5], colorSpace='rgb')
            image5Deney_2.size = (0.06, 0.1)
    
    elif kosulDeney.text == "HW": 
        if cevapDeney.text == "z":
            dizi = [1,2,3,4]
            shuffle(dizi)
            if dizi[0] == 1:
                image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Deney_2.size = (0.06, 0.1)
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0, 0)
                Poli2Deney.size = (0.06, 0.1)
                image3Deney_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Deney_2.size = (0, 0)
                Poli3Deney.size = (0.06, 0.1)
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0, 0)
                Poli4Deney.size = (0.06, 0.1)
            elif dizi[0] == 2:
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0.06, 0.1)
                image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Deney_2.size = (0, 0)
                Poli1Deney.size = (0.06, 0.1)
                image3Deney_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Deney_2.size = (0, 0)
                Poli3Deney.size = (0.06, 0.1)
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0, 0)
                Poli4Deney.size = (0.06, 0.1)
            elif dizi[0] == 3:
                image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Deney_2.size = (0.06, 0.1)
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0, 0)
                Poli4Deney.size = (0.06, 0.1)
                image1Deney_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Deney_2.size = (0, 0)
                Poli1Deney.size = (0.06, 0.1)
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0, 0)
                Poli2Deney.size = (0.06, 0.1)
            elif dizi[0] == 4:
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0.06, 0.1)
                image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Deney_2.size = (0, 0)
                Poli3Deney.size = (0.06, 0.1)
                image1Deney_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Deney_2.size = (0, 0)
                Poli1Deney.size = (0.06, 0.1)
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0, 0)
                Poli2Deney.size = (0.06, 0.1)
        
        if cevapDeney.text == "x":
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
                image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Deney_2.size = (0.06, 0.1)
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0, 0)
                Poli2Deney.size = (0.06, 0.1)
                image3Deney_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Deney_2.size = (0, 0)
                Poli3Deney.size = (0.06, 0.1)
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0, 0)
                Poli4Deney.size = (0.06, 0.1)
            elif dizi[0] == 2:
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0.06, 0.1)
                image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Deney_2.size = (0, 0)
                Poli1Deney.size = (0.06, 0.1)
                image3Deney_2.setColor([r3,g3,g3], colorSpace='rgb')
                image3Deney_2.size = (0, 0)
                Poli3Deney.size = (0.06, 0.1)
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0, 0)
                Poli4Deney.size = (0.06, 0.1)
            elif dizi[0] == 3:
                image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Deney_2.size = (0.06, 0.1)
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0, 0)
                Poli4Deney.size = (0.06, 0.1)
                image1Deney_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Deney_2.size = (0, 0)
                Poli1Deney.size = (0.06, 0.1)
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0, 0)
                Poli2Deney.size = (0.06, 0.1)
            elif dizi[0] == 4:
                image4Deney_2.setColor([r4,g4,g4], colorSpace='rgb')
                image4Deney_2.size = (0.06, 0.1)
                image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Deney_2.size = (0, 0)
                Poli3Deney.size = (0.06, 0.1)
                image1Deney_2.setColor([r1,g1,g1], colorSpace='rgb')
                image1Deney_2.size = (0, 0)
                Poli1Deney.size = (0.06, 0.1)
                image2Deney_2.setColor([r2,g2,g2], colorSpace='rgb')
                image2Deney_2.size = (0, 0)
                Poli2Deney.size = (0.06, 0.1)
    
    elif kosulDeney.text == "LW":
        if cevapDeney.text == "z":
            if degisken == 1:
                image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Deney_2.size = (0.06, 0.1)
                Poli2Deney.size = (0.06, 0.1)
                Poli3Deney.size = (0.06, 0.1)
                Poli4Deney.size = (0.06, 0.1)
            elif degisken == 2:
                image2Deney_2.setColor([r2,g2,b2], colorSpace='rgb')
                image2Deney_2.size = (0.06, 0.1)
                Poli1Deney.size = (0.06, 0.1)
                Poli3Deney.size = (0.06, 0.1)
                Poli4Deney.size = (0.06, 0.1)
            elif degisken == 3:
                image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Deney_2.size = (0.06, 0.1)
                Poli1Deney.size = (0.06, 0.1)
                Poli2Deney.size = (0.06, 0.1)
                Poli4Deney.size = (0.06, 0.1)
            elif degisken == 4:
                image4Deney_2.setColor([r4,g4,b4], colorSpace='rgb')
                image4Deney_2.size = (0.06, 0.1)
                Poli1Deney.size = (0.06, 0.1)
                Poli2Deney.size = (0.06, 0.1)
                Poli3Deney.size = (0.06, 0.1)
    
        if cevapDeney.text == "x":
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
                
                
            if degisken == 1:
                image1Deney_2.setColor([r1,g1,b1], colorSpace='rgb')
                image1Deney_2.size = (0.06, 0.1)
                Poli2Deney.size = (0.06, 0.1)
                Poli3Deney.size = (0.06, 0.1)
                Poli4Deney.size = (0.06, 0.1)
            elif degisken == 2:
                image2Deney_2.setColor([r2,g2,b2], colorSpace='rgb')
                image2Deney_2.size = (0.06, 0.1)
                Poli1Deney.size = (0.06, 0.1)
                Poli3Deney.size = (0.06, 0.1)
                Poli4Deney.size = (0.06, 0.1)
            elif degisken == 3:
                image3Deney_2.setColor([r3,g3,b3], colorSpace='rgb')
                image3Deney_2.size = (0.06, 0.1)
                Poli1Deney.size = (0.06, 0.1)
                Poli2Deney.size = (0.06, 0.1)
                Poli4Deney.size = (0.06, 0.1)
            elif degisken == 4:
                image4Deney_2.setColor([r4,g4,b4], colorSpace='rgb')
                image4Deney_2.size = (0.06, 0.1)
                Poli1Deney.size = (0.06, 0.1)
                Poli2Deney.size = (0.06, 0.1)
                Poli3Deney.size = (0.06, 0.1)
    # keep track of which components have finished
    Deney_ChangeDetectionComponents = [image1Deney_2, image2Deney_2, image3Deney_2, image4Deney_2, image5Deney_2, Poli1Deney, Poli2Deney, Poli3Deney, Poli4Deney, Poli5Deney, KeyDeney_2, SoundDeney_2]
    for thisComponent in Deney_ChangeDetectionComponents:
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
    
    # --- Run Routine "Deney_ChangeDetection" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1Deney_2* updates
        
        # if image1Deney_2 is starting this frame...
        if image1Deney_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image1Deney_2.frameNStart = frameN  # exact frame index
            image1Deney_2.tStart = t  # local t and not account for scr refresh
            image1Deney_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1Deney_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image1Deney_2.started')
            # update status
            image1Deney_2.status = STARTED
            image1Deney_2.setAutoDraw(True)
        
        # if image1Deney_2 is active this frame...
        if image1Deney_2.status == STARTED:
            # update params
            pass
        
        # *image2Deney_2* updates
        
        # if image2Deney_2 is starting this frame...
        if image2Deney_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image2Deney_2.frameNStart = frameN  # exact frame index
            image2Deney_2.tStart = t  # local t and not account for scr refresh
            image2Deney_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2Deney_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2Deney_2.started')
            # update status
            image2Deney_2.status = STARTED
            image2Deney_2.setAutoDraw(True)
        
        # if image2Deney_2 is active this frame...
        if image2Deney_2.status == STARTED:
            # update params
            pass
        
        # *image3Deney_2* updates
        
        # if image3Deney_2 is starting this frame...
        if image3Deney_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image3Deney_2.frameNStart = frameN  # exact frame index
            image3Deney_2.tStart = t  # local t and not account for scr refresh
            image3Deney_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3Deney_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image3Deney_2.started')
            # update status
            image3Deney_2.status = STARTED
            image3Deney_2.setAutoDraw(True)
        
        # if image3Deney_2 is active this frame...
        if image3Deney_2.status == STARTED:
            # update params
            pass
        
        # *image4Deney_2* updates
        
        # if image4Deney_2 is starting this frame...
        if image4Deney_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image4Deney_2.frameNStart = frameN  # exact frame index
            image4Deney_2.tStart = t  # local t and not account for scr refresh
            image4Deney_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4Deney_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image4Deney_2.started')
            # update status
            image4Deney_2.status = STARTED
            image4Deney_2.setAutoDraw(True)
        
        # if image4Deney_2 is active this frame...
        if image4Deney_2.status == STARTED:
            # update params
            pass
        
        # *image5Deney_2* updates
        
        # if image5Deney_2 is starting this frame...
        if image5Deney_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image5Deney_2.frameNStart = frameN  # exact frame index
            image5Deney_2.tStart = t  # local t and not account for scr refresh
            image5Deney_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5Deney_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image5Deney_2.started')
            # update status
            image5Deney_2.status = STARTED
            image5Deney_2.setAutoDraw(True)
        
        # if image5Deney_2 is active this frame...
        if image5Deney_2.status == STARTED:
            # update params
            pass
        
        # *Poli1Deney* updates
        
        # if Poli1Deney is starting this frame...
        if Poli1Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli1Deney.frameNStart = frameN  # exact frame index
            Poli1Deney.tStart = t  # local t and not account for scr refresh
            Poli1Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli1Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli1Deney.started')
            # update status
            Poli1Deney.status = STARTED
            Poli1Deney.setAutoDraw(True)
        
        # if Poli1Deney is active this frame...
        if Poli1Deney.status == STARTED:
            # update params
            pass
        
        # *Poli2Deney* updates
        
        # if Poli2Deney is starting this frame...
        if Poli2Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli2Deney.frameNStart = frameN  # exact frame index
            Poli2Deney.tStart = t  # local t and not account for scr refresh
            Poli2Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli2Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli2Deney.started')
            # update status
            Poli2Deney.status = STARTED
            Poli2Deney.setAutoDraw(True)
        
        # if Poli2Deney is active this frame...
        if Poli2Deney.status == STARTED:
            # update params
            pass
        
        # *Poli3Deney* updates
        
        # if Poli3Deney is starting this frame...
        if Poli3Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli3Deney.frameNStart = frameN  # exact frame index
            Poli3Deney.tStart = t  # local t and not account for scr refresh
            Poli3Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli3Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli3Deney.started')
            # update status
            Poli3Deney.status = STARTED
            Poli3Deney.setAutoDraw(True)
        
        # if Poli3Deney is active this frame...
        if Poli3Deney.status == STARTED:
            # update params
            pass
        
        # *Poli4Deney* updates
        
        # if Poli4Deney is starting this frame...
        if Poli4Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli4Deney.frameNStart = frameN  # exact frame index
            Poli4Deney.tStart = t  # local t and not account for scr refresh
            Poli4Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli4Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli4Deney.started')
            # update status
            Poli4Deney.status = STARTED
            Poli4Deney.setAutoDraw(True)
        
        # if Poli4Deney is active this frame...
        if Poli4Deney.status == STARTED:
            # update params
            pass
        
        # *Poli5Deney* updates
        
        # if Poli5Deney is starting this frame...
        if Poli5Deney.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            Poli5Deney.frameNStart = frameN  # exact frame index
            Poli5Deney.tStart = t  # local t and not account for scr refresh
            Poli5Deney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Poli5Deney, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Poli5Deney.started')
            # update status
            Poli5Deney.status = STARTED
            Poli5Deney.setAutoDraw(True)
        
        # if Poli5Deney is active this frame...
        if Poli5Deney.status == STARTED:
            # update params
            pass
        
        # *KeyDeney_2* updates
        waitOnFlip = False
        
        # if KeyDeney_2 is starting this frame...
        if KeyDeney_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            KeyDeney_2.frameNStart = frameN  # exact frame index
            KeyDeney_2.tStart = t  # local t and not account for scr refresh
            KeyDeney_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(KeyDeney_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'KeyDeney_2.started')
            # update status
            KeyDeney_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(KeyDeney_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(KeyDeney_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if KeyDeney_2.status == STARTED and not waitOnFlip:
            theseKeys = KeyDeney_2.getKeys(keyList=['z','x'], waitRelease=False)
            _KeyDeney_2_allKeys.extend(theseKeys)
            if len(_KeyDeney_2_allKeys):
                KeyDeney_2.keys = _KeyDeney_2_allKeys[-1].name  # just the last key pressed
                KeyDeney_2.rt = _KeyDeney_2_allKeys[-1].rt
                # was this correct?
                if (KeyDeney_2.keys == str(taskcevap)) or (KeyDeney_2.keys == taskcevap):
                    KeyDeney_2.corr = 1
                else:
                    KeyDeney_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop SoundDeney_2
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Deney_ChangeDetectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deney_ChangeDetection" ---
    for thisComponent in Deney_ChangeDetectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyDeney_2.keys in ['', [], None]:  # No response was made
        KeyDeney_2.keys = None
        # was no response the correct answer?!
        if str(taskcevap).lower() == 'none':
           KeyDeney_2.corr = 1;  # correct non-response
        else:
           KeyDeney_2.corr = 0;  # failed to respond (incorrectly)
    # store data for ConditionDeney (TrialHandler)
    ConditionDeney.addData('KeyDeney_2.keys',KeyDeney_2.keys)
    ConditionDeney.addData('KeyDeney_2.corr', KeyDeney_2.corr)
    if KeyDeney_2.keys != None:  # we had a response
        ConditionDeney.addData('KeyDeney_2.rt', KeyDeney_2.rt)
    SoundDeney_2.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from CodeTaskDeney
    if KeyDeney_2.corr == 0:
        SoundDeney_2.play()
    # the Routine "Deney_ChangeDetection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'ConditionDeney'


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
