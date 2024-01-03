from setuptools import find_packages, setup
from typing import List
DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    function to get the list of packages 
    in requirement.txt
    '''
    requirements = []

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [i.replace('\n','')for i in requirements]

        if DOT_E in requirements:
            requirements.remove(DOT_E)
    return requirements

setup(
    name='electronic_store_analysis',
    version='0.0.1',
    author='ST',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)