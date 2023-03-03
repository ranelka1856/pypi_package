import setuptools


with open('readme.md') as file:
    read_me_desc = file.read()

setuptools.setup(
    name='hamster_calculator',
    version='0.1',
    author='Ranelka',
    author_email='hamster@gmail.com',
    description='Calculator for hamsters',
    long_description=read_me_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/ranelka1856/pypi_package',
    packages=['hamster_calculator'],
    #install_requires=['logging'],
    python_requires='>=3.6',
)