import pathlib
from setuptools import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='vazha',
      version='0.2',
      description='മലയാള പൈത്തൺ',
      #   url='http://github.com/',
      author='user9747',
      author_email='padinju@gmail.com',
      license='MIT',
      long_description=README,
      long_description_content_type="text/markdown",
      packages=['vazha'],
      zip_safe=False,
      entry_points={
          'console_scripts': 'vazha=vazha.command_line:main'
      })
