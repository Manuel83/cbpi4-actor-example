

from setuptools import setup, find_packages

setup(name='CBPiActor1',
      version='4.0.3',
      description='CraftBeerPi Actor Example',
      author='Manuel Fritsch',
      author_email='manuel@craftbeerpi.com',
      url='http://web.craftbeerpi.com',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi-actor': ['*.txt', '*.rst', '*.yaml']},
      packages=['cbpi-actor'],
     )



