from src import CommunicationModel


def test_model_initial_state():
    """
    초기 상태 테스트: HW 상태가 'Disconnected'인지 확인
    """
    model = CommunicationModel()
    assert model.get_hw_status() == "Disconnected"


def test_model_connect():
    """
    HW 연결 테스트: HW 상태가 'Connected'로 변경되는지 확인
    """
    model = CommunicationModel()
    model.connect_hw()
    assert model.get_hw_status() == "Connected"


def test_model_disconnect():
    """
    HW 연결 해제 테스트: HW 상태가 'Disconnected'로 변경되는지 확인
    """
    model = CommunicationModel()
    model.connect_hw()
    model.disconnect_hw()
    assert model.get_hw_status() == "Disconnected"


def test_model_update_communication_data():
    """
    통신 데이터 업데이트 테스트: 데이터가 올바르게 저장되는지 확인
    """
    model = CommunicationModel()
    model.update_communication_data("key1", "value1")
    model.update_communication_data("key2", "value2")

    data = model.get_communication_data()
    assert data == {"key1": "value1", "key2": "value2"}


def test_model_get_communication_data_empty():
    """
    초기 통신 데이터 테스트: 초기 상태에서 데이터가 비어 있는지 확인
    """
    model = CommunicationModel()
    assert not model.get_communication_data()
