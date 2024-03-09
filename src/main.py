from get_operations import load_operations, sort_executed_operations
from func import changing_account_number_of_address, transfer_date_format, changing_account_number_of_sender

operations_data = load_operations()


def main():
    input(f'For last five operations click ENTER')
    for operation in sort_executed_operations(operations_data):
        print()
        date = operation.get('date')
        print(f"{transfer_date_format(date)} {operation.get('description')}")
        sender = operation.get('from')
        print(sender)
        address = operation.get('to')
        print(f"{changing_account_number_of_sender(sender)} -> {changing_account_number_of_address(address)}")
        print(f"{operation.get('operationAmount')["amount"]} {operation.get('operationAmount')["currency"]["name"]}")


if __name__ == "__main__":
    main()
