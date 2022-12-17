import sys
from UI import Ui_Form
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import random


class MainFunc(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.is_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.is_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()
            self.is_paint = False

    def draw_ellipse(self, qp):
        for i in range(random.randint(1, 10)):
            qp.setBrush(QColor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))
            paint_size = random.randint(10, 100)
            paint_coords = (random.randint((paint_size // 2) + 10, 300), random.randint((paint_size // 2) + 10, 300))
            ellipse_paint = (paint_coords[0] - (paint_size // 2), paint_coords[1] - (paint_size // 2))
            qp.drawEllipse(ellipse_paint[0], ellipse_paint[1], paint_size, paint_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainFunc()
    ex.show()
    sys.exit(app.exec_())