# setup.py
from setuptools import setup, find_packages

setup(
    name='chikku',
    version='0.3.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'google-generativeai',
    ],
    entry_points={
        'console_scripts': [
            'chikku = chikku.chikku:main',
        ],
    },
)
