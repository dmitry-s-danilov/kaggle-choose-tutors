from sys import prefix
from pathlib import Path

directory = 'data'
files = dict(
    train='train.csv',
    test='test.csv',
    submission='submission_example.csv',
)

directory_path = Path(prefix) / directory
file_paths = {
    key: directory_path / file
    for key, file in files.items()
}
