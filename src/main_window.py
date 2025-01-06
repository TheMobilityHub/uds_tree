from PySide6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QTabWidget,
    QLabel, QMenuBar, QMessageBox, QToolBar
)
from PySide6.QtGui import QAction, QIcon, QShortcut, QKeySequence
from PySide6.QtCore import Qt
from controller.uds_controller import UDSController
from model.uds_model import UDSModel
from view.uds_view import UDSView
from qt_material import apply_stylesheet
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UDS Tree")

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()

        # 화면 크기의 70%로 설정
        width = int(screen_size.width() * 0.8)
        height = int(screen_size.height() * 0.8)
        x = (screen_size.width() - width) // 2
        y = (screen_size.height() - height) // 2

        self.setGeometry(x, y, width, height)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # 상태바 추가
        self.init_status_bar()

        # QMenuBar 추가
        self.init_menu_bar()

        # QToolBar 추가
        self.tool_bar = QToolBar("Main Toolbar", self)
        self.addToolBar(Qt.RightToolBarArea, self.tool_bar)
        self.init_tool_bar()

        # 단축키 초기화
        self.init_shortcuts()

        # uds_model = UDSModel()
        # uds_view = UDSView()
        # uds_controller = UDSController(uds_model, uds_view)

        # self.tab_widget.addTab(uds_view, "UDS Communication")

    def init_status_bar(self):
        self.statusBar().setStyleSheet("""
        QStatusBar::item {
            border: none; 
        }
    """)
        
        self.status_message = QLabel("Project Not Selected")
        self.statusBar().addWidget(self.status_message)

        self.connection_status = QLabel("Disconnected")
        self.connection_status.setStyleSheet("color: red;")
        self.statusBar().addPermanentWidget(self.connection_status)

    def init_menu_bar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        file_menu = self.menu_bar.addMenu("File")
        settings_menu = self.menu_bar.addMenu("Settings")
        tools_menu = self.menu_bar.addMenu("Tools")
        help_menu = self.menu_bar.addMenu("Help")

        # File 메뉴에 Exit 추가
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        file_menu.addMenu("Open Project")
        file_menu.addMenu("Save Project")
        file_menu.addMenu("Save As")
        file_menu.addMenu("Close Project")

        settings_menu.addMenu("Theme Settings")
        settings_menu.addMenu("Log Settings")
        settings_menu.addMenu("User Settings")
        settings_menu.addMenu("Shortcuts")

        tools_menu.addMenu("Checksum Calculator")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
        help_menu.addMenu("License Information")
        help_menu.addMenu("User Guide")

    def init_tool_bar(self):
        # Device 상태 표시
        self.device_label = QLabel("Device: Not Connected")
        self.tool_bar.addWidget(self.device_label)

        # Connect 버튼
        connect_action = QAction(QIcon("connect_icon.png"), "Connect", self)
        connect_action.triggered.connect(self.connect_device)
        self.tool_bar.addAction(connect_action)

        # Disconnect 버튼
        disconnect_action = QAction(QIcon("disconnect_icon.png"), "Disconnect", self)
        disconnect_action.triggered.connect(self.disconnect_device)
        self.tool_bar.addAction(disconnect_action)

        # Refresh 버튼
        refresh_action = QAction(QIcon("disconnect_icon.png"), "Refresh", self)
        refresh_action.triggered.connect(self.refresh_project)
        self.tool_bar.addAction(refresh_action)
        # Refresh 버튼
        log_action = QAction(QIcon("disconnect_icon.png"), "Show Log", self)
        log_action.triggered.connect(self.show_log)
        self.tool_bar.addAction(log_action)
        
    def init_shortcuts(self):
        # Ctrl+Q: 애플리케이션 종료
        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(self.close)

        # Ctrl+S: 데이터 저장
        save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        save_shortcut.activated.connect(self.save_data)

        # F5: 새로 고침
        refresh_shortcut = QShortcut(QKeySequence("F5"), self)
        refresh_shortcut.activated.connect(self.refresh_data)

        # Ctrl+Shift+S: 모든 설정 저장
        save_all_shortcut = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
        save_all_shortcut.activated.connect(self.save_all_data)

    def show_about_dialog(self):
        QMessageBox.about(self, "About", "UDS Communication Tool v1.0")

    def update_status_bar(self, connection_status, process_status):
        # 연결 상태 업데이트
        self.connection_status.setText("Connected" if connection_status else "Disconnected")
        self.connection_status.setStyleSheet("color: green;" if connection_status else "color: red;")

        # 프로세스 상태 업데이트
        self.status_message.setText(process_status)

    def connect_device(self):
        print("Connecting to device...")
        self.update_status_bar(True, "Connecting to device...")

    def disconnect_device(self):
        print("Disconnecting from device...")
        self.update_status_bar(False, "Disconnected")

    def save_data(self):
        print("Data saved.")

    def refresh_data(self):
        print("Data refreshed.")

    def save_all_data(self):
        print("All settings saved.")

    def refresh_project(self):
        print("Project refreshed")

    def show_log(self):
        print("Log showed")
    
    def resizeEvent(self, event):
        self.tab_widget.resize(event.size())  # QTabWidget 크기를 창에 맞춤
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    extra = {
        'density_scale': '0',  # Density Scale
    }

    main_window = MainWindow()
    apply_stylesheet(app, theme='dark_blue.xml', extra=extra)
    main_window.show()
    sys.exit(app.exec())
