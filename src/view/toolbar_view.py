from PySide6.QtWidgets import QToolBar, QLabel
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon


class ToolBarView(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)
        self.init_tool_bar()

    def init_tool_bar(self):
        """툴바 초기화."""
        self.device_label = QLabel("Device: Not Connected")
        self.addWidget(self.device_label)

        # Connect 버튼
        connect_action = QAction(QIcon("connect_icon.png"), "Connect", self)
        connect_action.triggered.connect(self.connect_device)
        self.addAction(connect_action)

        # Disconnect 버튼
        disconnect_action = QAction(
            QIcon("disconnect_icon.png"), "Disconnect", self
        )
        disconnect_action.triggered.connect(self.disconnect_device)
        self.addAction(disconnect_action)

        # Refresh 버튼
        refresh_action = QAction(QIcon("refresh_icon.png"), "Refresh", self)
        refresh_action.triggered.connect(self.refresh_project)
        self.addAction(refresh_action)

        # Log 버튼
        log_action = QAction(QIcon("log_icon.png"), "Show Log", self)
        log_action.triggered.connect(self.show_log)
        self.addAction(log_action)

    def connect_device(self):
        """기기 연결."""
        print("Connecting to device...")

    def disconnect_device(self):
        """기기 연결 해제."""
        print("Disconnecting from device...")

    def refresh_project(self):
        """프로젝트 새로고침."""
        print("Project refreshed.")

    def show_log(self):
        """로그 표시."""
        print("Log showed.")

    def update(self, model):
        """툴바의 상태를 업데이트."""
        hw_status = model.get_hw_status()
        self.setWindowTitle(f"HW Status: {hw_status}")
