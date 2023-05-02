from libs.audio import read_audio, db_amp_change, write_audio
from libs.mpl import simple_figure


def task0211_4():
    sampling_frequency, data, max_value = read_audio('piano.wav')
    simple_figure(sampling_frequency, data, save_to_name='task0211_4_1before.png')
    inc_data = db_amp_change(data, 6)
    simple_figure(sampling_frequency, inc_data, save_to_name='task0211_4_2after.png')
    write_audio(sampling_frequency, inc_data, max_value, 'task0211_4_1.wav')


if __name__ == '__main__':
    task0211_4()
