from setuptools import find_packages,setup
from typing import List

def get_requires(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[x.replace("/n"," ") for x in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Ridha",
    author_email="ridha.ds22@duk.ac.in",
    packages=find_packages(),
    install_requires=get_requires("requirements.txt")
)