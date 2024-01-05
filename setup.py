from setuptools import setup, find_packages


setup(
    name='client_data',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0',
    ],
)
