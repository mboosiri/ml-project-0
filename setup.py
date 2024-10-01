from setuptools import find_packages, setup
from typing import List

HYPHEN_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    The function will return the module names of requirements.txt as list
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]

    if HYPHEN_E in requirements:
        requirements.remove(HYPHEN_E)

    return requirements

setup (
    name='ml-project-0',
    version='0.0.1',
    author='mb',
    author_email='boosiri007@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)