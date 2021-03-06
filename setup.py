from setuptools import setup, find_packages

from version import __version__

setup(
    name='po-help',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/stan5079/po-help',
    license='GNU General Public License v3.0',
    author='Stan Mertens',
    description='A small helper repository for handling .po files.',
    python_requires='>=3.9',
    install_requires=[
        'googletrans-py==4.0.0'
    ]
)
