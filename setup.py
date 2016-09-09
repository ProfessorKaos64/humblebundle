import sys
import os

from distutils.core import setup
from setuptools import find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

INSTALL_REQUIRES = [
    'lxml',
    'progressbar',
    'keyring',
    'pyxdg',
]

if sys.platform.startswith('linux'):

    INSTALL_REQUIRES += [
        'dbus-python',   # requires libdbus-glib-1-dev
        'secretstorage',
    ]

setup(
    name='humblebundle',
    author='https://github.com/MestreLion',
    url='https://github.com/MestreLion/humblebundle',
    version='0.1.0',
    license='GPLv3',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    package_dir={'humblebundle': 'humblebundle'},
    package_data={'humblebundle': ['humblebundle/*']},
    setup_requires=['setuptools-git'],
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'humblebundle = humblebundle:cli',
        ],
    },
)
