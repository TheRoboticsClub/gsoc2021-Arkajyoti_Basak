#!/usr/bin/python

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from enum import Enum

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QWidget):
    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.maxDistance = 85

    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(-self.maxDistance, -self.maxDistance, self.maxDistance * 2, self.maxDistance * 2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-15, -15, 30, 30).translated(self.movingOffset)
        return QRectF(-15, -15, 30, 30).translated(self._center())

    def _center(self):
        return QPointF(self.width()/2, self.height()/2)

    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        if (limitLine.length() > self.maxDistance):
            limitLine.setLength(self.maxDistance)
        return limitLine.p2()

    def joystickDirection(self):
        if not self.grabCenter:
            return 0.0
        normVector = QLineF(self._center(), self.movingOffset)
        currentDistance = normVector.length()
        angle = normVector.angle()

        # -2  <---------->  -1  <---------->  0  <---------->  1  <---------->  2
        #     <-backward->      <---left--->     <--right--->     <-forward-->
        # if distance is -2 to -1 move backward and so on

        distance = currentDistance / self.maxDistance
        if 45 < angle < 135:
            sendDistance = distance+1.0
        elif 135 < angle < 225:
            sendDistance = -distance
        elif 225 < angle < 315:
            sendDistance = -(distance+1.0)
        else:
            sendDistance = distance
        return sendDistance

    def mousePressEvent(self, ev):
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.movingOffset = QPointF(0, 0)
        self.update()

    def mouseMoveEvent(self, event):
        if self.grabCenter:
            self.movingOffset = self._boundJoystick(event.pos())
            self.update()