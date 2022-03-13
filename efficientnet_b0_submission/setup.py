#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = [
    "model-tools @ git+https://github.com/brain-score/model-tools"
]

setup(
    name='efficient_net_b0_brain_score',
    version='0.1.0',
    description="An efficient net b0 for adding brain or base model implementation",
    author="Suseendrakumar Duraivel",
    author_email='sd355@duke.edu',
    url='https://github.com/dsuseendar',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='brain-score template',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
)
