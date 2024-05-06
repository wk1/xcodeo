from setuptools import setup, find_packages

setup(
    name='xcodeo',
    version='0.0.4',
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
