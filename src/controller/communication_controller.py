class CommunicationController:
    def __init__(self, model, views):
        self.model = model
        self.views = views  # 상태바, 툴바, 메뉴바 등의 View 리스트

    def connect_hw(self):
        """HW 연결 요청."""
        self.model.connect_hw()
        self.update_views()

    def disconnect_hw(self):
        """HW 연결 해제 요청."""
        self.model.disconnect_hw()
        self.update_views()

    def update_data(self, key, value):
        """통신 데이터 업데이트 요청."""
        self.model.update_communication_data(key, value)
        self.update_views()

    def update_views(self):
        """모든 View 업데이트."""
        for view in self.views:
            view.update(self.model)
