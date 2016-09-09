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

# sys.path.append is used for this specific build to give
# access to the resources normally in the GitHub directory
# See: debian/install for a file listing.

if sys.platform.startswith('linux'):

    install_requires += [
        'dbus-python',   # requires libdbus-glib-1-dev
        'secretstorage',
    ]

setup(
    name='humblebundle',
    description='API to mananage your HumbleBundle library',
    long_description=open('README.md').read(),
    version='0.0.0',
    url='https://github.com/MestreLion/humblebundle',
    packages=find_packages('humblebundle', exclude='.gitignore'),
    include_package_data=True,
    package_data={'humblebundle': ['hooks/*', 'installers/*', '*json*', '*py*', 'makeinstall']}
    setup_requires=['setuptools-git'],
    console=[ os.path.join('humblebundle.py') ],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'humblebundle = humblebundle:cli',
        ],
    },
)
