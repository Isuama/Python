import socket
import sys
from datetime import datetime
import errno

def checkPortSocket(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                #print("get serv by port", socket.getservbyport(port))
                print("Port {}: \t Open".format(port))
            else:
                print("Port {}: \t Closed".format(port))
                print("Reason",errno.errorcode[result])
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Connection error")
        sys.exit()

portlist = []
def getPortList():

    # portlist = [21,22,80,8080,443]
    # return portlist

    for i in range(1, 65535):
        portlist.append(i)
    return portlist


time_init = datetime.now()
checkPortSocket('localhost', getPortList())
print("Port scanning completed in: ", (datetime.now()-time_init))
