import sys
import os

from distutils.core import setup
from setuptools import find_packages

install_requires = [
    'lxml',
    'progressbar',
    'keyring',
    'pyxdg',
]

if sys.platform.startswith('linux'):

    install_requires += [
        'dbus-python',   # requires libdbus-glib-1-dev
        'secretstorage',
    ]

setup(
    name='humblebundle',
    version='0.0.0',
    url='https://github.com/MestreLion/humblebundle',
    zip_safe=False
    packages=find_packages('humblebundle', exclude=['tests']),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=install_requires,
    console=[ os.path.join('humblebundle', 'humblebundle.py') ],
    entry_points={
        'console_scripts': [
            'humblebundle = humblebundle:cli',
        ],
    },
)
