from pathlib import Path
from typing import List


class Device:
    def __init__(self, device_id: str, size: int):
        """
        :param device_id: The ID of the device, like disk0 or disk0s1
        :param size: The size of the device
        """
        self.device_id = device_id
        """The device ID, like disk0 or disk0s1"""
        self.size = size
        """The size of the partition, in bytes"""

    @property
    def device_path(self) -> Path:
        """
        The path to the device.
        """
        return Path(f"/dev/{self.device_id}")

    @property
    def raw_device_path(self) -> Path:
        """
        The path to the raw device, which isn't block-buffered.
        """
        return Path(f"/dev/r{self.device_id}")


class Partition(Device):
    def __init__(self, name: str, content_type: str, device_id: str, uuid: str, size: int, mount_point: Path):
        """
        :param name: The name of the partition
        :param content_type: The type of the partition, e.g. Linux swap, Apple_HFS
        :param device_id: The ID of the device, like disk0s1
        :param uuid: The UUID of the partition
        :param size: The size of the partition
        :param mount_point: The mount point, if this partition is mounted
        """
        super().__init__(device_id, size)
        self.name = name
        """The name of the partition"""
        self.uuid = uuid
        """The UUID of the partition"""
        self.content_type = content_type
        """The type of the partition"""
        self.mount_point = mount_point
        """The mount point, if mounted, otherwise None"""

    def is_mounted(self):
        return self.mount_point is not None and self.mount_point.exists()


class Disk(Device):
    def __init__(self, size: int, partition_scheme: str, device_id: str, partitions: List[Partition]):
        """
        :param size: The size of the disk
        :param partition_scheme: The partition scheme for the disk
        :param device_id: The ID of the device, like disk0
        :param partitions: The partition list
        """
        super().__init__(device_id, size)
        self.partition_scheme = partition_scheme
        """The partition scheme for the disk. May be None if not detected"""
        self.partitions = partitions
        """The partition list"""

__all__ = ['Device', 'Partition', 'Disk']
