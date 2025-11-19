import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# -----------------------------
#          CAPITALIZE
# -----------------------------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# -----------------------------
#             TRIM
# -----------------------------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),              # пустая строка
    ("skypro", "skypro"),  # нет пробелов в начале → ничего не меняется
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# -----------------------------
#            CONTAINS
# -----------------------------

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("123", "1", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("hello", "", True),  # пустая строка считается содержащейся в любой строке
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# -----------------------------
#          DELETE SYMBOL
# -----------------------------

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("hello world", " ", "helloworld"),  # удаление пробелов
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # символ отсутствует
    ("test", "", "test"),       # пустой символ → ничего не удаляется
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
