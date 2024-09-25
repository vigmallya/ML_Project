from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .' #Intialised to remove it while reading from requirements.txt file (-e . use to trigger setup.py )

def get_reguirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements] #Replacing \n, while reading the requirements line by line

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Vignesh Mallya',
    author_email='vignesh.mallya315@gmail.com',
    packages=find_packages(), #Finds all the packages present in the project files 
    install_requires=get_reguirements('requirements.txt') , #All the required packages (['pandas','numpy','seaborn']etc)
)