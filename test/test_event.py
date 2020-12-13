import sys
from PyQt5.QtCore import (QEvent,QTimer,Qt)
from PyQt5.QtWidgets import (QApplication,QMenu,QWidget)
from PyQt5.QtGui import QPainter


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.justDoubleClicked = False
        self.key = ""
        self.text = ""
        self.message = ""
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("Events")
        QTimer.singleShot(0, self.giveHelp)

    def giveHelp(self):
        self.text = "请点击这里触发鼠标追踪功能"
        self.update()  # 重绘事件，也就是触发paintEvent函数


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())