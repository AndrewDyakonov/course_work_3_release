from funktion import get_json_to_list


def test_get_json_to_list():
    """Тест функции get_json_to_list"""
    assert type(get_json_to_list()) == list
    assert get_json_to_list() is not None
