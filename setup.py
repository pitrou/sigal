# -*- coding:utf-8 -*-

import os
from setuptools import setup

with open('README.rst') as f:
    README = f.read()

with open('docs/changelog.rst') as f:
    CHANGELOG = f.read()

# Load package meta from the pkgmeta module without loading the package.
pkgmeta = {}
pkgmeta_file = os.path.join(os.path.dirname(__file__), 'sigal', 'pkgmeta.py')
with open(pkgmeta_file) as f:
    code = compile(f.read(), 'pkgmeta.py', 'exec')
    exec(code, pkgmeta)

setup(
    name='sigal',
    version=pkgmeta['__version__'],
    url=pkgmeta['__url__'],
    license='MIT',
    author=pkgmeta['__author__'],
    author_email='contact@saimon.org',
    description='Simple static gallery generator',
    long_description=README + '\n' + CHANGELOG,
    packages=['sigal'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['blinker', 'click', 'jinja2', 'Markdown', 'Pillow',
                      'pilkit'],
    test_requires=['pytest'],
    extras_require={'CSS':  ['cssmin']},
    entry_points={
        'console_scripts': ['sigal = sigal:main']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
