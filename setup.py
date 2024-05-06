from setuptools import setup, find_packages
from xcodeo.version import __version__

setup(
    name='xcodeo',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'inquirer>=2.7.0',
    ],
    entry_points={
        'console_scripts': [
            'xcodeo=xcodeo.main:main',  # This entry point calls the main function
        ],
    },
)
