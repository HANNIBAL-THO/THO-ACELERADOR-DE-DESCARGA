from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
import random

class Punto:
    def __init__(self, w, h):
        self.x = random.randint(40, w-40)
        self.y = random.randint(40, h-40)
        angle = random.uniform(0, 2*3.1416)
        speed = random.uniform(1.2, 2.5)
        self.dx = speed * random.choice([-1, 1]) * random.uniform(0.5, 1.0)
        self.dy = speed * random.choice([-1, 1]) * random.uniform(0.5, 1.0)
        self.radius = 4

    def move(self, w, h):
        self.x += self.dx
        self.y += self.dy
        if self.x < 32 or self.x > w-32:
            self.dx *= -1
        if self.y < 32 or self.y > h-32:
            self.dy *= -1

class FondoAnimadoWidget(QWidget):
    def __init__(self, parent=None, num_puntos=64):  
        super().__init__(parent)
        self.num_puntos = num_puntos
        self.puntos = []
        self.lime = QColor(140, 255, 0)
        self.bg = QColor(20, 20, 20)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animar)
        self.timer.start(40)
        self.init_puntos()

    def init_puntos(self):
        w, h = max(self.width(), 400), max(self.height(), 400)
        self.puntos = [Punto(w, h) for _ in range(self.num_puntos)]

    def resizeEvent(self, event):
        self.init_puntos()

    def animar(self):
        w, h = self.width(), self.height()
        for p in self.puntos:
            p.move(w, h)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), self.bg)
      
        for i, p1 in enumerate(self.puntos):
            for j, p2 in enumerate(self.puntos):
                if i < j:
                    dist = ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
                    if dist < 90:
                        alpha = int(120 * (1 - dist/90))
                        pen = QPen(QColor(self.lime.red(), self.lime.green(), self.lime.blue(), alpha), 1)
                        painter.setPen(pen)
                        painter.drawLine(int(p1.x), int(p1.y), int(p2.x), int(p2.y))
        
        for p in self.puntos:
            painter.setBrush(QBrush(self.lime))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(int(p.x)-p.radius, int(p.y)-p.radius, p.radius*2, p.radius*2)
        painter.end()
