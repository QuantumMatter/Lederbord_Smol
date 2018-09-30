from rgbViews import *
import json


class DYIndicator:

    def __init__(self, rootView, x, y):
        self.__rootView__ = rootView
        self.__x__ = x
        self.__y__ = y
        self.rootDir = '/home/pi/scoreboard/scoreboard/ViewHierarchy/'

        # Downs Text Image
        self.downsImage = RGBImage(rootView, self.__x__, self.__y__ + 1, self.rootDir + '../res/down.png')
        self.downsLabel = RGBLabel(rootView, self.__x__ + 10, self.__y__, '0')
        # Yards Text Image
        self.yardsImage = RGBImage(rootView, self.__x__ + 19, self.__y__ + 1, self.rootDir + '../res/yards.png')
        self.yardsLabel = RGBLabel(rootView, self.__x__ + 29, self.__y__, '0')



class FootballBoard:

    def __init__(self, rootView):
        self.__rootView__ = rootView

        # Views
        self.awayLabel = RGBLabel(self.__rootView__, 0, 0, "GUEST")
        self.awayScore = RGBLabel(self.__rootView__, 0, 12, "00", TextStyle.IMAGE)
        self.homeLabel = RGBLabel(self.__rootView__, 63, 0, "HOME")
        self.homeScore = RGBLabel(self.__rootView__, 60, 12, "00", TextStyle.IMAGE)
        self.awayLabel.setColor(graphics.Color(0, 255, 255))
        self.homeLabel.setColor(graphics.Color(0, 255, 255))
        self.bsoIndicator = DYIndicator(self.__rootView__, 0, 38)
        self.periodIndicator = PeriodIndicator(self.__rootView__, 43, 0, 'P')
        self.clockIndicator = Clock(self.__rootView__, 65, 38)

    def setHomeScore(self, dataStr):
        # TODO make app send correct data instead of fixing here
        if len(dataStr) == 1:
            self.homeScore.setText("0" + dataStr)
        else:
            self.homeScore.setText(dataStr)

    def setHomeColor(self, dataStr):
        colorObject = json.loads(dataStr)
        red = int(colorObject["R"])
        green = int(colorObject["G"])
        blue = int(colorObject["B"])
        self.homeLabel.setColor(graphics.Color(red, green, blue))

    def setAwayScore(self, dataStr):
        # TODO make app send correct data instead of fixing here
        if len(dataStr) == 1:
            self.awayScore.setText("0" + dataStr)
        else:
            self.awayScore.setText(dataStr)

    def setAwayColor(self, dataStr):
        colorObject = json.loads(dataStr)
        red = int(colorObject["R"])
        green = int(colorObject["G"])
        blue = int(colorObject["B"])
        self.awayLabel.setColor(graphics.Color(red, green, blue))

    def setClock(self, dataStr):
        self.clockIndicator.setTime(dataStr)

    def setQuarter(self, dataStr):
        self.periodIndicator.setPeriod(dataStr)

    def setYards(self, dataStr):
        self.bsoIndicator.yardsLabel.setText(dataStr)

    def setDown(self, dataStr):
        self.bsoIndicator.downsLabel.setText(dataStr)


if __name__ == "__main__":
    rootView = RGBBase()
    board = FootballBoard(rootView)
    while True:
        pass