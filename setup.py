from setuptools import find_packages ,setup
from typing import List

def get_requirements(file_path) -> List[str]:
    l=[]
    with open(file_path,'r') as file:
        requirements=file.readlines()
        for requirement in requirements:
            if '\n' in requirement:
                requirement=requirement.replace('\n','')
            if requirement == '-e .':
                continue
            l.append(requirement)
    return l
            

setup(
    name='mlproject1',
    version='0.0.1',
    author='Akash',
    author_email='royakash0920@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)