import json


def load_operations():
    with open('C:/Users/maxim/PycharmProjects/PP_kurs_3/src/operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def sort_executed_operations(operations_data):
    """
    Taking all operations
    :return: list of last 5 executed ops sorted by date
    """
    executed_operations = []
    for operation in operations_data:
        if operation.get('state') == "EXECUTED" and operation.get('date'):
            executed_operations.append(operation)

    executed_operations.sort(key=lambda k: k['date'])
    # Sorting operations by date

    last_five_operations = executed_operations[-5:]
    # Taking last five operations

    return last_five_operations[::-1]
