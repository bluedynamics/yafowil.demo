from setuptools import find_packages
from setuptools import setup


version = '1.2.dev0'
shortdesc = 'YAFOWIL - Demo Application'
longdesc = ""


setup(
    name='yafowil.demo',
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
    package_dir={'': 'src'},
    namespace_packages=['yafowil'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'sphinx',
        'Chameleon',
        'docutils',
        'yafowil',
        'yafowil.webob',
        'yafowil.yaml',
        'yafowil.bootstrap',
        # add-on widgets
        # 'yafowil.widget.alohaeditor',
        'yafowil.widget.ace',
        'yafowil.widget.array',
        'yafowil.widget.autocomplete',
        'yafowil.widget.chosen',
        'yafowil.widget.cron',
        'yafowil.widget.datetime',
        'yafowil.widget.dict',
        'yafowil.widget.dynatree',
        'yafowil.widget.image',
        'yafowil.widget.location',
        'yafowil.widget.multiselect',
        'yafowil.widget.recaptcha',
        'yafowil.widget.richtext',
        'yafowil.widget.select2',
        'yafowil.widget.slider',
        'yafowil.widget.wysihtml5',
    ],
    entry_points="""
    [yafowil.plugin]
    register = yafowil.demo.loader:register
    """)
