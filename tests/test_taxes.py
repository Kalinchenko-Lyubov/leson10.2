import pytest

from src.taxes import calculate_taxes


def test_calculate_taxes():
    assert calculate_taxes([100, 1000], 20) == [120, 1200]


def test_calculate_taxes_empty_tax():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([0], 20)

    assert str(exc_info.value) == 'Неверная цена'

def test_calculate_taxes_empty_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([20], -5)

    assert str(exc_info.value) == 'Неверный налоговый процент'