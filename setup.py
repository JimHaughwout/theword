from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='theword',
    author='Jim Haughwout',
    author_email='haughwout@alum.mit.edu',
    description='Inspired by `import this` to answer an eternal question',
    url='https://github.com/JimHaughwout/theword',
    version='0.1',
    packages=['theword', ],
    package_dir={'theword':'theword'},
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta'
    ],
