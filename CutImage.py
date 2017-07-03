from PIL import Image, ImageDraw, ImageFont
import argparse
import sys

class Board:
    cut = 0
    rip = 0

    def __init__ (self,cut=0,rip=0):
        self.cut = cut
        self.rip = rip


class CutImage():
    image = Image

    def ParseSizes(self,psizes):
        sizestring = psizes
        return psizes.split(",")

    def __init__(self,sizes=[]):
        self.sizes = sizes
        self.process()

    def getfraction(self,dec):
        if dec == "0625":
            return "1/16"
        if dec == "125":
            return "1/8"
        if dec == "25":
            return "1/4"
        if dec == "5":
            return "1/2"
        if dec == "75":
            return "3/4"

    def getfont(self,fSize):
        return ImageFont.truetype("%WINDIR%\Fonts\consola.ttf", fSize)

    def process(self):
        boards= self.sizes.split(",")
        inCount = len(boards)
        scale = 5
        lWidth = 1
        width = 96*scale
        height = 48*scale
        white = (255, 255, 255)
        bg = (128,255,255)
        lColor = (0, 0, 0)
        image1 = Image.new("RGB", (width, height), white)
        draw = ImageDraw.Draw(image1)
        fontColor = (0,0,0,0)
        maxFontSize = 50
        fnt = ImageFont.truetype("%WINDIR%\Fonts\consola.ttf", maxFontSize)
        margin = 10

        topLeft = (0,0)
        botLeft = (0,image1.size[1]-1)
        botRight = (image1.size[0]-1,image1.size[1]-1)
        topRight = (image1.size[0]-1,0)

        draw.line([topLeft,topRight], fill=lColor  ,width=lWidth )
        draw.line([topRight,botRight], fill=lColor  ,width=lWidth )
        draw.line([botRight,botLeft], fill=lColor ,width=lWidth )
        draw.line([botLeft,topLeft], fill=lColor  ,width=lWidth )
        xCount = 0
        lastrip = 0

        for i in range(0,inCount):
            inputStr = boards[i]
            split = inputStr.split("x")
            fraction1 = split[0].split(".")
            fraction2 = split[1].split(".")
            hasFrac = False
            firstLengthText = str(fraction1[0])
            secondLengthText = str(fraction2[0])

            if len(fraction1) > 1:
                hasFrac = True
                fracText = self.getfraction(fraction1[1])
                firstLengthText += " " + str(fracText)

            if len(fraction2) > 1:
                hasFrac = True
                fracText = self.getfraction(fraction2[1])
                secondLengthText += " " + str(fracText)

            text = firstLengthText + "\"" + "x" + secondLengthText + "\""

            print split
            print inputStr
            board = Board(float(split[0]),float(split[1]))
            print "rip " , board.rip
            print "cut " , board.cut
            x = (xCount + board.cut) * scale
            y = board.rip * scale
            leftRip = xCount *scale
            print "x: ",x, "y: ",y
            print topRight
            print botLeft
            print "xCount: ", xCount
            lastrip = [(x,y),(image1.size[0],y)]
            leftText= (xCount + board.cut/2) * scale
            farLeft = xCount *scale

            draw.line([(farLeft,0),(farLeft,y)], fill=lColor,width=lWidth ) #leftcutline
            draw.line([(x,0),(x,y)], fill=lColor,width=lWidth ) #cutline
            draw.line([(leftRip,y),(x,y)], fill=lColor,width=lWidth ) #ripline

            print "leftText: ",leftText
            fontSizeFits = False
            curFontSize = maxFontSize
            f =fnt
            w,h = 0,0
            while fontSizeFits == False:
                f = self.getfont(curFontSize)
                w,h = draw.textsize(text ,font=f)
                if(w + 2* margin < x-farLeft):
                    fontSizeFits = True
                curFontSize -= 1

            draw.text((leftText-w/2,y/2-h/2), text, font=f, fill=fontColor)
            xCount += board.cut

        draw.line(lastrip, fill=lColor, width=lWidth)
        self.image=image1

