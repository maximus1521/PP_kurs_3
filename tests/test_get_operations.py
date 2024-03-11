from src.get_operations import sort_executed_operations


def test_sort_executed_operations():
    a = [
        {"state": "EXECUTED", "date": "2024-06-01"},
        {"state": "EXECUTED", "date": "2023-05-05"},
        {"state": "CANCELED", "date": "2022-04-12"},
        {"state": "EXECUTED", "date": "2022-04-12"},
        {"state": "EXECUTED", "date": "2021-03-12"},
        {"state": "EXECUTED", "date": "2019-02-12"},
        {"state": "EXECUTED", "date": "2023-01-12"}
    ]
    b = [
        {"state": "EXECUTED", "date": "2024-06-01"},
        {"state": "EXECUTED", "date": "2023-05-05"},
        {"state": "EXECUTED", "date": "2023-01-12"},
        {"state": "EXECUTED", "date": "2022-04-12"},
        {"state": "EXECUTED", "date": "2021-03-12"}
    ]
    assert sort_executed_operations(a) == b
