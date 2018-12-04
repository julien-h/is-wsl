from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='iswsl',
    version='1.0.1',
    packages=['iswsl'],
    url='https://github.com/julien-h/is-wsl',
    license='MIT',
    author='Julien Harbulot',
    author_email='julien.harbulot@epfl.ch',
    description='Python utility to check whether the current script runs inside Windows\' WSL',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
