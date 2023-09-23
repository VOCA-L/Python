from threading import *
from socket import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class Signal(QObject):
    recv_signal = pyqtSignal(str)
    discon_signal = pyqtSignal()

class ClientSocket:
    def __init__(self, parent) -> None:
        self.parent = parent

        self.recv = Signal()
        self.recv.recv_signal.connect(self.parent.updateMsg)
        
        self.dis_con = Signal()
        self.dis_con.discon_signal.connect(self.parent.updateDisconnect)

        self.bConnect = False

    def __del__(self) -> None:
        self.stop()

    def connectServer(self, ip, port) -> bool:
        self.client = socket(AF_INET, SOCK_STREAM)

        try:
            self.client.connect((ip, port))
        except Exception as e:
            print("Connection Error: ", e)
            return False
        else:
            self.bConnect = True
            self.t = Thread(target=self.receive, args=(self.client,))
            self.t.start()

    def stop(self):
        self.bConnect = False
        if hasattr(self, 'client'):
            self.client.close()
            del(self.client)
            print("Client Stop")
            self.dis_con.discon_signal.emit()

    def receive(self, client):
        while self.bConnect:
            try:
                recv = client.recv(1024)
            except Exception as e:
                print("Receive Error: ", e)
                break
            else:
                msg = str(recv, encoding='utf-8')
                if msg:
                    self.recv.recv_signal.emit(msg)
                    print("[RECV] : ", msg)
        self.stop()
    
    def send(self, msg):
        if not self.bConnect:
            return
    
        try:
            self.client.send(msg.encode())
        except Exception as e:
            print("Send Error: ", e)
