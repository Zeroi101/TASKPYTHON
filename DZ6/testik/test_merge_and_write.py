import pytest
from DZ62 import merge_and_write
def create_test_data(test_data):
    with open("testirovanie.txt", "a") as f:
        f.writelines(test_data)
def test_merge_and_write():
    test_data = ["aboba perviy\n" "aboba vtoroy\n" "aboba amogus\n" "amogus dva\n" "amogus tri\n"]
    create_test_data(test_data)
    assert test_data == merge_and_write("test.txt", "test2.txt", "testirovanie.txt")
@pytest.mark.parametrize(
        "result_exception, file1_path, file2_path, output_file_path",
        [
         (FileNotFoundError,"test.txt","test2.txt","testirovanie.txt")
        ]
)
def test_with_exception(result_exception, file1_path, file2_path, output_file_path):
    with pytest.raises(result_exception):
        merge_and_write("test.txt","test3.txt","testirovanie.txt")