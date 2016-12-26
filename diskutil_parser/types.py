from typing import Union

from .containers import Partition, Disk

ParseResult = Union[Disk, Partition]

__all__ = ['ParseResult']
