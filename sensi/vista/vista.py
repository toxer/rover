import picamera
import subprocess
import threading


class Vista(threading.Thread):
   
    def __init__(self,inidirizzoTrasmissione,portaTrasmissione,handler):
        threading.Thread.__init__(self)
        #Setto il sistema di trasmissione
        self.address = inidirizzoTrasmissione
        self.port=portaTrasmissione
        self.handler=handler
       
       
    
    def startTrasmission(self):
        if hasattr(self,'gstreamer'):
            print("Trasmissione in corso")
            return
        if self.address==None or self.port==None:
            println("Parametri di connessione non settati")
            return

        print("host "+self.address) 
        
        self.gstreamer = subprocess.Popen([
        'gst-launch-1.0', '-v',
        'fdsrc',
        '!', 'h264parse',
        '!', 'rtph264pay', 'config-interval=10', 'pt=96',
        '!', 'udpsink', 'host='+self.address, 'port='+self.port
    ], stdin=subprocess.PIPE)


    def setCamera(self,width,height):
        self.trasmissionOn=True
        if width==None:
            self.width = 1280
        else:
            self.width=width
        if height==None:
                self.height = 720
        else:
            self.height=height
        
        if not hasattr (self,'camera'):
            self.camera = picamera.PiCamera(resolution=(self.width, self.height), framerate=25)
            self.camera.hflip = True
        if self.gstreamer == None:
            print("Trasmissione non ancora partita")
            return
        else:
            print("Stream agganciato")
    
    def run(self):
        self.startTrasmission();
        self.setCamera(None,None);
        self.trasmissionOn=True

        

        if hasattr(self,'camera') and hasattr(self,'gstreamer'):
            self.camera.start_recording(self.gstreamer.stdin, format='h264', bitrate=2000000)
            while self.trasmissionOn:
                pass

            
  
    
    def stop(self):
        self.trasmissionOn=False
        if hasattr(self,'gstreamer'):
            pass
        
        

      



        

        

        
            
        
        
        

