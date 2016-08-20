import threading
import picamera


class vista():
    def __init__(self,inidirizzoTrasmissione,portaTrasmissione,handler):
        #Setto il sistema di trasmissione
        self.address = inidirizzoTrasmissione
        self.port=portaTrasmissione
        self.handler=handler
    
    def startTrasmission(self):
        if self.gstreamer != None:
            println("Trasmissione in corso")
            return
        if self.address==None || self.port==None:
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

    def startCamera(self):
        if self.camera==None:
            self.camera = picamera.PiCamera(resolution=(1280, 720), framerate=25)
            self.camera.hflip = True

        
            
        
        
        

