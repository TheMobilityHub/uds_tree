import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QTabWidget
from PySide6.QtGui import QShortcut, QKeySequence
from qt_material import apply_stylesheet
from src import MenuBarView, StatusBarView, ToolBarView
from src import CommunicationModel
from src import CommunicationController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("UDS Tree")
        self.set_window_size()

        self.communication_model = CommunicationModel()
        self.status_bar = StatusBarView()
        self.tool_bar = ToolBarView()
        self.menu_bar = MenuBarView()
        self.communication_controller = CommunicationController()

        self.connect_mvc()

        self.init_ui()
        self.init_shortcuts()

    def set_window_size(self):
        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        width = int(screen_size.width() * 0.8)
        height = int(screen_size.height() * 0.8)
        x = (screen_size.width() - width) // 2
        y = (screen_size.height() - height) // 2
        self.setGeometry(x, y, width, height)

    def connect_mvc(self):

        self.communication_controller.model = self.communication_model

        self.communication_controller.views = [
            self.status_bar,
            self.tool_bar,
            self.menu_bar,
        ]

        self.tool_bar.controller = self.communication_controller
        self.menu_bar.controller = self.communication_controller

    def init_ui(self):

        self.setStatusBar(self.status_bar)
        self.addToolBar(self.tool_bar)
        self.setMenuBar(self.menu_bar)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

    def init_shortcuts(self):

        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(self.close)

        connect_shortcut = QShortcut(QKeySequence("C"), self)
        connect_shortcut.activated.connect(
            self.communication_controller.connect_device()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    apply_stylesheet(app, theme="dark_blue.xml", extra={"density_scale": "0"})
    main_window.show()
    sys.exit(app.exec())
