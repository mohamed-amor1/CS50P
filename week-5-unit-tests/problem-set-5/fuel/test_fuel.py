from fuel import gauge, convert
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("4/4") == 100
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
