from scipy.io import loadmat
from scipy.io.wavfile import read, write
import numpy as np

from libs.path import get_resources_path, get_output_resources_path, get_ext


def get_quantization_bit_depth(data):
    return 8 * data.itemsize


def get_sampling_interval(sampling_frequency):
    return 1 / sampling_frequency


def get_data_length_in_seconds(sampling_frequency, data):
    return data.size / sampling_frequency


def get_seconds_axis(sampling_frequency, data):
    step = get_sampling_interval(sampling_frequency)
    stop = get_data_length_in_seconds(sampling_frequency, data)
    return np.arange(start=0, step=step, stop=stop)


def get_max_abs_possible_value(data):
    quantization_bit_depth = get_quantization_bit_depth(data)
    return 2 ** (quantization_bit_depth - 1)


def normalize_data(data):
    max_value = get_max_abs_possible_value(data)
    return data / max_value, max_value


def clip_data(data):
    return np.clip(data, -1, 1)


def denormalize_data(data, max_value):
    clipped_data = clip_data(data)
    new_type = ({
        32768: np.int16
    })[max_value]
    return (clipped_data * max_value).astype(new_type)


def load_wav_file(filename):
    sampling_frequency, data = read(get_resources_path(filename))
    normalized_data, max_value = normalize_data(data)
    return sampling_frequency, normalized_data, max_value


def load_mat_file_raw(filename):
    return loadmat(filename, squeeze_me=True, struct_as_record=False)


def load_mat_file(filename, fields):
    mat = load_mat_file_raw(filename)
    out = dict()
    max_value = None
    for field in fields:
        outer_data = mat[field]
        if not hasattr(outer_data, '_fieldnames'):
            # raise ValueError(f"can't load {field} from mat file {filename}: no _fieldnames")
            out[field] = outer_data
        else:
            for name in outer_data._fieldnames:
                inner_data = getattr(outer_data, name)
                normalized_data, max_value_inner = normalize_data(inner_data)
                max_value = max_value or max_value_inner
                if max_value != max_value_inner:
                    raise ValueError(f"can't load {field} from mat file {filename}: "
                                     f"invalid max_value {max_value_inner}, expected {max_value}")
                out[f"{field}.{name}"] = normalized_data
    return out, max_value


def read_audio(filename):
    return load_wav_file(get_resources_path(filename))


def convert_to_db(ratio_data):
    return 20 * np.log10(np.abs(ratio_data))


def convert_to_ratio(db_data):
    return 10 ** (db_data / 20)


def db_amp_change(data, db_change):
    db_data = convert_to_db(data)
    db_data += db_change
    return np.sign(data) * convert_to_ratio(db_data)


def write_audio(sampling_frequency, data, max_value, filename):
    denormalized_data = denormalize_data(data, max_value)
    write(get_output_resources_path(filename), sampling_frequency, denormalized_data)
