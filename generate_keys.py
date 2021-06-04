
from ruamel.yaml import YAML
from pathlib import Path
from clean_yaml import homogenize_key

keys = list()
yaml = YAML()
for yml_path in Path("data").rglob("*.yml"):
    with open(yml_path, "r") as yml:
        data = yaml.load(yml)
        temp = [homogenize_key(key) for key in data.keys()]
    keys.extend(temp)

# return a unique list
keys = list(set(keys))
keys = sorted(keys)

with open("valid_keys.txt", "w+") as write_file:
    write_file.write("\n".join(keys))

