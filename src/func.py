from datetime import datetime


def transfer_date_format(date):
    """
    Transfer date format to required
    :return: easy readable Date format
    """
    new_date = date[:10]
    new_date = datetime.strptime(new_date, "%Y-%m-%d").strftime('%d.%m.%Y')
    return new_date


def changing_account_number_of_sender(sender):
    """
    Hiding sensitive account info from sender 'FROM'
    :return: crosses and digits in account num of 'FROM'
    """
    if not sender:
        return 'NO DATA'
    else:
        sender_digit_part = sender.split()[-1]
        if len(sender_digit_part) == 20:
            hidden_sender = sender[:-21] + ' **' + sender[-4:]
        else:
            hidden_sender = sender[:-17] + ' ' + sender[-16:-12] + ' ' + sender[-12:-10] + '** **** ' + sender[-4:]
    return hidden_sender


def changing_account_number_of_address(address):
    """
    Hiding sensitive account info of recipient
    :return: crosses and digits in account num of 'TO'
    """
    address_digit_part = address.split()[-1]
    if len(address_digit_part) == 20:
        hidden_address = address[:-21] + ' **' + address[-4:]
    else:
        hidden_address = address[:-17] + ' ' + address[-16:-12] + ' ' + address[-12:-10] + '** **** ' + address[-4:]
    return hidden_address


