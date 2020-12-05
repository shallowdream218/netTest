from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap


class static_GraphicItem(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("host.png")
        self.width = 85
        self.height = 85
        self.setPixmap(self.pix)
        self.setFlag(QGraphicsItem.ItemIsSelectable)


