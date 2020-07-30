#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='scikit-sos',
      version='0.1.10',
      description='A scikit-learn compatible implementation of Stochastic Outlier Selection (SOS) for detecting outliers.',
      long_description=README,
      author='Sourangshu Ghosh',
      author_email='sourangshug123@gmail.com',
      url='https://github.com/SourangshuGhosh/Stochastic-Outlier-Selection-SOS-',
      license='MIT',
      packages=['sksos'],
      install_requires=['numpy'],
      include_package_data=True,
      zip_safe=False,
      entry_points={'console_scripts':
          ['sos=sksos.cli:main']
    }
)

