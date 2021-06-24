# SPDX-License-Identifier: MIT

import os
import threading

import ioctl.hidraw
import pytest
import uhid


def find_hidraw(device: uhid.UHIDDevice) -> ioctl.hidraw.Hidraw:
    visited = set()

    while True:
        for node in os.listdir('/dev'):
            if node in visited:  # pragma: no cover
                continue

            visited.update([node])
            if node.startswith('hidraw'):
                path = f'/dev/{node}'
                if device.unique_name == ioctl.hidraw.Hidraw(path).uniq:
                    return path


@pytest.fixture
def vendor_rdesc():
    return [
        # Vendor page report descriptor
        0x06, 0x00, 0xff,   # Usage Page (Vendor Page)
        0x09, 0x00,         # Usage (Vendor Usage 0)
        0xa1, 0x01,         # Collection (Application)
        0x85, 0x20,	        # .Report ID (0x20)
        0x75, 0x08,	        # .Report Size (8)
        0x95, 0x08,	        # .Report Count (8)
        0x15, 0x00,	        # .Logical Minimum (0)
        0x26, 0xff, 0x00,   # .Logical Maximum (255)
        0x09, 0x00,	        # .Usage (Vendor Usage 0)
        0x81, 0x00,	        # .Input (Data,Arr,Abs)
        0x09, 0x00,	        # .Usage (Vendor Usage 0)
        0x91, 0x00,	        # .Outpur (Data,Arr,Abs)
        0xc0,               # End Collection
    ]


@pytest.fixture()
def uhid_device(vendor_rdesc):
    device = uhid.UHIDDevice(0x4321, 0x1234, 'test device', vendor_rdesc, backend=uhid.PolledBlockingUHID)
    device.wait_for_start()

    stop_dispatch = threading.Event()
    dispatch_thread = threading.Thread(target=device.dispatch, args=(stop_dispatch,))
    dispatch_thread.start()

    try:
        yield device
    finally:
        stop_dispatch.set()
        device.destroy()


@pytest.fixture()
def uhid_device_hidraw(uhid_device):
    return find_hidraw(uhid_device)
