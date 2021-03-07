import numpy as np
import pandas as pd


def read_array(path, delimiter=","):
    """Reads data from csv file into numpy array.

    Args:
        param path: File path to read from. Should be a .npy/npz.
        param delimiter: One character string to delimit the file with.
    Returns:
        Numpy array of read data.
    """
    df = pd.read_csv(path, delimiter=delimiter)
    return df.to_numpy()


def read_dataframe(path, sep=','):
    """Reads data from csv file into pandas dataframe.

    Args:
        param path: File path to read from.
        param delimiter: One character string to delimit the file with.
    Returns:
        Pandas dataframe of read data.
    """
    df = pd.read_csv(path, delimiter=delimiter)
    return df


def write_array(path, array, sep=','):
    """Writes an array to disk.

    Args:
        param path: Path to write to.
        param array: Numpy array or python list to write to disk.
        param delimiter: One character string to delimit the file with.
    """
    df = pd.DataFrame(array)
    df.to_csv(path, index=False, sep=',')


def write_dataframe(path, df, delimiter=','):
    """Writes a Pandas Dataframe to disk.

    Args:
        param path: Path to write to.
        param df: Pandas dataframe to write to.
        param delimiter: One character string to delimit the file with.
    """
    df.to_csv(path, index=False, sep=',')


def lined_file_to_array(path):
    """Reads a file split by newlines into a numpy array.

    Args:
        param path: The delimited text file to read from.
    Returns:
        Numpy array containing split data.
    """
    with open(path) as f:
        txt = f.read()
        lines = txt.splitlines()
        return np.array(lines)


def lined_file_to_df(path):
    """Reads a file split by newlines into a numpy array.

    Args:
        param path: The delimited text file to read from.
    Returns:
        Pandas dataframe containing split data.
    """
    with open(path) as f:
        txt = f.read()
        lines = txt.splitlines()
        df = pd.DataFrame(np.array(lines))
        return df
