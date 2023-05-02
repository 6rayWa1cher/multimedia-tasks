from matplotlib import pyplot as plt

from libs.audio import get_seconds_axis
from libs.path import get_figures_path


def save_figure(fig, fig_name):
    fig.savefig(get_figures_path(fig_name))


def process_common_flags(fig, show=False, save_to_name=None):
    if show:
        fig.show()
    if save_to_name:
        save_figure(fig, save_to_name)


def simple_figure(sampling_frequency, data, **kwargs):
    fig, ax = plt.subplots()
    ax.plot(get_seconds_axis(sampling_frequency, data), data)
    process_common_flags(fig, **kwargs)
    return fig, ax
