# Shaun Bowman
# Mar 11 2022
# loggerClass.py
from ina260.controller import Controller
import csv

class Breakout:

    def __init(self, i2cChan=1, relaysOff=True):
        self.pSenseIna0x40 = Controller(address=0x40)
        self.pSenseIna0x41 = Controller(address=0x41)
        self.pSenseIna0x44 = Controller(address=0x44)
        self.relayBord0x22 = Controller(address=0x22)

        self.v0x40 = False
        self.v0x41 = False
        self.v0x44 = False
        self.i0x40 = False
        self.i0x41 = False
        self.i0x44 = False
        self.p0x40 = False
        self.p0x41 = False
        self.p0x44 = False

        self.recFileLocation = '/home/pi/git/RpiDatalogger/logs'
        self.recFileNameNoExt = 'LogTest'

        if relaysOff:
            # initialize relay states to off
            self.relayBord0x22.relayBankSet(bank='a', state=0)
            self.relayBord0x22.relayBankSet(bank='b', state=0)

    def __getTime(self):
        # gets current time & returns as simple string for data recording
        return

    def __incActnCnt(self):
        # increments basic action counter. The action counter increments for
        # each controller action: measurement, relay state change, ect.
        return

    def __commitRecord(self):
        # commits the overall record to the recording
        return

    def __measureElec(self):
        # execute measurements of recording
        return

    def setRelay(self, bank='a', relay=0, state=0):
        # sets a relay state & increments action counter / recording as
        # required.
        return

    def recordingCntrl(self, state=0):
        # starts / stops recording for given record
        return

    def recordingSetup(self, 
                       fileName='breakoutRec', 
                       fileDirAbs='/home/pi', 
                       addDatetime=False,
                       doContMode=False,
                       autoHz=10):
        # setup recording, w file name, specify if date/time should be appended
        # to the filename, specify if recordings should be scheduled to occur
        # automatically, and if so - at what rate in Hz
        self.recFileNameNoExt = fileName
        self.recFileLocation = fileDirAbs
        self.recAutoHz = autoHz
        self.recAddDateTime = addDatetime
        self.recDoContMode = doContMode
    
        return
