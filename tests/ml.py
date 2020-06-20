from putils import ml

def test_uniform_sample():
    float_list = [1.1, 1.5, 1.5]
    template = {
        "some_int": "uniform(0, 5)",
        "some_float": "loguniform(1e-5, 1e-3)",
        "float_from_list": [1.1, 1.5, 1.5],
    }

    total = 3
    for i, res in enumerate(ml.uniform_sample_params(template, total)):
        assert 0 <= res["some_int"] <= 5
        assert 1e-5 <= res["some_float"] <= 1e-3
        assert res["float_from_list"] in float_list

    assert i == total - 1