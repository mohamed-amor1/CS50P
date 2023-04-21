from twttr import shorten
import pytest


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("twIttEr") == "twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("1") == "1"
