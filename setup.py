from setuptools import setup

from version import __version__

setup(
    name='po-help',
    version=__version__,
    packages=['po_help'],
    url='https://github.com/stan5079/po-help',
    license='GNU General Public License v3.0',
    author='Stan Mertens',
    author_email='',
    description='A small helper repository for handling .po files.',
    install_requires=[
        'googletrans==3.1.0a0'
    ]
)
