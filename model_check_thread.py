"""This module is to run progressbar"""

try:
    from PySide2 import QtCore  # type: ignore
except ModuleNotFoundError:
    from PySide6 import QtCore  # type: ignore


# pylint: disable=too-few-public-methods
class ModelCheckThread(QtCore.QThread):  # type: ignore
    """
    This is a thread class for progressbar.
    """

    progress_signal = QtCore.Signal(int)

    def run(self) -> None:
        """This function progress bar signal."""
        # Do some work here
        for i in range(101):
            self.progress_signal.emit(i)
