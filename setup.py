import os
from setuptools import setup, find_packages
import ateoto_base as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="ateoto-base",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, site, app',
    author='Matthew McCants	',
    author_email='mattmccants@gmail.com',
    url="https://github.com/Ateoto/ateoto-base",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
    ],
)
