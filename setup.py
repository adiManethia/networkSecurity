"""
The setup.py file is the centre of all activity in building, distributing Python projects. It is used by setup tools (or distutils in older versions)
to define the configuration of your project. It is also used to install your project, like its metadata, dependencies, and entry points.
    
"""
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements from requirements.txt file

    """
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            # Read lines from file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst

#print(get_requirements())

## setup metadata
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Adtiya",
    author_email="adigit2075.14111998@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)