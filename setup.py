from setuptools import setup

setup(
    name='trecon',
    version='0.0.1',
    entry_points = {
        'console_scripts': ['trecon=trecon.trecon:main'],
    },
    
)