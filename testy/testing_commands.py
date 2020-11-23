import pytest
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# wywołanie funkcji w pytest 'python -m pytest testing_commands.py'
# w normalnym świecie wyglądałoby to poprostu 'pyton + plik
'przydane strony'