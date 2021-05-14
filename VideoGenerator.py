import cv2
import numpy as np
import time
class VideoGenerator():
    cam = None
    operation = 'n'
    def __init__(self):
        #Chose camera option
        self.cam = cv2.VideoCapture(1)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

    def run(self):
        while True:
            #Read each frame from VideoCapture
            ret, frame = self.cam.read()
            frame = self.frameRunner(frame)
            cv2.imshow('window',frame)

            #display a frame for 1 ms, after which display will be automatically closed.
            inp = cv2.waitKey(1)
            if(not inp==-1):
                self.operation = inp
        # When everything done, release the capture
        self.cam.release()
        cv2.destroyAllWindows()
        
    def frameRunner(self,frame):
        if(self.operation==ord('n')):
            return frame
        elif(self.operation==ord('t')):
            return self.addText(frame)
        elif(self.operation==ord('f')):
            return self.changeFrameRate(frame,0.5)
        elif(self.operation==ord('h')):
            return self.haltFrameRate(frame)
        else:
            return frame
            
    def addText(self,frame):
        cv2.putText(frame,'Hello!',(500,800),cv2.FONT_HERSHEY_SIMPLEX,10,(255, 255, 255))
        return frame
    
    def changeFrameRate(self,frame,fr):
        #Since self.cam.set(cv2.CAP_PROP_FPS) is not working, using time.sleep
        time.sleep(fr)
        return frame
    
    def haltFrameRate(self,frame):
        while(True):
            inp = cv2.waitKey(1)
            if(inp==ord('h')):
                self.operation = 'n'
                break
        return frame

if  __name__=='__main__':
    VideoGenerator().run()