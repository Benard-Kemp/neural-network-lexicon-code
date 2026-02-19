"""
Reward Modeling (Pairwise Preferences) - Minimal Pytorch Example

"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Tuple, Dict

import torch
import torch.nn as nn
import torch.nn.functional as F

