# SPDX-License-Identifier: MIT

import functools

from typing import List

import hid

import hidabc


class HidapiInterface(hidabc.ExtendedInterface):
    def __init__(self, path: str) -> None:
        self._hidapi = hid.device()
        self._hidapi.open_path(str.encode(path))

        # FIXME: Fetch this dict directly from device_info struct
        for device_dict in hid.enumerate():
            if device_dict['path'] == path:
                self._vid = device_dict['vendor_id']
                self._pid = device_dict['product_id']

    @property
    @functools.lru_cache(maxsize=None)
    def name(self) -> str:
        return str(self._hidapi.get_product_string())

    @property
    def vid(self) -> int:
        assert isinstance(self._vid, int)
        return self._vid

    @property
    def pid(self) -> int:
        assert isinstance(self._pid, int)
        return self._pid

    def read(self) -> List[int]:
        return list(self._hidapi.read(1024))  # 1024 is already too much for HID data

    def write(self, data: List[int]) -> None:
        written = self._hidapi.write(data)
        if written != len(data):
            raise IOError(f'Failed to write (expected to write {len(data)} but wrote {written})')
