from twttr import shorten
import pytest

def test_str():
    assert shorten("Just setting up my twitter") == "jst sttng p my twttr"
    assert shorten("These Are Just Words") == "Ths r jst wrds"
    assert shorten("THESE ARE ALL CAPS") == "Ths r ll cps"
    assert shorten("these are all lower") == "Ths r ll lwr"

def test_digit():
    assert shorten("1000000") == "1000000"
    assert shorten("456 543 234") == "456 543 234"
    assert shorten("360, 000, 000") == "360, 000, 000"

def test_mark():
    assert shorten("!@#$%^&*") == "!@#$%^&*"
    assert shorten("(){}[]") == "(){}[]"
    assert shorten("\n\t\/") == "\n\t\/"
    assert shorten(", . ; ' : \" ") == ", . ; ' : \" "

def test_comb():
    assert shorten("These Are 3 $10 notes.") == "Ths r 3 $10 nts."
    assert shorten("Go Crazy! 100//") == "G Crzy! 100//"