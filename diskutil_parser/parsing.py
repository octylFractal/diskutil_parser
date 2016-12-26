import plistlib
from pathlib import Path
from typing import TextIO, List

from .containers import Disk, Partition
from .types import ParseResult


def parse(data: (TextIO, str)) -> List[ParseResult]:
    if isinstance(data, TextIO):
        data = data.read()

    plist = plistlib.loads(data)
    # We're interested in the partitions too
    adap_data = plist['AllDisksAndPartitions']
    return [deserialize(disk_data) for disk_data in adap_data]


def deserialize(data) -> ParseResult:
    """
    Deserialize `data` into a Disk or Partition, depending on the data.

    :param data: the plist data
    :return: a Disk or Partition
    """
    if "Partitions" in data:
        # This is a disk
        return deserialize_disk(data)
    # Otherwise probably a partion
    return deserialize_part(data)


def deserialize_disk(data) -> Disk:
    size = data["Size"]
    part_scheme = data.get("Content", "")
    device_id = data["DeviceId"]
    partitions = [deserialize_part(part_data) for part_data in data["Partitions"]]
    return Disk(size, part_scheme, device_id, partitions)


def deserialize_part(data) -> Partition:
    # I think DiskUUID is what we want.
    uuid = data.get("DiskUUID", "")
    name = data.get("VolumeName", "")
    mount_point = Path(data["MountPoint"]) if "MountPoint" in data else None
    size = data["Size"]
    content_type = data["Content"]
    device_id = data["DeviceId"]
    return Partition(name, content_type, device_id, uuid, size, mount_point)


__all__ = ['parse', 'deserialize', 'deserialize_disk', 'deserialize_part']
