import sys
import warnings

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.version_info < (3, 5, 0):
    warnings.warn("The minimum Python version supported by tot is 3.5.")
    exit()

long_description = """
    Tide of Times framework to test ML.
"""

setup(
    name="tot",

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.0.1",

    description="Tide of Times framework",
    long_description=long_description,

    url="https://github.com/etibger/tot",

    # Author details
    author="Tibor Gerlai",
    author_email="tibi.gerlai@gmail.com",

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],

    # What does your project relate to?
    keywords='Tabletop game simulation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'doc': ['Sphinx', 'autodoc'],
        'test': ['pytest', 'coverage', 'coveralls', 'pytest-cov'],
    },

    # List dependencies for testing
    tests_require=['pytest', 'coverage', 'coveralls'],
)
