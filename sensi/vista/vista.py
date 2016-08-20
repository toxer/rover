import threading
import picamera


class Vista():
    def __init__(self,inidirizzoTrasmissione,portaTrasmissione,handler):
        #Setto il sistema di trasmissione
        self.address = inidirizzoTrasmissione
        self.port=portaTrasmissione
        self.handler=handler
    
    def startTrasmission(self):
        if self.gstreamer != None:
            println("Trasmissione in corso")
            return
        if self.address==None or self.port==None:
            println("Parametri di connessione non settati")
            return
        
        self.gstreamer = subprocess.Popen([
        'gst-launch-1.0', '-v',
        'fdsrc',
        '!', 'h264parse',
        '!', 'rtph264pay', 'config-interval=10', 'pt=96',
        '!', 'udpsink', 'host='+self.address, 'port='+self.port	
        ], stdin=subprocess.PIPE)
        print ("Trasmissione partita")

    def startCamera(self,width,height):
        if width==None:
            self.width = 1280
        else:
            self.width=width
        if height==None:
                self.height = 1280
        else:
            self.height=height
        
        if self.camera==None:
            self.camera = picamera.PiCamera(resolution=(self.width, self.height), framerate=25)
            self.camera.hflip = True
        if self.gstreamer == None:
            print("Trasmissioe non ancora partita")
            return
        self.camera.start_recording(self.gstreamer.stdin, format='h264', bitrate=2000000)

        

        

        
            
        
        
        

