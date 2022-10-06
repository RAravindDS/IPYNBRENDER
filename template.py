import os
import logging
from pathlib import Path  # It's automatically detects your os and run!

""" 
- This will ask the project name and it will automatically create all the nesessary files for you!
"""

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s] %(message)s"
)

while True:
    project_name = input("Enter the project name: ")
    if project_name != '':
        break

logging.info(f'Creating project name: {project_name}')


# list of files
list_of_files = [
    '.github/workflows/.gitkeep',  # it helps to run certain checks
    f"src/{project_name}/__init__.py",  # src for running all the files
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integeration/__init__.py",  # testing all
    "init_setup.sh",  # it helps to create conda env setup
    "requirements.txt",
    "requirements_dev.txt",  # This is only for our testing
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",  # it will test the pypi package on various enviroment

]


for filepath in list_of_files:
    # This will take care of forward or backward slash
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":  # here we are checking the file is directory then only we are making the directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory at : {filedir} for file: {filename}")

    # if the file not exist or size of the file is 0 we are creting
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(
                f'Creating the new file: {filename} at path: {filepath}')

    else:  # if file is already there are passing it!
        logging.info(f'file is already present at : {filepath}')
