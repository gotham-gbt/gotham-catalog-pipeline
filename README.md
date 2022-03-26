# GOTHAM Catalog Pipeline

[![YAML catalog validation](https://github.com/laserkelvin/gotham-hackathon-2021/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/laserkelvin/gotham-hackathon-2021/actions/workflows/ci.yml)

This repository sets up version control and automated validation for new catalogs used in the GOTHAM collaboration.

## How to contribute

1. Fork this repository and clone it locally.
2. Install the three packages needed for this repository with `pip install -r requirements.txt` after navigating to it.
2. Make a new branch: `git checkout -b kelvin_new_catalogs`. Name `kelvin_new_catalogs` to something more descriptive for you.
3. Add the new YAML files in the standardized format as the other existing YAML files. Consult [the webpage](https://gotham-gbt.github.io/gotham-catalog-pipeline/) for the FAQ.
4. Run `pytest test.py` to validate the entries. If the tests fail, check which test failed and what the logging message is; usually it is a typo you've made in the YAML file.
  - If `test_validation_parsing` fails, there's a problem with the YAML syntax. The logger will tell you which line of the file is bad.
  - If `test_value_parsing` fails, then something that should be a floating point value cannot be converted. Usually this means you've got too many decimal points, or a negative sign was copied from LaTeX which Python doesn't recognize.
  - If `test_known_keys` fails, then you have a term that is not recognized. Run `clean_yaml.py` first to homogenize terms, particularly the quadrupole terms, and run again. If it still fails, be sure that you're using a parameter that is _actually_ correct, and doesn't already exist in the `valid_keys.txt` file that you just typo'd. In that case, run `generate_keys.py` to generate a new `valid_keys.txt` to add the entry.
5. Add the files that have been changed with `git add` and then commit them with `git commit`. Afterwards, push the changes up.
6. Make a pull request on the main repository, detailing what has been changed/added.

## Frequent problems

- One frequently encountered problem during validation is when you copy paste from LaTeX tables, which tends to mess up both the formatting and unicode characters. The __most frequent problem is the negative sign__.
