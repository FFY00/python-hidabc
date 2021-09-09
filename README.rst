******
hidabc
******

Collection of abstract protocols to interact with HID devices.


Backend implementations
=======================

- Linux Hidraw - ``HidrawInterface``
- PyUSB (libusb/openusb) - ``PyUSBInterface``


Compatibility Table
===================

+--------------------+----------------------+----------------------+----------------------+---------------------------------+
| Interface/Platform |        Linux         |        macOS         |        Windows       | OpenBSD, NetBSD, Haiku, Solaris |
+--------------------+----------------------+----------------------+----------------------+---------------------------------+
| Interface          | ``HidrawInterface``  | ``PyUSBInterface``\* | ``PyUSBInterface``\* | ``PyUSBInterface``\*            |
|                    | ``PyUSBInterface``\* |                      |                      |                                 |
+--------------------+----------------------+----------------------+----------------------+---------------------------------+
| ExtendedInterface  | ``HidrawInterface``  | ``PyUSBInterface``\* | ``PyUSBInterface``\* | ``PyUSBInterface``\*            |
|                    | ``PyUSBInterface``\* |                      |                      |                                 |
+--------------------+----------------------+----------------------+----------------------+---------------------------------+
| FullInterface      | ``PyUSBInterface``\* | ``PyUSBInterface``\* | ``PyUSBInterface``\* | ``PyUSBInterface``\*            |
+--------------------+----------------------+----------------------+----------------------+---------------------------------+

\* Requires OS driver detach.
