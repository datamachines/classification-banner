#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='classification-banner',
      version='1.0',
      description='Classification banner compatable with GTK3 and X11.',
      author='Mike May',
      author_email='mikemay@datamachines.io',
      url='https://www.github.com/datamachines/classification-banner',
      packages=find_packages(),
      scripts=["bin/classification_banner"],
      data_files=[("classification_banner", ["style.css"])]
     )