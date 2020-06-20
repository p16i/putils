import math
import time

import pytest

from putils import runtime

def test_timer():
    
    tm = runtime.Timer("so") 
    with tm:
        time.sleep(1)

    assert math.fabs(tm.time_took - 1) < 1e-2