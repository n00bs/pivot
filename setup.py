import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pivot',
    version='0.2',
    packages=['pivot'],
    include_package_data=True,
    install_requires=[
        'Django',
        'djangorestframework'
    ],
    license='Apache License, Version 2.0',  # example license
    description='Backend which implements Pivot API v2',
    long_description='Implement Pivot API v2',
    url='http://pivot.uw.edu/',
    author='Abhishek Chauhan',
    author_email='--',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
