from setuptools import find_packages, setup

setup(name='decomp',
      version='2.0.0a1',
      description='Toolkit for working with Universal\
                   Decompositional Semantics graphs',
      url='https://decomp.io/',
      author='Aaron Steven White',
      author_email='aaron.white@rochester.edu',
      license='MIT',
      packages=find_packages(),
      package_dir={'decomp': 'decomp'},
      package_data={'decomp': ['data/*']},
      install_requires=['requests==2.22.0',
                        'networkx==2.2',
                        'memoized_property==1.0.3',
                        'overrides==3.1.0',
                        'typing==3.6.2',
                        'rdflib==4.2.2',
                        'setuptools==41.0.1',
                        'numpy==1.16.4',
                        'pyparsing==2.2.0',
                        'predpatt @ http://github.com/hltcoe/PredPatt/tarball/master#egg=predpatt'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
