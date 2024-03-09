from src.func import transfer_date_format, changing_account_number_of_sender, changing_account_number_of_address


def test_transfer_date_format():
    assert transfer_date_format('2019-01-02') == '02.01.2019'
    assert transfer_date_format('2022-02-19') == '19.02.2022'
    assert transfer_date_format('2023-12-01') == '01.12.2023'


def test_changing_account_number_of_sender():
    assert changing_account_number_of_sender('Счет 71687416928274675290') == 'Счет **5290'
    assert changing_account_number_of_sender('МИР 5211277418228469') == 'МИР 5211 27** **** 8469'
    assert changing_account_number_of_sender('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert changing_account_number_of_sender('Visa Platinum 6942697754917688') == 'Visa Platinum 6942 69** **** 7688'
    assert changing_account_number_of_sender('MasterCard 8847384717023026') == 'MasterCard 8847 38** **** 3026'


def test_changing_account_number_of_address():
    assert changing_account_number_of_address('Счет 71687416928274675290') == 'Счет **5290'
    assert changing_account_number_of_address('МИР 5211277418228469') == 'МИР 5211 27** **** 8469'
    assert changing_account_number_of_address('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert changing_account_number_of_address('Visa Platinum 6942697754917688') == 'Visa Platinum 6942 69** **** 7688'
    assert changing_account_number_of_address('MasterCard 8847384717023026') == 'MasterCard 8847 38** **** 3026'
