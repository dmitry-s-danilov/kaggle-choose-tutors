from sys import prefix
from pathlib import Path

data_path = Path(prefix) / 'data'

data_files = dict(
    train='train.csv',
    test='test.csv',
    submission_example='submission_example.csv',
)

data_paths = {
    data_key: data_path / data_file
    for data_key, data_file in data_files.items()
}
