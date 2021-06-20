import cv2
import numpy as np
import time


class VideoGenerator():
    cam = None
    frame = None
    currentFPS = 60
    haltOp = False
    colorOp = False
    fpsOp = False
    def __init__(self):
        # Chose camera option
        self.cam = cv2.VideoCapture(1)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    def update(self):
        ret, self.frame = self.cam.read()
        self.frameRunner()
        if(not self.haltOp):
            cv2.imshow('window', self.frame)
    
    def end(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def frameRunner(self):
        if(self.colorOp):
            self.frame = self.changeColor()
    
    def frameController(self,op):
        if(op==0):
            self.colorOp = not self.colorOp
        elif(op==1):
            self.haltOp = not self.haltOp
    
    def changeColor(self):
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        frame = cv2.inRange(hsv, lower_blue, upper_blue)
        return frame

if __name__ == '__main__':
    VideoGenerator().update()
