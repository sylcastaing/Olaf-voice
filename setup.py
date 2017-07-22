from setuptools import setup

from setuptools import setup, find_packages

setup(
  name='Olaf-voice',
  version='1.0',
  description='Voice assistant',
  author='Sylvain Castaing',
  author_email='castaing.sylvain@gmail.com',
  packages=find_packages(include=['olaf']),
  include_package_data=True,
  install_requires=['apiai', 'requests'],
)