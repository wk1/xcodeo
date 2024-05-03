from setuptools import setup, find_packages

setup(
    name='xcodeo',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'inquirer==3.2.4',  # Ensure the correct version is specified
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'xcodeo=xcodeo.main:main',
        ],
    },
)
