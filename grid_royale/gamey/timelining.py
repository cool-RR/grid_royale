# Copyright 2020 Ram Rachum and collaborators.
# This program is distributed under the MIT license.

from __future__ import annotations

import random
import concurrent.futures
import numbers
from typing import (Iterable, Union, Optional, Tuple, Any, Iterator, Type,
                    Sequence, Callable)
import collections.abc

import keras.models
import more_itertools
import numpy as np

from .base import Observation, Action
from .policing import Policy, QPolicy
from . import utils


class BaseTimeline(collections.abc.Sequence):
    def __init__(self):
        ...

class FullTimeline(BaseTimeline):
    def __init__(self, observation: Observation, action: Action) -> None:
        self.observations = [observation]
        self.actions = [action]
        self.rewards = []

class ListView(collections.abc.Sequence):
    def __init__(self, _list: list, length: int) -> None:
        self._list = _list
        self.length = length


    def __len__(self):
        return max(self.length, len(self._list))


    def __getitem__(self, i: Union[int, slice]) -> Any:
        if isinstance(i, int):
            if i >= self.length or i <= - (self.length + 1):
                raise IndexError
            else:
                return self._list[i]
        else:
            assert isinstance(i, slice)
            raise NotImplementedError




class Timeline(BaseTimeline):
    def __init__(self, observation: Observation, action: Action) -> None:
        self._full_timeline = FullTimeline(observation, action)



