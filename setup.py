from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='luigi_completion',
      use_scm_version=True,
      setup_requires=["setuptools_scm"],
      description='completion for luigi on bash, zsh',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      author='vaaaaanquish',
      author_email='6syun9@gmail.com',
      url='https://github.com/vaaaaanquish/luigi_completion',
      packages=find_packages(),
      platforms='any',
      classifiers=['Programming Language :: Python :: 3.6'],
      entry_points={"console_scripts": ["mklcomp = luigi_completion.make_luigi_completion:main"]})

print('\n-------------------------------------------------\n')
print('  [Please set your shell]')
print('    bash:https://github.com/vaaaaanquish/luigi_completion/blob/master/luigi_completion/luigi_completion.bash')
print('    zsh:https://github.com/vaaaaanquish/luigi_completion/blob/master/luigi_completion/luigi_completion.zsh')
print('\n-------------------------------------------------\n')
