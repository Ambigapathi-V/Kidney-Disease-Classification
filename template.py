import os 
from pathlib import Path
import logging

# Set up logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'cnn-Classifier'

list_of_files = [
    'github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trainls.ipynb',
    'app.py',
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    
    # Check if the directory exists
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    # Check if the file already exists
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        logging.info(f"Creating file: {file_path}")
        with open(file_path, 'w') as f:
            pass
            logging.info(f"File {file_path} created successfully.")