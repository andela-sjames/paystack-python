"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='paystack-python',
    version='1.2.0b1',
    long_description=long_description,
    url='https://github.com/andela-sjames/paystack-python',

    # Author details
    author='author',
    author_email='pypa-dev@googlegroups.com',

    license='GNU GENERAL PUBLIC LICENSE',

    keywords='paystack python library',

    classifiers=[
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['requests'],

    extras_require={
        'test': ['coverage'],
    },

)
