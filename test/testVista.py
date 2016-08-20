import sys  
sys.path.append("../sensi/vista")  
import vista
import time



#attivo la trasmissione
vista = vista.Vista("192.168.1.7","5000",None)
vista.start()

#vista.stop();
