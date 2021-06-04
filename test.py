
from pathlib import Path
from loguru import logger
from ruamel.yaml import YAML


def test_validate_parsing():
    """
    This test will make sure all of the YAML files are
    parseable by the YAML loader, as well as raise warnings
    in the log when the number of keys do not match the number of
    lines in the file, excluding comments and blank lines.
    """
    yml_paths = Path("data").rglob("*.yml")
    yaml_loader = YAML()
    for path in yml_paths:
        logger.debug(f"Opening file {path}.")
        with open(path, "r") as read_file:
            data = yaml_loader.load(read_file)
            logger.debug(f"Loaded {len(data)} keys.")
            # restart at the top of the file
            read_file.seek(0)
            lines = read_file.readlines()
            # ignore comment lines and only grab key/value pairs
            lines = [line for line in lines if not line.startswith("#") and line != "\n"]
            logger.debug(f"Expected {len(lines)} entries.")
            if len(data) != len(lines):
                logger.warning(f"Number of entries does not match expected for {path.stem}")


def test_value_parsing():
    """
    This test will make sure keys that are not expected to be
    strings will be parseable as Python floats.
    """
    yml_paths = Path("data").rglob("*.yml")
    yaml_loader = YAML()
    # a list of keys expected to be strings to ignore
    text_keys = ["name", "formula", "doi", "smiles", "notes", "author"]
    for path in yml_paths:
        logger.debug(f"Opening file {path}.")
        with open(path, "r") as read_file:
            data = yaml_loader.load(read_file)
            for key, value in data.items():
                if key not in text_keys:
                    logger.debug(f"Running {key} with {value}")
                    # try and convert the value to float
                    try:
                        _ = float(value)
                    except ValueError as error:
                        raise Exception(f"Failed to parse {key} with value {value} for file {path.stem}")


def test_known_keys():
    """
    This test will check every YAML file to make sure the
    parameter keys are recognized.
    """
    yml_paths = Path("data").rglob("*.yml")
    yaml_loader = YAML()
