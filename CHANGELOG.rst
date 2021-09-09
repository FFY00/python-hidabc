+++++++++
Changelog
+++++++++


0.3.0 (10-09-2021)
==================

- Add initial Linux Hidraw implementation
- Add initial PyUSB implementation
- Add ``hidabc.Interface.transfer``
- Add ``interrupt_in`` and ``interrupt_out`` to ``hidabc.FullInterface``
- Make ``hidabc.ExtendedInterface.get_report_descriptor`` a property (``report_descriptor``)
- Fix ``hidabc.FullInterface.get_report`` and ``hidabc.FullInterface.set_report`` signatures


0.2.0 (24-06-2021)
==================

- Rename ``hidabc.Device`` to ``hidabc.Interface``
- Add ``hidabc.Device`` context manager
- Add ``hidabc.__version__``


0.1.0 (24-06-2021)
==================

- Initial release
