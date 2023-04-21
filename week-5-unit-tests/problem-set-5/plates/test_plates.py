from plates import is_valid
import pytest


def test_start_with_2_letters():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True


def test_lenght_between_2_and_6():
    assert is_valid("AB1235") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCD123") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("") == False


def number_in_the_end_not_in_middle():
    assert is_valid("AB12B4") == False
    assert is_valid("AB1234") == True
    assert is_valid("1234AB") == False
    assert is_valid("AB12345") == False


def no_periods_spaces_punctuation_marks():
    assert is_valid("AB-123") == False
    assert is_valid("AJ.123") == False
    assert is_valid("AA 123") == False
    assert is_valid("AX!123") == False
    assert is_valid("AZ!#12") == False
    assert is_valid("AN$123") == False
