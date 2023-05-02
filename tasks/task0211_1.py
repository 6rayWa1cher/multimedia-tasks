from scipy.io.wavfile import read

from libs.mpl import simple_figure
from libs.path import get_resources_path


def task0211_1():
    sampling_frequency, data = read(get_resources_path('flute-A4.wav'))
    simple_figure(sampling_frequency, data, save_to_name='task0211_1.png')


if __name__ == '__main__':
    task0211_1()
