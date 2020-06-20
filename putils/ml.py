from typing import Dict, NamedTuple, Union

from sklearn.model_selection import ParameterSampler
from scipy.stats import distributions as dist

def uniform_sample_params(template: Dict, n_samples: int):
    # Sample according to the template for n_samples
    param_grid = dict()

    for k, v in template.items():
        if type(v) == str:
            param_grid[k] = eval("dist." + v)
        else:
            param_grid[k] = v

    return ParameterSampler(param_grid, n_iter=n_samples)
