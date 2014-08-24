import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now
# 1) we have a top level README file
# 2) it's easier to type in the README file than to put a raw string in below


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    author="Kunal Tyagi",
    author_email="ktyagi@live.in",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ],
    description=("An set of tools to allow python ROS files setup and test easily."),
    keywords = "example documentation tutorial test ROS",
    license = "GNUPLv3",
    long_description=read('README.md'),
    name="test_framework",
    packages=['test_package', 'tests'],
    test_suite = 'nose.collector',
    version="0.0.1",
    url = "http://github.com/kunaltyagi/test_framework",
)
