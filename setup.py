'''
Setup.py is a special Python script that tells Python how to build, install, and 
distribute your project as a package.

The setup.py file is an essential part of packing and distributing Python Projects.
It is used by setuptools(or distutils in older Oython Version) to define the configuration of your project,
such as its metadata,dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
        """
        This function will return List of requirement

        """
        try:
                with open('requirement.txt','r') as file:
                        #Read lines from file
                        lines=file.readlines()
                        ## process each line 
                        for line in lines:
                                requirement=line.strip()
                                ##ignore empty lines and -e .
                                if requirement and requirement!= '-e .':
                                        requirement_lst.append(requirement)
        except FileNotFoundError:
                print("requirements.txt file not found")

print(get_requirements())                                        

