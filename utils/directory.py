import os


def get_root_folder():
    basedir = os.path.abspath(os.path.dirname(__file__))
    basedir = os.path.join(basedir, os.pardir)
    basedir = os.path.abspath(basedir)
    return basedir


def get_abs_path(from_file):
    root_folder = get_root_folder()
    location = os.path.join(root_folder, from_file)
    location = os.path.abspath(location)
    return location
