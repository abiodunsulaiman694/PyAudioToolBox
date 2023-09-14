from setuptools import setup, find_packages

setup(
    name='pyaudiotoolbox',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pydub',
        'moviepy'
    ],
)
