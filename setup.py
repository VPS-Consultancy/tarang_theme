# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in tarang_theme/__init__.py
from tarang_theme import __version__ as version

setup(
	name='tarang_theme',
	version=version,
	description='Web Application UI',
	author='VPS Consultancy',
	author_email='vivekchamp84@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
