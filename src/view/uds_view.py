from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem


class UDSView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 메인 레이아웃
        layout = QVBoxLayout(self)

        # 제목 라벨
        self.title_label = QLabel("UDS Communication")
        layout.addWidget(self.title_label)

        # 요청 데이터 입력 필드
        self.request_input = QLineEdit()
        self.request_input.setPlaceholderText("Enter UDS request data")
        layout.addWidget(self.request_input)

        # 요청 전송 버튼
        self.send_request_button = QPushButton("Send Request")
        layout.addWidget(self.send_request_button)

        # 응답 데이터 표시 테이블
        self.response_table = QTableWidget(0, 2)  # 0행 2열 테이블
        self.response_table.setHorizontalHeaderLabels(["Key", "Value"])
        layout.addWidget(self.response_table)

    def get_request_data(self):
        """입력 필드에서 요청 데이터를 가져옵니다."""
        return self.request_input.text()

    def update_response_display(self, response_data):
        """응답 데이터를 테이블에 표시합니다."""
        self.response_table.setRowCount(0)  # 기존 행 삭제
        for key, value in response_data.items():
            row_position = self.response_table.rowCount()
            self.response_table.insertRow(row_position)
            self.response_table.setItem(row_position, 0, QTableWidgetItem(key))
            self.response_table.setItem(row_position, 1, QTableWidgetItem(value))
