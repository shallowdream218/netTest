import sys
import cgitb

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from scene import GraphicScene
from view import GraphicView

cgitb.enable(format("text"))


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.scene = GraphicScene(self)
        self.view = GraphicView(self.scene, self)
        self.view.setGeometry(100, 100, 820, 520)
        self.scene.setSceneRect(100, 100, 800, 500)
        # self.scene.setBackgroundBrush(Qt.gray)
        # self.view.setBackgroundBrush(Qt.red)

        # 设置view可以进行鼠标的拖拽选择
        # self.view.setDragMode(self.view.RubberBandDrag)

        self.setMinimumHeight(800)
        self.setMinimumWidth(1500)
        self.setCentralWidget(self.view)
        self.setWindowTitle("Demo")


def demo_run():
    app = QApplication(sys.argv)
    demo = MainWindow()
    # compatible with Mac Retina screen.
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    # show up
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    demo_run()
