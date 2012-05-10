#!/usr/bin/env jython

from java.awt import Robot
from java.awt.event import InputEvent
from java.awt import MouseInfo
from java.awt import Toolkit
from java.awt import Dimension
import sys
import socket
import SocketServer
import SimpleHTTPServer


# TODO: trajectory stabilization


DEFAULT_PORT = 8000

MOUSE_MOVE_SPEED = 1.5


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        #print self.path
        if self.path == '/b1':
            rbt.mousePress(InputEvent.BUTTON1_MASK)
            rbt.mouseRelease(InputEvent.BUTTON1_MASK)
        elif self.path == '/b2':
            rbt.mousePress(InputEvent.BUTTON2_MASK)
            rbt.mouseRelease(InputEvent.BUTTON2_MASK)
        elif self.path == '/b3':
            rbt.mousePress(InputEvent.BUTTON3_MASK)
            rbt.mouseRelease(InputEvent.BUTTON3_MASK)
        elif self.path.startswith('/mv?'):
            x, y = self.path[4:].split('&')

            p = MouseInfo.getPointerInfo().getLocation()
            mouse_x = int(p.getX() + int(x) * MOUSE_MOVE_SPEED)
            mouse_y = int(p.getY() + int(y) * MOUSE_MOVE_SPEED)
            mouse_x = max(min(mouse_x, W), 0)
            mouse_y = max(min(mouse_y, H), 0)

            rbt.mouseMove(mouse_x, mouse_y)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def get_ip():
    if not sys.platform.startswith('linux'):
        ip = socket.gethostbyname(socket.gethostname())
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))   # Google's public DNS server
        ip = s.getsockname()[0]
        s.close()

    return ip


d = Dimension(Toolkit.getDefaultToolkit().getScreenSize())
W = int(d.getWidth()) - 1
H = int(d.getHeight()) - 1

rbt = Robot()
PORT = int(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_PORT
httpd = SocketServer.ThreadingTCPServer(('', PORT), MyHandler)
print '%s:%d' % (get_ip(), PORT)
httpd.serve_forever()

