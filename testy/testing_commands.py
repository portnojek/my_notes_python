import pytest

def func(x):
    return x + 0.1

def test_answer():
    assert func(4.9) == 5

def test_approx():
    assert func(5) == 5.1


# wywołanie funkcji w pytest 'python -m pytest testing_commands.py'
# w normalnym świecie wyglądałoby to poprostu 'pyton + plik'