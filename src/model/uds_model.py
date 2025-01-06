class UDSModel:
    def send_request(self, request_data):
        # 네트워크 통신 코드
        response = self._send_can_message(request_data)
        return self._parse_response(response)

    def _send_can_message(self, data):
        # CAN 통신 코드 (python-can 사용)
        # 실제 메시지 전송 로직
        pass

    def _parse_response(self, response):
        # 응답 데이터 처리 로직
        pass
    