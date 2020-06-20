import pytest

from putils import parsing

def test_parse_model_params():
    act = parsing.paramset("emb:32|l1:48|do:0.5")

    exp = dict(emb=32, l1=48, do=0.5)

    assert act == exp