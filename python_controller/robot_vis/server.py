__author__ = 'michal'

from PyQt4 import QtGui

import sys
sys.path.append("..")

import cPickle
import sys
import robot_model

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtNetwork import QUdpSocket, QHostAddress

class RobotVisServer(QUdpSocket):

    HOST = QHostAddress.Any
    PORT = 9010

    def __init__(self):
        super(RobotVisServer, self).__init__()

        self._windows_dict = {}

        self.bind(self.HOST, self.PORT)
        self.readyRead.connect(self.read_data)

    def read_data(self):
        while self.hasPendingDatagrams():
            size = self.pendingDatagramSize()
            (str_data, host, port) = self.readDatagram(size)

            vis_state = cPickle.loads(str_data)
            self.handle_vis_state(vis_state)

    def handle_vis_state(self, vis_state):
        robot_name = vis_state.get_robot_name()

        if robot_name in self._windows_dict:
            pass


def main():
    app = QtGui.QApplication(sys.argv)

    robot = RobotVisServer()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()