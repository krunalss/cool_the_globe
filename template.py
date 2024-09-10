import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Updated project name based on the FastAPI app structure
project_name = "app"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/static/__init__.py",
    f"{project_name}/main.py",
    f"{project_name}/routes/__init__.py",
    f"{project_name}/routes/homepage.py",
    f"{project_name}/templates/index.html",
    "pyproject.toml",
    "Dockerfile",
    "research/trials.ipynb",
    "test.py"
]

# Create the directory structure and empty files as necessary
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
