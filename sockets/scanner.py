#program to scan ports...
import sys
import socket
from datetime import datetime
#Define our target 
if (len(sys.argv))==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax error.")
    print("Syntax : \"python scanner.py <ip or host name>\"")
#adding a banner. Banner is nothing but a code producing a good looking output indicating completion of a task 
print("-"*50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

#now we will try to estalish a connection between a port and the traget ip address
try: 
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)#its like all the connection attempts should last for one second only if not successful then move on 
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))#print(f"Port {port} available")
            s.close
        else:
            print("not able to connect {} to {}".format(target, port))
            s.close
except KeyboardInterrupt:
    print("Keyboard interrupt")
    sys.exit()
except socket.gaierror:
    print("Hostname not resolved.")
    sys.exit()
except socket.error:
    print("could not connect to the server...")
    sys.exit


