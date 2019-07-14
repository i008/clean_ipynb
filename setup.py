#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.MD') as readme_file:
    readme = readme_file.read()

requirements = ['jupytext','importanize','autoflake']

setup_requirements = ['jupytext','importanize','autoflake', 'autopep8']


test_requirements = []

setup(
    author="Jakub Cieslik",
    author_email='kubacieslik@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Cleanup imports in jupyter notebooks",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='cleanipynb',
    name='cleanipynb',
    packages=find_packages(include=['clean_ipynb']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/i008/clean_ipynb',
    version='0.4.2',
    zip_safe=False,
    entry_points={
        "console_scripts": ["clean_ipynb = clean_ipynb.clean_ipynb:main",
                            "cleanipynb = clean_ipynb.clean_ipynb:main"],

    }
)
