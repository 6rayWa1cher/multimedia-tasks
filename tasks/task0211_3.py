from libs.audio import read_audio


def task0211_3():
    sampling_frequency, data = read_audio('piano.wav')
    print(data[50000:50010])


if __name__ == '__main__':
    task0211_3()
