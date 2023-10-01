"""
Test goes here
"""
from main import main_res


def test_func():
    return main_res()


if __name__ == "__main__":
    assert test_func()["extract_to"] == "./data/rainfall.csv"
    assert test_func()["transform_db"] == "rainfall.db"
    assert test_func()["create"] == "Create Success"
    assert test_func()["read"] == "Read Success"
    assert test_func()["update"] == "Update Success"
    assert test_func()["delete"] == "Delete Success"
