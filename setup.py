# -*- coding: UTF-8 -*-
from setuptools import setup


setup(
    name='FlaskSQL',
    version='1.0.0',
    url='https://github.com/jzhong00/FlaskSQL/',
    license='MIT',
    author='Jason Zhong',
    author_email='jasonyzhong06@gmail.com',
    description='MySQL integration for Flask',
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'PyMySQL'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
