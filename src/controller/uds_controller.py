class UDSController:
    def __init__(self, uds_model, uds_view):
        self.uds_model = uds_model
        self.uds_view = uds_view

    def handle_send_request(self, request_data):
        response = self.uds_model.send_request(request_data)
        self.uds_view.update_response_display(response)
