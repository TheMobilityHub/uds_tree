from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon


class ToolBarView(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)
        self._controller = None

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value

        self.init_actions()

    def init_actions(self):

        connect_action = QAction(QIcon("connect_icon.png"), "Connect", self)
        connect_action.triggered.connect(self._controller.connect_device)
        self.addAction(connect_action)

        disconnect_action = QAction(
            QIcon("disconnect_icon.png"), "Disconnect", self
        )
        disconnect_action.triggered.connect(self._controller.disconnect_device)
        self.addAction(disconnect_action)

        refresh_action = QAction(QIcon("refresh_icon.png"), "Refresh", self)
        refresh_action.triggered.connect(self._controller.refresh_project)
        self.addAction(refresh_action)

        log_action = QAction(QIcon("log_icon.png"), "Show Log", self)
        log_action.triggered.connect(self._controller.show_log)
        self.addAction(log_action)

    def update(self, model):
        """툴바 상태 업데이트."""
        hw_status = model.get_hw_status()
        self.device_label.setText(f"Device: {hw_status}")
