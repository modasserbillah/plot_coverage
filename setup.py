#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'beautifulsoup4==4.9.1', 'html5lib==1.1', 'pandas==1.0.5', 'plotly==4.8.1', 'lxml==4.5.1']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Modasser Billah",
    author_email='imtishad@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python package to generate plots from coverage report",
    entry_points={
        'console_scripts': [
            'plot_coverage=plot_coverage.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='plot_coverage',
    name='plot_coverage',
    packages=find_packages(include=['plot_coverage', 'plot_coverage.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/modasserbillah/plot_coverage',
    version='0.1.8',
    zip_safe=False,
)
