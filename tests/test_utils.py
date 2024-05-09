from pathlib import Path
from src.utils import get_date_from_str, load_json, sort_list_dict_by_key, hide_account_number

ROOT_PATH = Path(__file__).parent.parent
TEST_1_JSON = ROOT_PATH.joinpath("tests", "test_data", "test.json")
TEST_2_JSON = ROOT_PATH.joinpath("tests", "test_data", "test_sort_data.json")


def test_get_date_from_str():
    assert get_date_from_str("2019-07-03T18:35:29.512364") == "03.07.2019"


def test_load_json():
    assert load_json(TEST_1_JSON) == [{"id": 1, "amount": "31957.58"}, {"id": 2, "amount": "3234682.45"}]


def test_sort_list_dict_by_key():
    assert sort_list_dict_by_key(load_json(TEST_2_JSON), "date") == [
        {'date': '2020-07-11T10:50:58.294041', 'amount': '200', 'name': 'руб.'},
        {'date': '2019-08-30T10:55:58.294041', 'amount': '400', 'name': 'руб.'},
        {'date': '2019-08-30T10:50:58.294041', 'amount': '300', 'name': 'руб.'},
        {'date': '2019-08-26T10:50:58.294041', 'amount': '100', 'name': 'руб.'}
    ]


def test_hide_account_number():
    assert hide_account_number("Счет 35383033474447895560") == "Счет **5560"
    assert hide_account_number("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert hide_account_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert hide_account_number("") == ""
