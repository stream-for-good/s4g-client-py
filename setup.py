#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup process."""

from io import open
from os import path

from setuptools import find_packages, setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'),
          encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Basic project information
    name='s4gpy',
    version='0.0.7',
    # Authorship and online reference
    author='Nicolas Herbaut',
    author_email='nicolas.herbaut@univ-paris1.fr',
    url='https://github.com/stream-for-good/s4g-client-py',
    # Detailled description
    description='S4G/discoverability API Wrapper.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='streaming, recommendation, science',
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    # Package configuration
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    python_requires='>= 3.7',
    install_requires=["requests~=2.25.1", "munch~=2.5.0"],
    # Licensing and copyright
    license='Apache 2.0'
)
