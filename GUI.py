from VideoGenerator import VideoGenerator
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
Window.size = (320, 420)
class GUIWidget(Widget):
    vgr = None
    cam = None
    fps = 120
    def __init__(self,**kwargs):
        super(GUIWidget,self).__init__(**kwargs)
     
    def start(self):
        self.vgr = VideoGenerator()
        self.build()
    
    def exit(self):
        self.vgr.end()
        Clock.unschedule(self.run)

    def build(self):
        Clock.unschedule(self.run)
        
        Clock.schedule_interval(self.run,1/self.vgr.currentFPS)

    def run(self,dt):
        
        self.vgr.update()

    def changeColor(self):
        self.vgr.frameController(0)
    def halt(self):
        self.vgr.frameController(1)
    
    def changeFPS(self,*args):
        self.fps = 61 - args[1]
        if(self.fps!=self.vgr.currentFPS):
            Clock.unschedule(self.run)
            self.vgr.currentFPS = self.fps 
            Clock.schedule_interval(self.run,1/self.vgr.currentFPS)
      

    
        
        

class GUIApp(App):
    vgr = None
    def __init__(self,**kwargs):
        super(GUIApp,self).__init__(**kwargs)
        self.title = 'GUI window'
    

if  __name__=='__main__':
    GUIApp().run()
    
