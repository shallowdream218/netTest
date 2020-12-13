import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QLabel, QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # 有view就要有scene
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        # 设置view可以进行鼠标的拖拽选择
        self.view.setDragMode(self.view.RubberBandDrag)
        self.setMinimumHeight(500)
        self.setMinimumWidth(500)

        self.setCentralWidget(self.view)

        self.setWindowTitle("Graphics Demo")

        self.init_ui()


    def init_ui(self):

            item1 = host()
            item1.setPos(0,0)
            self.scene.addItem(item1)

            item2 = switch()
            item2.setPos(0,0)
            self.scene.addItem(item2)


    # 设置第一个图元


class host(QGraphicsPixmapItem):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.pix = QPixmap("host.png")
        self.width = 150  # 图元宽
        self.height = 150  # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)  # ***设置图元是可以被移动的

        # 设置第二个图元


class switch(QGraphicsPixmapItem):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.pix = QPixmap("switch.png")
        self.width = 50  # 图元宽
        self.height = 50  # 图元高
        self.setPixmap(self.pix)  # 设置图元
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # ***设置图元是可以被选择的
        self.setFlag(QGraphicsItem.ItemIsMovable)  # ***设置图元是可以被移动的


def demo_run():
    app = QApplication(sys.argv)
    demo = MainWindow()
    # 适配 Retina 显示屏（选写）.

    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    demo_run()