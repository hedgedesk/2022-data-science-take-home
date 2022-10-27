# !/usr/bin/env python

from setuptools import setup

import re, os


def find_packages_cust(path):
    ret = []
    for root, dirs, files in os.walk(path):
        if '__init__.py' in files:
            ret.append(re.sub('^[^A-z0-9_]+', '', root.replace('/', '.')))

    return ret


requirements_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'requirements.txt')
install_requires = open(requirements_file).read().splitlines()
print(install_requires)
setup(name='src',
      version='0.0.1',
      package_dir={'src': './src'},
      install_requires=install_requires,
      author='Victor Andrean',
      author_email='victor@pangea.io',
      url='',
      packages=find_packages_cust('./src/'),
      include_package_data=True,
      classifiers=['Programming Language :: Python :: 3.8']
      )