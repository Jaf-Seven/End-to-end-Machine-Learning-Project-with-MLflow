# =============================
# common.py (with examples)
# =============================

import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


# ===================================================
# Function: read_yaml()
# ===================================================
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


# Example:
# Suppose params.yaml contains:
# model:
#   type: "RandomForest"
#   n_estimators: 100
# data_path: "data/train.csv"
#
# >>> cfg = read_yaml(Path("params.yaml"))
# [INFO]: YAML file: params.yaml loaded successfully
# >>> print(cfg.model.type)
# RandomForest
# >>> print(cfg.data_path)
# data/train.csv
# (Returns ConfigBox where you can access values as attributes)


# ===================================================
# Function: create_directories()
# ===================================================
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates multiple directories if they don't already exist.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


# Example:
# >>> create_directories(["artifacts", "models"])
# [INFO]: Created directory at: artifacts
# [INFO]: Created directory at: models
# (Creates folders if they don’t exist, returns None)


# ===================================================
# Function: save_json()
# ===================================================
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves data into a JSON file.
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


# Example:
# >>> data = {"accuracy": 0.95, "loss": 0.1}
# >>> save_json(Path("results.json"), data)
# [INFO]: JSON file saved at: results.json
#
# (results.json file will contain)
# {
#     "accuracy": 0.95,
#     "loss": 0.1
# }


# ===================================================
# Function: load_json()
# ===================================================
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file and returns it as a ConfigBox.
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


# Example:
# >>> cfg = load_json(Path("results.json"))
# [INFO]: JSON file loaded successfully from: results.json
# >>> print(cfg.accuracy)
# 0.95
# >>> print(cfg.loss)
# 0.1


# ===================================================
# Function: save_bin()
# ===================================================
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves Python objects (like models, datasets, etc.) in binary format using joblib.
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


# Example:
# >>> from sklearn.ensemble import RandomForestClassifier
# >>> model = RandomForestClassifier()
# >>> save_bin(model, Path("model.pkl"))
# [INFO]: Binary file saved at: model.pkl
#
# (model.pkl file is created with the serialized model)


# ===================================================
# Function: load_bin()
# ===================================================
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads binary data (previously saved with joblib).
    """

    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


# Example:
# >>> model_loaded = load_bin(Path("model.pkl"))
# [INFO]: Binary file loaded from: model.pkl
# >>> type(model_loaded)
# sklearn.ensemble._forest.RandomForestClassifier
# (Returns the same object you saved earlier)


# ===================================================
# Function: get_size()
# ===================================================
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in kilobytes (KB).
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


# Example:
# >>> print(get_size(Path("results.json")))
# ~ 1 KB
# (Returns approximate file size as string)
