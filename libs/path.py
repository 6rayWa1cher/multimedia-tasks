from pathlib import Path


def get_root_path():
    curr_path = Path(__file__).parent
    while curr_path.parent.exists() and not curr_path.joinpath('tasks').is_dir():
        curr_path = curr_path.parent
    return curr_path


def get_figures_path(*args):
    return Path(get_root_path(), 'figures', *args)


def get_resources_path(*args):
    return Path(get_root_path(), 'resources', *args)


def get_output_resources_path(*args):
    return Path(get_root_path(), 'output_resources', *args)


def get_filename_without_ext(filename):
    return filename[:filename.rindex('.')]


def get_ext(filename):
    return filename[filename.rindex('.') + 1:]
