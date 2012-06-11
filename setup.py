# Copyright 2012, BlueDynamics Alliance - http://bluedynamics.com

from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc = \
'YAFOWIL - Demo Application'
longdesc = ""

tests_require = ['interlude']

setup(name='yafowil.demo',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'License :: OSI Approved :: Python Software Foundation License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development',
      ],
      keywords='html input widgets form compound',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://github.com/bluedynamics/yafowil.demo',
      license='BSD simplified and CC-BY-SA',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['yafowil'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'setuptools',
        'Chameleon',
        'yafowil',
        'yafowil.webob',
        'yafowil.yaml',
         # add-on widgets to document
        'yafowil.widget.richtext',
        'yafowil.widget.datetime',   
        'yafowil.widget.array',
        'yafowil.widget.dict',
        'yafowil.widget.image',
        'yafowil.widget.autocomplete',
        'yafowil.widget.dynatree',
      ],
      tests_require=tests_require,
      test_suite="yafowil.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
)