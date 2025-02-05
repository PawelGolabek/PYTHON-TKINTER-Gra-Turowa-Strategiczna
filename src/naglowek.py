import configparser
from dis import dis
from email.policy import default
from faulthandler import disable
from platform import system_alias
from tabnanny import check
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import Tk, Canvas, Frame, BOTH
from random import randint
import PIL.Image
import tkinter.ttk as ttk
import sys,os
from pathlib import Path

class ui_icons():
    x=10

class _events():
    playerDestroyed = False
    showedWin = False
    showedLoose = False
    disabledWin = False
    disabledLoose = False

    
class global_var():
    def __init__(self,config,root):
        self.finished = False
        self.shipChoiceRadioButtons = []
        self.radio = IntVar(root, 999)
        self.radio2 = IntVar(root, 999)
        self.ammunitionOptionChoice = StringVar(root)
        self.tmpCounter = 0
        # START CONDITIONS
        self.radio.set(0)
        ## DYNAMIC UI ##
        self.uiSystems = []
        self.uiSystemsAS = []
        self.uiSystemsProgressbars = []
        ## INPUT HANDLING VARIABLES ##
        self.mouseOnUI = FALSE
        self.mouseWheelUp = FALSE
        self.mouseWheelDown = FALSE
        self.mouseButton1 = FALSE
        self.updateTimer = -1
        self.frameTime = 0
        self.mouseButton2 = FALSE
        self.mouseButton3 = FALSE
        self.mouseButton3justPressed = FALSE
        self.mouseButton3released = FALSE
        self.prevPointerX = 0.0
        self.prevPointerY = 0.0
        self.pointerX = 0.0
        self.pointerX = 0.0
        self.pointerY = 0.0
        self.pointerDeltaX = 0.0
        self.pointerDeltaY = 0.0
        self.drag = ''
        ## GAME OPTIONS ##
        self.fogOfWar = True
        self.gameSpeed = 1
        self.turnLength = 1080
        self.zoom = 1
        self.shieldRegen = 1
        self.shieldMaxState = 1000
        self.respawns = 0
        self.enemyRespawns = 0
        # GAME DATA
        self.labelCounter = 0
        self.choices = StringVar()
        self.options = []
        self.shipChoice = ''
        self.landmarks = []
        self.ships = []
        self.turnInProgress = FALSE
        self.misslesShot = 0
        self.currentMissles = []
        self.lasers = []
        self.radio0Hidden = False
        self.radio1Hidden = False
        self.radio2Hidden = False
        # DRAW DATA
        self.paused = False
        self.pausedLVisible = False
        self.ovalsList = []
        self.availableOvalsList = []
        # WIN CONDITIONS
        self.wonByEliminatingEnemy = False
        self.lostByEliminatingPlayer = False
        self.lostByEliminatingEnemy = False
        self.lostByDisablingPlayer = False
        self.lostByDisablingEnemy = False
        self.lostByDisablingEnemyCapital = False
        self.wonByEliminatingPlayer = False
        self.wonByEliminatingEnemy = False
        self.wonByDisablingPlayer = False
        self.wonByDisablingEnemy = False
        self.wonByDisablingEnemyCapital = False
        self.wonByEliminating0 = False
        self.wonByEliminating1 = False
        self.wonByEliminating2 = False
        self.wonByEliminating3 = False
        self.wonByEliminating4 = False
        self.wonByEliminating5 = False
        self.lostByEliminating0 = False
        self.lostByEliminating1 = False
        self.lostByEliminating2 = False
        self.lostByEliminating3 = False
        self.lostByEliminating4 = False
        self.lostByEliminating5 = False
        self.winByDisabling0 = False
        self.winByDisabling1 = False
        self.winByDisabling2 = False
        self.winByDisabling3 = False
        self.winByDisabling4 = False
        self.winByDisabling5 = False
        self.wonByDisabling0 = False
        self.wonByDisabling1 = False
        self.wonByDisabling2 = False
        self.wonByDisabling3 = False
        self.wonByDisabling4 = False
        self.wonByDisabling5 = False
        self.looseByDisabling0 = False
        self.looseByDisabling1 = False
        self.looseByDisabling2 = False
        self.looseByDisabling3 = False
        self.looseByDisabling4 = False
        self.looseByDisabling5 = False
        self.lostByDisabling0 = False
        self.lostByDisabling1 = False
        self.lostByDisabling2 = False
        self.lostByDisabling3 = False
        self.lostByDisabling4 = False
        self.lostByDisabling5 = False
        self.winBySeeingLandmarks = False
        self.wonBySeeingLandmarks = False
        self.winByDomination = False
        self.wonByDomination = False
        self.looseByDomination = False
        self.lostByDomination = False
        # DEFAULT WIN CONDITIONS
        self.winByDisablingEnemyCapital = False
        self.looseByDisablingEnemyCapital = False
        # ZOOM
        self.mouseX = 0
        self.mouseY = 0
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        self.yellowX = 0
        self.yellowY = 0
        self.zoomChange = 0
        cwd = Path(sys.argv[0])
        cwd = str(cwd.parent)
        self.image = PIL.Image.open(os.path.join(cwd, config.get("Images", "image")))
        self.imageMask = PIL.Image.open(os.path.join(cwd, config.get("Images", "imageMask")))
        # Path finding data
        self.PFprecision = 30
        #debugging
        self.debugging = True
        pass


