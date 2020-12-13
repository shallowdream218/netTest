from PyQt5.QtWidgets import QGraphicsView, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

from GraphicItem import *
from edge import Edge
from static_GraphicItem import *
import copy


class GraphicView(QGraphicsView):

    def __init__(self, graphic_scene, parent=None):
        super().__init__(parent)

        self.gr_scene = graphic_scene
        self.parent = parent

        self.edge_enable = False
        self.drag_edge = None

        self.init_ui()

    def init_ui(self):
        self.setScene(self.gr_scene)
        self.setRenderHints(QPainter.Antialiasing |
                            QPainter.HighQualityAntialiasing |
                            QPainter.TextAntialiasing |
                            QPainter.SmoothPixmapTransform |
                            QPainter.LosslessImageRendering)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(self.AnchorUnderMouse)
        self.setDragMode(self.RubberBandDrag)

        item1 = static_host()
        item2 = static_switch()
        item3 = static_server()
        item4 = static_router()

        item1.setPos(0, 0)
        item2.setPos(150, 10)
        item3.setPos(300, 0)
        item4.setPos(450, 0)

        self.gr_scene.addItem(item1)
        self.gr_scene.addItem(item2)
        self.gr_scene.addItem(item3)
        self.gr_scene.addItem(item4)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_E:
            self.edge_enable = ~self.edge_enable

    def mousePressEvent(self, event):
        item = self.get_item_at_click(event)

        if event.button() == Qt.RightButton:
            if isinstance(item, host):
                self.gr_scene.remove_node(item)
            if isinstance(item, switch):
                self.gr_scene.remove_node(item)
            if isinstance(item, server):
                self.gr_scene.remove_node(item)
            if isinstance(item, router):
                self.gr_scene.remove_node(item)

        if event.button() == Qt.MidButton:
            if isinstance(item, static_host):
                if type(item) == static_host:
                    host_item = host()
                    host_item.setPos(0, 200)
                    host_item.setFlag(QGraphicsItem.ItemIsMovable)
                    self.gr_scene.add_node(host_item)
            if isinstance(item, static_switch):
                if type(item) == static_switch:
                    switch_item = switch()
                    switch_item.setPos(150, 200)
                    switch_item.setFlag(QGraphicsItem.ItemIsMovable)
                    self.gr_scene.add_node(switch_item)
            if isinstance(item, static_server):
                if type(item) == static_server:
                    server_item = server()
                    server_item.setPos(300, 200)
                    server_item.setFlag(QGraphicsItem.ItemIsMovable)
                    self.gr_scene.add_node(server_item)
            if isinstance(item, static_router):
                if type(item) == static_router:
                    router_item = router()
                    router_item.setPos(450, 200)
                    router_item.setFlag(QGraphicsItem.ItemIsMovable)
                    self.gr_scene.add_node(router_item)

        elif self.edge_enable:
            if isinstance(item, host):
                self.edge_drag_start(item)
            if isinstance(item, switch):
                self.edge_drag_start(item)
            if isinstance(item, server):
                self.edge_drag_start(item)
            if isinstance(item, router):
                self.edge_drag_start(item)

        else:
            super().mousePressEvent(event)

    def get_item_at_click(self, event):
        """ Return the object that clicked on. """
        pos = event.pos()
        item = self.itemAt(pos)
        return item

    # 这个方法是删除选中的所有图元，原来这个方法是可以的，因为它就一个类型的图元。而现在有四种类型的图元，而参数只有一个，所以这个删除是不可以的。
    def get_items_at_rubber(self):
        """ Get group select items. """
        area = self.rubberBandRect()
        return self.items(area)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self.edge_enable and self.drag_edge is not None:
            sc_pos = self.mapToScene(pos)
            self.drag_edge.gr_edge.set_dst(sc_pos.x(), sc_pos.y())
            self.drag_edge.gr_edge.update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.edge_enable:
            # 拖拽结束后，关闭此功能
            self.edge_enable = False
            item = self.get_item_at_click(event)
            # 终点图元不能是起点图元，即无环图
            if isinstance(item, host) and item is not self.drag_start_item:
                self.edge_drag_end(item)
            if isinstance(item, switch) and item is not self.drag_start_item:
                self.edge_drag_end(item)
            if isinstance(item, server) and item is not self.drag_start_item:
                self.edge_drag_end(item)
            if isinstance(item, router) and item is not self.drag_start_item:
                self.edge_drag_end(item)

            else:
                self.drag_edge.remove()
                self.drag_edge = None
        else:
            super().mouseReleaseEvent(event)

    def edge_drag_start(self, item):
        self.drag_start_item = item
        self.drag_edge = Edge(self.gr_scene, self.drag_start_item, None)

    def edge_drag_end(self, item):
        new_edge = Edge(self.gr_scene, self.drag_start_item, item)
        self.drag_edge.remove()
        self.drag_edge = None
        new_edge.store()
