import pytest
from app import calculate_total, apply_discount

def test_calculate_total():
    assert calculate_total(10.0, 5) == 50.0

def test_apply_discount():
    assert apply_discount(100.0, 10) == 90.0
    assert apply_discount(50.0, 0) == 50.0
    with pytest.raises(ValueError):
        apply_discount(100.0, 105)
