""" Utility file for bazel runfiles.
"""
import os

from bazel_tools.tools.python.runfiles import runfiles

WORKSPACE_NAME = 'mede101'


def runfile_location(path):
    """ Returns the runfile location of the file. To use this function, 
    the file must be included in the bazel build rules data deps section.
    Example usage:
    
    py_binary(
        name = "hello_world",
        srcs = ["hello_world.py"],
        deps = [foo.py],
        data = [data.txt],
    )
    
    Then access the file using runfile_location('data.txt').
     
    Args:
        path: string path to access.
    Returns:
        string path of runfile.
    """
    r = runfiles.Create()
    return r.Rlocation(os.path.join(WORKSPACE_NAME, path))
