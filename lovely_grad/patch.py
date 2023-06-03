# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/10_patch.ipynb.

# %% auto 0
__all__ = ['monkey_patch']

# %% ../nbs/10_patch.ipynb 5
from typing import Any, Optional as O


from tinygrad.tensor import Tensor
import numpy as np

# import torch
from fastcore.foundation import patch_to
from matplotlib import pyplot as plt, rcParams

from .repr_str import StrProxy


from .repr_rgb import RGBProxy
from .repr_plt import PlotProxy
from .repr_chans import ChanProxy

# %% ../nbs/10_patch.ipynb 11
def monkey_patch(cls=Tensor):
    "Monkey-patch lovely features into `cls`" 

    if not hasattr(cls, '_plain_repr'):
            cls._plain_repr = cls.__repr__
            cls._plain_str = cls.__str__

    @patch_to(cls)
    def __repr__(self: Tensor):
        return str(StrProxy(self))

    # Plain - the old behavior
    @patch_to(cls, as_prop=True)
    def p(self: Tensor):
        return StrProxy(self, plain=True)

    # Verbose - print both stats and plain values
    @patch_to(cls, as_prop=True)
    def v(self: Tensor):
        return StrProxy(self, verbose=True)

    # .deeper and .deeper(...)
    @patch_to(cls, as_prop=True)
    def deeper(self: Tensor):
        return StrProxy(self, depth=1)

    # .rgb and .rgb(...)
    @patch_to(cls, as_prop=True)
    def rgb(t: Tensor):
        return RGBProxy(t)
    
    # .chans and .chans(...)
    @patch_to(cls, as_prop=True)
    def chans(t: Tensor):
        return ChanProxy(t)

    # .plt and .plt(...)
    @patch_to(cls, as_prop=True)
    def plt(t: Tensor):
        return PlotProxy(t)
