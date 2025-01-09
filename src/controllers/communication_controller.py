class CommunicationController:
    def __init__(self, model=None, views=None):
        self._model = model
        self._views = views if views else []

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, value):
        self._views = value

    def close_application(self):
        print("Application closed.")

    def open_project(self):

        print("Opening project...")

    def save_project(self):

        print("Saving project...")

    def save_as_project(self):

        print("Saving project as...")

    def close_project(self):

        print("Closing project...")

    def show_about_dialog(self):

        print("Showing About dialog.")

    def show_license_info(self):
        print("Displaying license information.")

    def update_views(self):
        for view in self._views:
            view.update(self._model)

    def connect_device(self):
        print("Connecting Device ... ")

    def disconnect_device(self):
        print("Disconnect!")

    def refresh_project(self):
        print("refresh!")

    def show_log(self):
        print("Show Log")
