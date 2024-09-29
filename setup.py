from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    #returns list of requirements

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.1.0', # Initial version
    url='https://github.com/TomaIjatomi/mlopsproject',
    author='Toma',
    packages=find_packages(), # Automatically find packages in the project directory
    install_requires=get_requirements('requirements.txt') # List project dependencies
)