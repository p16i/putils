import re 

from typing import Dict, Union

int_rx = re.compile("^[0-9]+$")

def paramset(ss: str) -> Dict[str, Union[int, float]]:
    params = dict()
    for pg in ss.split("|"):
        k, v = pg.split(":")

        if re.match(int_rx, v):
            params[k] = int(v)
        elif "." in v:
            params[k] = float(v)
        else:
            params[k] = v

    return params