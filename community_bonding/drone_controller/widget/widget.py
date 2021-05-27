#!/usr/bin/python

from PyQt5 import QtWidgets
from PyQt5 import QtCore
import threading
import sys

from joystick import Joystick
from roverHandler import RoverHandler


class Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.min_z = 2.5
        self.speed = 2.0
        self.initUI()
        self.drone = RoverHandler()
        self.drone.enable_topics_for_read()

    def do_takeoff(self):
        z = max(self.sld.value()/20, self.min_z)
        self.thread_takeoff = threading.Thread(target=self.drone.takeoff, args=[z, ])
        self.thread_takeoff.start()

    def do_land(self):
        self.drone.land()

    def updateJoystick(self):
        while True:
            distance = self.joystick.joystickDirection()
            if distance != 0:
                vx = distance if distance > -1.1 and distance < 1.1 else 0.0
                vy = distance + 1.0 if distance > -2.1 and distance < -1.1 else 0.0
                vy = distance - 1.0 if distance > 1.1 and distance < 2.1 else vy
                z = max(self.sld.value()/20, self.min_z)
                self.drone.set_vel(self.speed*vx, self.speed*vy, z)

    def updateLabel(self, value):
        self.label.setText(str(value/20))

    def initUI(self):
        grid = QtWidgets.QGridLayout()

        self.joystick = Joystick()
        self.thread_updateJoystick = threading.Thread(target=self.updateJoystick)
        self.thread_updateJoystick.start()

        self.sld = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.sld.valueChanged.connect(self.updateLabel)

        self.label = QtWidgets.QLabel('0', self)
        self.label.setFixedSize(40, 15)

        self.btn_takeoff = QtWidgets.QPushButton(self)
        self.btn_takeoff.setText("Takeoff")
        self.btn_takeoff.clicked.connect(self.do_takeoff)

        self.btn_land = QtWidgets.QPushButton(self)
        self.btn_land.setText("Land")
        self.btn_land.clicked.connect(self.do_land)

        grid.addWidget(self.joystick, 0, 0)
        grid.addWidget(self.sld, 0, 1)
        grid.addWidget(self.label, 0, 2)
        grid.addWidget(self.btn_takeoff, 1, 0)
        grid.addWidget(self.btn_land, 2, 0)

        self.setLayout(grid)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Drone-Controller')
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    sys.exit(app.exec_())
