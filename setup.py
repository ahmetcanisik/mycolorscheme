from setuptools import setup, find_packages

setup(
    name="mycolorscheme",
    version="0.0.6",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mycolorscheme=mycolorscheme.__main__:main',
        ],
    },
)