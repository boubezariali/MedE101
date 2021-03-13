import csv
import os

import numpy as np
import pandas as pd


def read_array(path, sep=','):
    """Read data from csv file into numpy array.

    Args:
        path: File path to read from. Should be a .npy/npz.
        sep: One character string to delimit the file with.
    Returns:
        Numpy array of read data.
    """
    df = pd.read_csv(path, sep=sep)
    return df.to_numpy()


def read_dataframe(path, sep=','):
    """Read data from csv file into pandas dataframe.

    Args:
        path: File path to read from.
        sep: One character string to delimit the file with.
    Returns:
        Pandas dataframe of read data.
    """
    df = pd.read_csv(path, sep=sep)
    return df


def write_array(path, array, sep=','):
    """Write an array to disk.

    Args:
        path: Path to write to.
        array: Numpy array or python list to write to disk.
        sep: One character string to delimit the file with.
    """
    df = pd.DataFrame(array)
    df.to_csv(path, index=False, sep=',')


def write_dataframe(path, df, sep=','):
    """Write a Pandas Dataframe to disk.

    Args:
        path: Path to write to.
        df: Pandas dataframe to write to.
        sep: One character string to delimit the file with.
    """
    df.to_csv(path, index=False, sep=',')


def lined_file_to_array(path):
    """Read a file split by newlines into a numpy array.

    Args:
        path: The delimited text file to read from.
    Returns:
        Numpy array containing split data.
    """
    with open(path) as f:
        txt = f.read()
        lines = txt.splitlines()
        return np.array(lines)


def lined_file_to_df(path):
    """Read a file split by newlines into a numpy array.

    Args:
        path: The delimited text file to read from.
    Returns:
        Pandas dataframe containing split data.
    """
    with open(path) as f:
        txt = f.read()
        lines = txt.splitlines()
        df = pd.DataFrame(np.array(lines))
        return df


def add_line_to_file(path, line, sep='\n'):
    """Append a single line to a file, default newline-separated

    Args:
        line: represented by 1D list or array
        path: the text file to write to
    """
    string = ','.join(str(item) for item in line) + sep
    with open(path, 'a') as f:
        f.write(string)
