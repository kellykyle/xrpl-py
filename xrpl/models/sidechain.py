"""A Sidechain represents a door account to a bridge."""

from __future__ import annotations

from dataclasses import dataclass

from xrpl.models.base_model import BaseModel
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class Sidechain(BaseModel):
    """A Sidechain represents a door account to a bridge."""

    src_chain_door: str
    src_chain_issue: str
    dst_chain_door: str
    dst_chain_issue: str
