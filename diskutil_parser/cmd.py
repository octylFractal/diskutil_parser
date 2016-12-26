from typing import List

from sh import Command

from .parsing import parse
from .types import ParseResult

_diskutil_list = Command('diskutil').bake('list', '-plist')


def diskutil_list() -> List[ParseResult]:
    proccess = _diskutil_list()
    data = proccess.stdout.decode('utf-8')
    return parse(data)


__all__ = ['diskutil_list']
