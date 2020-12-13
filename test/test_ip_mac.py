from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
import sys

class linEditDemo(QWidget):
    def __init__(self,parent=None):
        super(linEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit的输入掩码例子")

        flo = QFormLayout()
        ipEdit = QLineEdit()
        macEdit = QLineEdit()
        dateEdit = QLineEdit()
        liceEdit = QLineEdit()

        ipEdit.setInputMask("000.000.000.000;_")
        macEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        dateEdit.setInputMask("0000-00-00")
        liceEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        flo.addRow("数字掩码",ipEdit)
        flo.addRow("Mac掩码", macEdit)
        flo.addRow("日期掩码", dateEdit)
        flo.addRow("许可证掩码", liceEdit)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = linEditDemo()
    win.show()
    sys.exit(app.exec_())

