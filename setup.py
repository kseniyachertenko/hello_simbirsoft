from setuptools import setup, find_packages
from os.path import join, dirname
import hellosimbirsoft

setup(
    name = 'hellosimbirsoft',
    version = hellosimbirsoft.__version__,
    packages = find_packages(),
    long_description = open(join(dirname(__file__), 'README.md')).read(),
    install_requires = [
    	'termcolor==1.1.0'
	],
	entry_points = {
    	'console_scripts': [
            'hellosimbirsoft = hellosimbirsoft.main:getMessage',
        ]
    }
)