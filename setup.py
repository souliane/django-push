# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from distutils.core import setup
from setuptools import find_packages


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='django-push',
    version=__import__('django_push').__version__,
    author='Bruno Renié',
    author_email='bruno@renie.fr',
    url='https://github.com/brutasse/django-push',
    license='BSD',
    description='PubSubHubbub (PuSH) support for Django',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='runtests.runtests',
    zip_safe=False,
)
