# setup.py
from setuptools import setup, find_packages

setup(
    name='pkd-chikku',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pkd-chikku = pkd_chikku.chikku:main',
        ],
    },
)
