import setuptools

with open("README.md", "r", encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "mlproject2"
AUTHOR_USER_NAME = "nlsrikanth7"
SRC_REPO = "mlproject2"
AUTHOR_EMAIL = "nlsrikanth@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL, 
    description = 'A small python package for CNN app',
    long_description= long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where = "src")


)

# import os
# from setuptools import find_packages, setup
# from typing import List

# HYPEN_E_DOT = '-e .'

# def get_requirements(file_path:str)->List[str]:     # this function will return the list of requirements
#     requirements =[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements

# setup(
# name = 'cnnClassifier',
# version = '0.0.1',
# author ='nlsrikanth7',
# author_email= 'nlsrikanth@gmail.com',
# packages = find_packages(),
# # install_requires = ['pandas', 'numpy', 'seaborn']
# install_requires = get_requirements('requirements.txt')

# )