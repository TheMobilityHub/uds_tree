class CommunicationModel:
    def __init__(self):
        self.hw_status = "Disconnected"
        self.communication_data = {}

    def connect_hw(self):
        self.hw_status = "Connected"

    def disconnect_hw(self):
        self.hw_status = "Disconnected"

    def get_hw_status(self):
        return self.hw_status

    def update_communication_data(self, key, value):
        self.communication_data[key] = value

    def get_communication_data(self):
        return self.communication_data
