# SPDX-License-Identifier: MIT

import threading

import pytest

import hidabc


class DummyInterface():
    def __init__(self):
        self._data = []

    @property
    def name(self):  # pragma: no cover
        return 'dummy device'

    @property
    def vid(self):  # pragma: no cover
        return 0x0000

    @property
    def pid(self):  # pragma: no cover
        return 0x0000

    def read(self):  # pragma: no cover
        return self._data

    def write(self, data):  # pragma: no cover
        assert isinstance(data, list)
        self._data = data


@pytest.fixture()
def device():
    return hidabc.Device(DummyInterface())


def test_lock(device):
    def write_ff(device, done):
        with device as interface:
            interface.write([0xff])
        done.set()

    done = threading.Event()
    task = threading.Thread(target=write_ff, args=[device, done])

    with device as interface:
        task.start()
        interface.write([0x01])
        assert interface.read() == [0x01]

    done.wait()
    task.join()

    with device as interface:
        assert interface.read() == [0xff]