class ui_metrics():
    rootX = 1870
    rootY = 1000
    canvasWidth = 1120
    canvasHeight = 640
    shipImageFrameHeight = 60
    shipDataWidth = canvasWidth/12
    shipDataHeight = 40
    shipDataOffsetY = 20
    shipDataOffsetBetween = 60
    leftMargin = 10
    systemScalesWidth = 200
    systemScalesMarginTop = 60
    systemScalesOffset = 100
    systemScalesWidthOffset = 350
    systemScalesLFHeight = 300
    systemProgressbarsHeightOffset = 60
    systemsLFWidth = 400
    systemScalesLFWidth = systemsLFWidth
    systemScaleWidth = 160
    pausedLWidth = 100
    pausedLHeight = 100
    canvasX = 440
    canvasY = 10
    systemsLFHeight = canvasY + canvasHeight + 10
    shipDataX = canvasX
    shipDataY = canvasY + 20
    orderLength = 3
    objectivesLFX = 20
    objectivesLFY = canvasY + canvasHeight + 20 + 1/2 *systemScalesLFHeight
    objectivesLFWidth = systemsLFWidth*2/3
    objectivesLFHeight = 1/2 * systemScalesLFHeight
    exitBX = canvasX + canvasWidth - 20
    exitBY = canvasY + canvasHeight + 220
    startTurnBX = exitBX + 160
    startTurnBY = exitBY 
    timeElapsedPBX = canvasX + canvasWidth - 130
    timeElapsedPBY = canvasY + canvasHeight + 240
    timeElapsedLX = timeElapsedPBX
    timeElapsedLY = timeElapsedPBY - 30
    gameSpeedLX = timeElapsedPBX
    gameSpeedLY = timeElapsedPBY + 30
    gameSpeedSCX = timeElapsedPBX
    gameSpeedSCY = timeElapsedPBY + 60
    #editor
    editorSystemsFrameX = 100
    editorSystemsFrameY = 500
    editorSystemsX = 10
    editorSystemsY = 20
    editorSystemsYOffset = 50
    editorSystemsLOffsetX = 150
    editorSubsystemsXOffset = 400
    editorSystemsWidth = 350
    editorSaveButtonX = 1000
    editorSaveButtonY = 700
    editorChoiceMenuLFWidth = editorSystemsWidth
    editorChoiceMenuLFHeight = 80
    editorChoiceMenuOffset = 80
    editorChoiceMenuY = 150
    shipStatsLFHeight = 430
    shipStatsLFWidth = 350
    #custom game
    cgShipLF = 150
    cgRedShipX = rootX-300-cgShipLF
    cgBlueShipX = 300+cgShipLF
    cgBlueShipY = 600
    cgMapLFWidth = 300
    cgShipYoffset = 100
    cgStartButton = cgBlueShipY + cgShipYoffset *2
    cgCanvasWidth = 800
    cgCanvasHeight = 500
    cgCanvasX = rootX/2 - cgCanvasWidth/2
    cgMapChoiceY = cgCanvasHeight + 30
    cgMapChoiceX = rootX/2 - cgMapLFWidth/2
    #ms
    msCanvasWidth = 800
    msCanvasHeight = 500
    msCanvasX = 440
    msCanvasY = 100
    

class game_rules():
    movementPenalityHard = 0.9
    movementPenalityMedium = 0.7

class dynamic_object():
    x=10

class landmark():
    def __init__(self, xPos=100, yPos=100, cooldown=800, defaultCooldown=800, radius=100, boost='none',visible = True,id = 999):
        self.xPos = xPos
        self.yPos = yPos
        self.cooldown = cooldown
        self.defaultCooldown = defaultCooldown
        self.radius = radius
        self.boost = boost
        self.visible = visible
        self.id = id
        self.owner = 'none'
        self.wasContested = False

class ghost_point():
    def __init__(self, xPos=300, yPos=300,number = 0): 
        self.xPos = xPos
        self.yPos = yPos
        self.number = number
        
def declareGlobals():
    global combatUiReady
    global missionSelectUiReady
    global editorUiReady
    global cgGameUiReady
    global combatSystemInfo
    global cgGameInfo
    global editorInfo
    global shipEditorInfo
    global mainInfo
    global gameMenuInfo
    global uiMetrics
    global allSystemsList
    global allSubsystemsList
    global allEnginesList
    global allRadarsList
    global allThrustersList
    global allGeneratorsList
    global systemStats 
    global engineStats 
    global thrustersStats
    global radarStats
    global generatorStats
    global subsystemStats
    global systemStatsBlueprints
    global subsystemStatsBlueprints
    global engineStatsBlueprints
    global thrustersStatsBlueprints
    global radarStatsBlueprints
    global generatorStatsBlueprints
    global systemLookup
    global mapOptions
    global campaignOptions
    global ovalNumber
    global loadingCombat
    combatSystemInfo = dynamic_object()
    shipEditorInfo = dynamic_object()
    editorInfo = dynamic_object()
    mainInfo = dynamic_object()
    gameMenuInfo = dynamic_object()
    uiMetrics = ui_metrics()
    systemStats = dynamic_object()
    systemStatsBlueprints = dynamic_object()
    engineStats = dynamic_object()
    thrustersStats = dynamic_object()
    radarStats = dynamic_object()
    generatorStats = dynamic_object()
    subsystemStats = dynamic_object()
    engineStatsBlueprints = dynamic_object()
    subsystemStatsBlueprints = dynamic_object()
    thrustersStatsBlueprints = dynamic_object()
    radarStatsBlueprints = dynamic_object()
    generatorStatsBlueprints = dynamic_object()
    systemLookup = dynamic_object()
    cgGameInfo = dynamic_object()
    campaignOptions = dynamic_object()
    allSystemsList = []
    allSubsystemsList = []
    allEnginesList = []
    allRadarsList = []
    allThrustersList = []
    allGeneratorsList = []
    mapOptions = []
    combatUiReady = False
    editorUiReady = False
    missionSelectUiReady = False
    cgGameUiReady = False
    ovalNumber = 0
    loadingCombat = False