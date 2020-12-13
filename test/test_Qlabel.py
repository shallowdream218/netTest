from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.red)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>nqj</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("host.png"))
        label4.setText("<a href='www.baidu.com'>欢迎访问百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        # 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        # 3允许label1控件访问超链接
        label1.setOpenExternalLinks(True)
        # 打开允许访问超链接，默认是不允许，需要使用setOpenExternalLinks(True)允许浏览器访问超链接
        label4.setOpenExternalLinks(False)  # 如果是True的话，点击就会跳转到百度

        # 点击文本框绑定槽事件

        label4.linkActivated.connect( link_clicked )

        # 滑过文本框绑定槽事件

        label2.linkHovered.connect( link_hovered )
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel 例子")


def link_hovered(self):
    print("当鼠标滑过label-2标签时，触发事件。")

# IndentationError: unindent does not match any outer indentation level:缩进错误：未缩进与任何外部缩进级别都不匹配


def link_clicked(self):
    print("当鼠标点击label-4标签时，触发事件。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.resize(500,500)
    win.move(100,100)
    # win.setGeometry(500, 500, 100, 100)
    win.show()
    sys.exit(app.exec_())






