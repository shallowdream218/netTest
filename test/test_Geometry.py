import sys
from PyQt5.QtWidgets import QApplication,QWidget


app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
window.move(550,150)
#setGeometry(300,300,150,200) 前两个参数是窗口在屏幕上的x和y坐标，后两个是窗口本身的宽度和高度
window.show()
sys.exit(app.exec_())