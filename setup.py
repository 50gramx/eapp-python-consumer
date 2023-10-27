import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# NOTE: DO NOT EDIT ANYTHING TILL LINE NO 10
setup(
    name='eapp_python_consumer',
    version='0.0.1',
    author='Amit Khetan',
    author_email='amit.khetan.70@50gramx.io',
    description='A python project to provide ethos core capability consumption for all the python consumers.',
    package_dir={'': 'src/eapp_python_consumer'},
    packages=find_packages(where='src/eapp_python_consumer'),
    install_requires=['protobuf==3.14.0', 'grpcio==1.34.0', 'grpcio-tools==1.34.0', 'ethos', 'PyYAML~=6.0.1'],
    include_package_data=True
)
