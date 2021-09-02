from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='competition',
    version='0.0.1',

    author='Dmitry S. Danilov',
    author_email='dmitry.s.danilov@gmail.com',

    description='Choose proper tutors for math exam within the Kaggle competition',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/dmitry-s-danilov/kaggle-choose-tutors',
    project_urls={
        'Bug Tracker': 'https://github.com/dmitry-s-danilov/kaggle-choose-tutors/issues',
        'Kaggle Competition': 'https://www.kaggle.com/c/choose-tutors',
    },

    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='machine-learning, prediction-competition, python',

    license='MIT License',
    license_files=['LICENSE.txt'],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    data_files=[
        (
            'data',
            [
                'data/train.csv',
                'data/test.csv',
                'data/submission_example.csv',
            ]
        )
    ],

    python_requires=">=3.9",
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
    ],
)
