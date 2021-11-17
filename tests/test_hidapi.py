# SPDX-License-Identifier: MIT

import time

import hidabc.hidapi


def test_properties(uhid_device, uhid_device_hidraw, vendor_rdesc):
    interface = hidabc.hidapi.HidapiInterface(uhid_device_hidraw)

    assert interface.name == 'test device'
    assert interface.phys_name == f'UHIDDevice/{interface.uniq_name}'
    assert interface.bus == 0x03
    assert interface.vid == 0x4321
    assert interface.pid == 0x1234
    assert interface.report_descriptor == vendor_rdesc


def test_write(uhid_device, uhid_device_hidraw):
    interface = hidabc.hidraw.HidrawInterface(uhid_device_hidraw)

    data = [0, 1, 2, 3, 4, 5, 6, 7]
    received = []

    def receive_output(data, report_type):
        received.append(data)

    uhid_device.receive_output = receive_output

    interface.write(data)
    interface.write(list(reversed(data)))

    time.sleep(0.1)  # give some time for the events to be dispatched

    assert received == [data, list(reversed(data))]
