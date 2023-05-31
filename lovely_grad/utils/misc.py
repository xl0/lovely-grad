# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/03b_utils.misc.ipynb.

# %% auto 0
__all__ = []

# %% ../../nbs/03b_utils.misc.ipynb 4
import re
import codecs
import numpy as np

from tinygrad.tensor import Tensor

from fastcore.test import test_eq

# %% ../../nbs/03b_utils.misc.ipynb 6
def is_cpu(x: Tensor) -> bool:
    x.device.lower() == "cpu"
    # assert 1, "Not implemented"

    # if hasattr(x, "devices"): # Unified Array (jax >= 0.4)
    #     return list(x.devices())[0] == jax.devices("cpu")[0]
    # if hasattr(x, "device"): # Old-style DeviceArray
    #     return x.device() == jax.devices("cpu")[0]

    # assert hasattr(x, "sharding"), f"Weird input type={type(input)}, expecrted Array, DeviceArray, or ShardedDeviceArray"
    # return False

