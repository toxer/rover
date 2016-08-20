import sys  
sys.path.append("../sensi/vista")  
import Vista


#attivo la trasmissione
vista = vista.Vista("192.168.1.3","5000",None)
vista.startTrasmission()
vista.startCamera()
