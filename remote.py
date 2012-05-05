#!/usr/bin/env jython

from java.awt import Robot
from java.awt.event import KeyEvent
import sys
import socket
import SocketServer
import SimpleHTTPServer

DEFAULT_PORT = 8000

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


rbt = Robot()
PORT = int(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_PORT
httpd = SocketServer.ThreadingTCPServer(('', PORT), MyHandler)
print '%s:%d' % (socket.gethostbyname(socket.gethostname()), PORT)
httpd.serve_forever()
