from PySide6.QtWidgets import QStatusBar, QLabel


class StatusBarView(QStatusBar):
    def __init__(self):
        super().__init__()
        self.init_status_bar()

    def init_status_bar(self):
        """상태바 초기화."""
        self.status_message = QLabel("Project Not Selected")
        self.addWidget(self.status_message)

        self.connection_status = QLabel("Disconnected")
        self.connection_status.setStyleSheet("color: red;")
        self.addPermanentWidget(self.connection_status)

    def update(self, connection_status, process_status):
        """상태 업데이트."""
        self.connection_status.setText(
            "Connected" if connection_status else "Disconnected"
        )
        self.connection_status.setStyleSheet(
            "color: green;" if connection_status else "color: red;"
        )
        self.status_message.setText(process_status)
