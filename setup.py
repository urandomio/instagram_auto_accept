#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'docopt',
    'instagram-api'
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

github_dependencies = [
    'git+https://github.com/urandomio/Instagram-API-python.git'
]

setup(
    name='instagram_auto_accept',
    version='0.1.0',
    description="A utility for Instagram API to automatically accept new Follow Requests.",
    long_description=readme + '\n\n' + history,
    author="James Brink",
    author_email='brink.james@gmail.com',
    url='https://github.com/jamesbrink/instagram_auto_accept',
    packages=[
        'instagram_auto_accept',
    ],
    dependency_links=github_dependencies,
    package_dir={'instagram_auto_accept':
                 'instagram_auto_accept'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='instagram_auto_accept',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    scripts=['scripts/instagram_auto_accept', ],
    test_suite='tests',
    tests_require=test_requirements
)
