from pathlib import Path


def get_figures_path(*args):
    return Path('figures', *args)


def get_resources_path(*args):
    return Path('resources', *args)


def get_output_resources_path(*args):
    return Path('output_resources', *args)
