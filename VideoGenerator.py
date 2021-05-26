import cv2
import numpy as np
import time


class VideoGenerator():
    cam = None
    frame = None
    operation = 'n'
    haltOp = False
    fpsOp = False
    colorOp = False

    def __init__(self):
        # Chose camera option
        self.cam = cv2.VideoCapture(1)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        

    def run(self):
        while True:
            # Read each self.frame from VideoCapture
            ret, self.frame = self.cam.read()
            self.frameRunner()
            if(not self.haltOp):
                cv2.imshow('window', self.frame)
            inp = cv2.waitKey(1)
            
            if(not inp == -1):
                self.operation = inp
            else:
                self.operation = ''

        # When everything done, release the capture
        self.cam.release()
        cv2.destroyAllWindows()

    def frameRunner(self):
        self.frameController()
        if(self.colorOp):
            self.frame = self.changeColor(self.frame)
        if(self.fpsOp):
            self.frame = self.changeFrameRate(self.frame, 0.5)
        if(self.haltOp):
            self.frame = self.haltFrameRate(self.frame)
        return self.frame

    def frameController(self):
        if(self.operation == ord('n')):
            self.colorOp = False
            self.fpsOp = False
            self.haltOp = False
        elif(self.operation == ord('c')):
            self.colorOp = not self.colorOp
        elif(self.operation == ord('f')):
            self.fpsOp = not self.fpsOp
        elif(self.operation == ord('h')):
            self.haltOp = not self.haltOp

    def changeColor(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        frame = cv2.inRange(hsv, lower_blue, upper_blue)
        return frame

    def changeFrameRate(self, frame, fr):
        # Since self.cam.set(cv2.CAP_PROP_FPS) is not working, using time.sleep
        time.sleep(fr)
        return frame

    def haltFrameRate(self, frame):
        return frame
    
    def getFrame(self):
        return self.self.frame

if __name__ == '__main__':
    VideoGenerator().run()
