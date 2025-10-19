# Importing necessary libraries
import os
from pathlib import Path
import logging

# Setting up basic logging configuration
# level=logging.INFO → shows informational messages
# format → includes timestamp and message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining project name
project_name = "mlProject"

# List of all files and folders to be created for the project
list_of_files = [
    ".github/workflows/.gitkeep",                  # Placeholder for GitHub workflows
    f"src/{project_name}/__init__.py",             # Makes 'src/mlProject' a package
    f"src/{project_name}/components/__init__.py",  # Package for ML components
    f"src/{project_name}/utils/__init__.py",       # Package for utility functions
    f"src/{project_name}/utils/common.py",         # Common utility file
    f"src/{project_name}/config/__init__.py",      # Package for config handling
    f"src/{project_name}/config/configuration.py", # Configuration handling file
    f"src/{project_name}/pipeline/__init__.py",    # Pipeline-related package
    f"src/{project_name}/entity/__init__.py",      # Entity-related package
    f"src/{project_name}/entity/config_entity.py", # Entity configuration file
    f"src/{project_name}/constants/__init__.py",   # Constants package
    "config/config.yaml",                          # Configuration YAML file
    "params.yaml",                                 # Parameters file
    "schema.yaml",                                 # Schema definition
    "main.py",                                     # Main execution script
    "app.py",                                      # Flask/FastAPI entry point
    "Dockerfile",                                  # Docker configuration
    "requirements.txt",                            # Dependencies
    "setup.py",                                    # Project setup script
    "research/trials.ipynb",                       # Jupyter notebook for experiments
    "templates/index.html",                        # HTML template for web app
    "test.py"                                      # Test file
]

# Looping through all files in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object for easier path handling
    filedir, filename = os.path.split(filepath)  # Split directory and filename

    # If directory part exists, create it (if not already present)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories recursively
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create the file if it does not exist OR if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and is not empty, log that info
    else:
        logging.info(f"{filename} is already exists")
