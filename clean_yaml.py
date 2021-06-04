
from ruamel.yaml import YAML
from pathlib import Path
from shutil import copy2

from loguru import logger

def homogenize_key(key: str) -> str:
    # replace quadrupole terms with lower case
    if "Chi" in key:
        key = key.lower()
    # now also get rid of whitespace
    key = "".join(key.split(" "))
    return key


if __name__ == "__main__":
    yaml = YAML()
    for yml_path in Path("data").rglob("*.yml"):
        logger.info(f"Opening {yml_path.stem}")
        changed = False
        with open(yml_path, "r") as read_file:
            data = yaml.load(read_file)
        new_data = data.copy()
        for key, value in data.items():
            new_key = homogenize_key(key)
            logger.debug(f"Old key: {key} - new key: {new_key}")
            if new_key not in data.keys():
                new_data[new_key] = value
                # delete the old version
                del new_data[key]
                changed = True
                logger.info(f"Homogenizing key; old: {key}, new: {new_key}")
        # make a backup of the old file
        if changed:
            logger.info(f"Saving a backup copy of {yml_path.stem} due to changes.")
            copy2(yml_path, str(yml_path) + ".bak")
            with open(yml_path, "w+") as write_file:
                write_file.write(f"# File modified after homogenizing keys")
                yaml.dump(new_data, write_file)
