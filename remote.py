#!/usr/bin/env jython

from java.awt import Robot
from java.awt.event import KeyEvent
from java.lang import System
import sys
import socket
import SocketServer
import SimpleHTTPServer

DEFAULT_PORT = 8000

# http://docs.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print self.path
        if self.path == '/up':
            rbt.keyPress(KeyEvent.VK_PAGE_UP)
            rbt.keyRelease(KeyEvent.VK_PAGE_UP)
        elif self.path == '/down':
            rbt.keyPress(KeyEvent.VK_PAGE_DOWN)
            rbt.keyRelease(KeyEvent.VK_PAGE_DOWN)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def get_ip():
    if not System.getProperty('os.name').startswith('Linux'):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))   # Google's public DNS server
        ip = s.getsockname()[0]
        s.close()
    else:
        ip = socket.gethostbyname(socket.gethostname())

    return ip


rbt = Robot()

if len(sys.argv) == 2:
    PORT = int(sys.argv[1])
else:
    PORT = DEFAULT_PORT

httpd = SocketServer.ThreadingTCPServer(('', PORT), MyHandler)
print '%s:%d' % (get_ip(), PORT)
httpd.serve_forever()

