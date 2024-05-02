from setuptools import setup, find_packages

setup(
    name='xcodeo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'inquirer>=2.7.0',  # Stelle sicher, dass du die richtige Version angibst
    ],
    entry_points={
        'console_scripts': [
            'xcodeo=xcodeo.main:main',  # Befehl führt `main` in `main.py` aus
        ],
    },
)