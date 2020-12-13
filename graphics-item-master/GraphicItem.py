from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap


class host(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("host.png")
        self.width = 50
        self.height = 50
        self.setPixmap(self.pix)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # update selected node and its edge
        if self.isSelected():
            for gr_edge in self.scene().edges:
                gr_edge.edge_wrap.update_positions()


class switch(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("switch.png")
        self.width = 50
        self.height = 50
        self.setPixmap(self.pix)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # update selected node and its edge
        if self.isSelected():
            for gr_edge in self.scene().edges:
                gr_edge.edge_wrap.update_positions()


class server(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("server.png")
        self.width = 50
        self.height = 50
        self.setPixmap(self.pix)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # update selected node and its edge
        if self.isSelected():
            for gr_edge in self.scene().edges:
                gr_edge.edge_wrap.update_positions()


class router(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("router.png")
        self.width = 50
        self.height = 50
        self.setPixmap(self.pix)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # update selected node and its edge
        if self.isSelected():
            for gr_edge in self.scene().edges:
                gr_edge.edge_wrap.update_positions()
