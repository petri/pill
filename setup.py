from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='pill',
      version=version,
      description="Plonish extensions to Twill",
      long_description="added verbs",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='twill testing plone zope',
      author='Petri Savolainen',
      author_email='petri.savolainen@iki.fi',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
