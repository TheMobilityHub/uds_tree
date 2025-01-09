from PySide6.QtWidgets import QMenuBar, QMessageBox
from PySide6.QtGui import QAction


class MenuBarView(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_menu_bar()

    def init_menu_bar(self):
        """메뉴바 초기화."""
        file_menu = self.addMenu("File")
        settings_menu = self.addMenu("Settings")
        tools_menu = self.addMenu("Tools")
        help_menu = self.addMenu("Help")

        # File 메뉴
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close_application)
        file_menu.addAction(exit_action)
        file_menu.addAction("Open Project")
        file_menu.addAction("Save Project")
        file_menu.addAction("Save As")
        file_menu.addAction("Close Project")

        # Settings 메뉴
        settings_menu.addAction("Theme Settings")
        settings_menu.addAction("Log Settings")
        settings_menu.addAction("User Settings")
        settings_menu.addAction("Shortcuts")

        # Tools 메뉴
        tools_menu.addAction("Checksum Calculator")

        # Help 메뉴
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
        help_menu.addAction("License Information")
        help_menu.addAction("User Guide")

    def show_about_dialog(self):
        """About 대화상자 표시."""
        QMessageBox.about(self, "About", "UDS Communication Tool v1.0")

    def close_application(self):
        """애플리케이션 종료."""
        self.parent().close()

    def update(self, model):
        """메뉴바 상태 업데이트."""
        print(f"MenuBar updated: {model.get_hw_status()}")
