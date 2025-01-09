from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction


class MenuBarView(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._controller = None
        self.init_menu_bar()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value
        self.init_actions()

    def init_menu_bar(self):

        self.file_menu = self.addMenu("File")
        self.settings_menu = self.addMenu("Settings")
        self.tools_menu = self.addMenu("Tools")
        self.help_menu = self.addMenu("Help")

    def init_actions(self):

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self._controller.close_application)
        self.file_menu.addAction(exit_action)

        open_project_action = QAction("Open Project", self)
        open_project_action.triggered.connect(self._controller.open_project)
        self.file_menu.addAction(open_project_action)

        save_project_action = QAction("Save Project", self)
        save_project_action.triggered.connect(self._controller.save_project)
        self.file_menu.addAction(save_project_action)

        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self._controller.save_as_project)
        self.file_menu.addAction(save_as_action)

        close_project_action = QAction("Close Project", self)
        close_project_action.triggered.connect(self._controller.close_project)
        self.file_menu.addAction(close_project_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self._controller.show_about_dialog)
        self.help_menu.addAction(about_action)

        license_info_action = QAction("License Information", self)
        license_info_action.triggered.connect(
            self._controller.show_license_info
        )
        self.help_menu.addAction(license_info_action)

    def update(self, model):

        print(f"MenuBar updated: {model.get_hw_status()}")
