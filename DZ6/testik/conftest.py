#coding=utf-8
import pytest
@pytest.fixture(autouse=True)
def my_fixture():
    with open("testirovanie.txt", "w") as f:
        pass