from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap


class static_host(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("host.png")
        self.width = 20
        self.height = 20
        self.setPixmap(self.pix)



class static_switch(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("switch.png")
        self.width = 20
        self.height = 20
        self.setPixmap(self.pix)



class static_server(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("server.png")
        self.width = 20
        self.height = 20
        self.setPixmap(self.pix)



class static_router(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("router.png")
        self.width = 20
        self.height = 20
        self.setPixmap(self.pix)








