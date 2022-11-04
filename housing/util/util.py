import yaml
from housing.exception import HousingException
import os, sys

def read_yaml_file(file_path:str) -> dict:
    """
    Read a YAML file and returns the contents as a dictonary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e