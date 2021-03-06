from setuptools import setup
import os

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path).read().strip()

setup(name='pypersist',
      version=read("VERSION"),
      description='Persistent memoisation framework for Python',
      url='https://github.com/mtorpey/pypersist',
      author='Michael Torpey',
      author_email='mct25@st-andrews.ac.uk',
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
      ],
      license='GPL',
      packages=['pypersist'],
      install_requires=['requests'],
      include_package_data=True,
      long_description=read('README.md'),
      zip_safe=False)
