import os

import numpy as np

DELIMETER = "@@"


class DelimetedFile:
    """Class that represents a delimeted file. This class contains utilities
    for reading, writing, and handling the delimeted file.
    """

    def __init__(self, path, overwrite=False):
        """Initialize the DelimetedFile.
        :param path: file path to read/write from.
        :param overwrite: flag to overwrite pre-existing data in the filepath or
            not. Setting this to true will reset the file and any data will
            be lost.
        """
        assert os.path.isfile, "Input a valid file path."
        self.path = path
        self._lst = []

        if os.path.exists(path) and not overwrite:
            with open(path, "r") as f:
                txt = f.read()
                self._lst = txt.split(DELIMETER)

    def write(self):
        """Write any data stored in the object to disk."""
        with open(self.path, "w") as f:
            txt = DELIMETER.join(self._lst)
            f.write(txt)

    def add(self, lst):
        """Add a list of strings to the existing data stored int he object.
        :param lst: list of strings to add to the object.
        """
        self._lst.extend(lst)

    @property
    def lst(self):
        """Return a copy of the stored data in the object."""
        return np.copy(self._lst)
