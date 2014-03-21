'''
{{cookiecutter.project}}: {{cookiecutter.description}}

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}.
Licensed under {{cookiecutter.license_name}}.
'''
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = "{{cookiecutter.version}}"

setup(name="{{cookiecutter.project}}",
      version=version,
      description="{{cookiecutter.description or ''}}",
      long_description=open("README.rst").read(),
      classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Programming Language :: Python'
      ],
      keywords="{{cookiecutter.keywords}}", # Separate with spaces
      author="{{cookiecutter.author}}",
      author_email="{{cookiecutter.author_email}}",
      url="{{cookiecutter.url}}",
      license="{{cookiecutter.license_name}}",
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe={{cookiecutter.zip_safe}},
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      
      # TODO: List of packages that this one depends upon:   
      install_requires={{cookiecutter.install_requires.split().__repr__()}},
      # TODO: List executable scripts, provided by the package (this is just an example)
      entry_points={
        'console_scripts': 
            ['{{cookiecutter.egg}}={{cookiecutter.package}}:main']
      }
)
