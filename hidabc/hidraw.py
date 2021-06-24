# SPDX-License-Identifier: MIT

import functools
import os

from typing import List

import ioctl.hidraw


class HidrawInterface():
    def __init__(self, path: str) -> None:
        self._hidraw = ioctl.hidraw.Hidraw(path)
        self._bus, self._vid, self._pid = self._hidraw.info

    @property
    @functools.lru_cache(maxsize=None)
    def name(self) -> str:
        return self._hidraw.name

    @property
    @functools.lru_cache(maxsize=None)
    def phys_name(self) -> str:
        return self._hidraw.phys

    @property
    @functools.lru_cache(maxsize=None)
    def uniq_name(self) -> str:
        return self._hidraw.uniq

    @property
    def bus(self) -> int:
        return self._bus

    @property
    def vid(self) -> int:
        return self._vid

    @property
    def pid(self) -> int:
        return self._pid

    @property
    @functools.lru_cache(maxsize=None)
    def report_descriptor(self) -> List[int]:
        return self._hidraw.report_descriptor

    def read(self) -> List[int]:
        return list(os.read(self._hidraw.fd, 1024))  # 1024 is already too much for HID data

    def write(self, data: List[int]) -> None:
        written = os.write(self._hidraw.fd, bytes(data))
        if written != len(data):
            raise IOError(f'Failed to write (expected to write {len(data)} but wrote {written})')
