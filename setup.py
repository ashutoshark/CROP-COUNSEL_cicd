
#setup.py is a Python script used to build and install Python packages. 
#It contains information about the package, such as its name, version, and dependencies, 
#as well as instructions for building and installing the package. 

from setuptools import find_packages,setup
from typing import List

# this hypen is use to triger requirement.txt folder
HYPEN_E_DOT='-e.'

# this function use to fetch all lib name form requremet.txt file
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
#    this hypen has no use other wise so we need to remove form req list after fetch
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='crop_counsel',
    version='0.0.1',
    author='ashutosh',
    author_email="ashutoshark08@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)