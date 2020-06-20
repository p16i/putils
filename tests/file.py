import pytest

from putils import file


def test_add_suffix_to_file_path():

    res = file.add_suffix_to_file_path("~/abc.txt", "new")

    assert res == "~/abc-new.txt"