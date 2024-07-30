from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    """
        This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "Machine Learning Project",
    version= "1.0.0",
    author= "Mujeeb",
    author_email= "mujeebblouch7036@gmail.com",
    package = find_packages(),
    intall_requires = get_requirements("requirements.txt")
)