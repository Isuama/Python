SocketType = class socket(builtins.object)

     |  socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object

     |  socket(family=-1, type=-1, proto=-1, fileno=None) -> socket object

     |  

     |  Open a socket of the given type.  The family argument specifies the address family; it defaults to AF_INET.  The type argument specifies whether this is a stream (SOCK_STREAM, this is the default)or datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,specifying the default protocol.  Keyword arguments are accepted.

     |  The socket is created as non-inheritable.

     |  When a fileno is passed in, family, type and proto are auto-detected,unless they are explicitly set.

     |  A socket object represents one endpoint of a network connection.

     |  Methods of socket objects (keyword arguments not allowed):

     |  _accept() -- accept connection, returning new socket fd and client address

     |  bind(addr) -- bind the socket to a local address