import numpy as np
from scipy.io.wavfile import read, write

from libs.audio import get_seconds_axis
from libs.mpl import simple_figure
from libs.path import get_resources_path, get_output_resources_path


def task0211_2():
    sampling_frequency, data = read(get_resources_path('flute-A4.wav'))
    seconds_axis = get_seconds_axis(sampling_frequency, data)
    extracted_data = data[np.logical_and(1 <= seconds_axis, seconds_axis <= 1.2)]
    print('size before:', data.size, 'size after:', extracted_data.size)
    write(get_output_resources_path('task0211_2_test.wav'), sampling_frequency, extracted_data)
    simple_figure(sampling_frequency, extracted_data, save_to_name='task0211_2.png')


if __name__ == '__main__':
    task0211_2()
