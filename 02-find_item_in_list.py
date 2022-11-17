# checks ports for ftp, ssh, telnet, and http services in the localhost interface
import socket
ip = '127.0.0.1'

portlist = [21, 22, 23, 80]
for port in portlist:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    print(port, ":", result)
    sock.close()

# output when port 80 is close
# 21 : 111
# 22 : 111
# 23 : 111
# 80 : 111

# output when port 80 is open
# 21 : 111
# 22 : 111
# 23 : 111
# 80 : 0
