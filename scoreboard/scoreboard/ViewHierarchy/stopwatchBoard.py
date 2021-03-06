from rgbViews import *
import json

class splitView:
    def __init__(self, rootView, x, y):
        self.__rootView__ = rootView
        self.__x__ = x
        self.__y__ = y
        self.splits = 0
        self.zeroString = "00:00"
        self.dataStr1 = ""
        self.dataStr2 = ""
        self.dataStr3 = ""


    def split(self, dataStr):
        self.dataStr3 = self.dataStr2
        self.dataStr2 = self.dataStr1
        self.dataStr1 = dataStr

        self.splits+=1

        if self.splits == 1:
            self.__split1__ = Clock(self.__rootView__, self.__x__, self.__y__)
        if self.splits == 2:
            self.__split2__ = Clock(self.__rootView__, self.__x__ + 32, self.__y__)
        if self.splits == 3:
            self.__split3__ = Clock(self.__rootView__, self.__x__ + 64, self.__y__)

        self.__split1__.setTime(self.dataStr1)
        self.__split2__.setTime(self.dataStr2)
        self.__split3__.setTime(self.dataStr3)


class StopwatchBoard:
    # TODO implement color scheme (splits are darker as they go down to help readability)

    def __init__(self, rootView):
        self.__rootView__ = rootView
        self.seconds = 0
        self.running = False

        self.splitView = splitView(self.__rootView__, 1, 38)
        self.mainClock = Clock(self.__rootView__, 33, 10) # TODO make big clock
        self.mainClock.minLabel.setFont("../../fonts/vcr_28.bdf")
        self.mainClock.minLabel.setOrigin(0, 21)
        self.mainClock.minLabel.setColor(graphics.Color(0, 238, 255))
        self.mainClock.secLabel.setFont("../../fonts/vcr_28.bdf")
        self.mainClock.secLabel.setOrigin(50, 21)
        self.mainClock.secLabel.setColor(graphics.Color(0, 238, 255))
        self.mainClock.colon = RGBLabel(self.mainClock.__rootView__, 38, 21, ":")
        self.mainClock.colon.setFont("../../fonts/vcr_28.bdf")
        self.mainClock.colon.setColor(graphics.Color(0, 238, 255))
        self.mainClock.__rootView__.__children__.remove(self.mainClock.seperatorImage)
        self.mainClock.__rootView__.redraw()

        self.startTime = None
        self.format = "%M:%S"

    def setClock(self, dataStr):
        self.mainClock.setTime(dataStr)

    def split(self, dataStr):
        self.splitView.split(dataStr)

    def timeStr(self, format):
        elapsed =(datetime.now() - self.startTime).total_seconds()
        return time.strftime(format, time.gmtime(self.seconds + elapsed))

    def startTimer(self, dataStr):
        self.running = True
        while self.running:
            self.setClock(self.timeStr(self.format))
            # self.seconds += 1
            time.sleep(0.1)

    def stopTimer(self, dataStr):
        self.running = False

    def setSeconds(self, dataStr):
        self.seconds = int(dataStr)
        self.startTime = datetime.now()
        self.setClock(self.timeStr(self.format))

    def splitTimer(self, dataStr):
        self.splitView.split(self.timeStr(self.format))
