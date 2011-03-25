# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup, find_packages

import django_php_bridge
long_description = codecs.open("README.rst", "r", "utf-8").read()

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='django-php-bridge',
    version=django_php_bridge.__version__,
    description=django_php_bridge.__doc__,
    author=django_php_bridge.__author__,
    author_email=django_php_bridge.__contact__,
    url=django_php_bridge.__homepage__,
    version=version,
    long_description=long_description,
    packages=['django_php_bridge'],
    author='Wes Winham',
    author_email='winhamwr@gmail.com',
    url='http://github.com/winhamwr/django-php-bridge/',
    license='BSD',
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['phpserialize'],
)
