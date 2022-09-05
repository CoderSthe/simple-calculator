from setuptools import setup, find_packages

setup(
    name='simple_calculator',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Simple Calculator',
    long_description=open('README.md').read(),
    url='https://github.com/CoderSthe/simple-calculator',
    author='Sithembiso Mdhluli',
    author_email='mdhluli269@gmail.com'
)