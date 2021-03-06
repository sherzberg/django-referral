import os
from setuptools import setup, find_packages

import referral


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-referral',
    version=referral.__version__,
    description='A small django application for marketing using referral links',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='akuryou',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-referral',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
        'factory_boy',
    ],
)
