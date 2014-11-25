#!/usr/bin/env python

from setuptools import setup

setup(name='plumbing-ucd-server',
      version='0.11',
      description='A simple Flask-based HTTP pony to lookup Unicode character names for a string.',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-ucd-server',
      requires=[
      ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-unicode/tarball/master#egg=cooperhewitt.unicode-0.11',
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/tarball/master#egg=cooperhewitt.flask-0.35',
      ],
      install_requires=[
          'cooperhewitt.unicode',
          'cooperhewitt.flask',
      ],
      packages=[],
      scripts=[
          'scripts/ucd-server.py',
      ],
      download_url='https://github.com/cooperhewitt/plumbing-ucd-server/tarball/master#egg=plumbing-ucd-server-0.11',
      license='BSD')
