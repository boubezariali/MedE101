import numpy as np
import pandas as pd


def read_array(path):
    array = np.load(path)
    return array

def write_array(path, array):
   np.save(path, array) 

def delimited_file_to_df(path, delimiter=','):
    df = pd.read_csv(path, delimiter)
    return df

def delimited_file_to_array(path, delimiter=','):
    df = pd.read_csv(path, delimiter)
    return df.to_numpy()

def lined_file_to_array(path):
    with open(path) as f:
        txt = f.read()
        lines = txt.splitlines()
        return np.array(lines)


    
