# mypy-dataklasses
[![python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://python.org)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

---

A MyPy plugin for [dataklases](https://github.com/dabeaz/dataklasses).

## Installation
```bash
pip install mypy-dataklasses
```

## Usage
Enable plugin in mypy configuration. [MyPy Docs](https://mypy.readthedocs.io/en/stable/extending_mypy.html#configuring-mypy-to-use-plugins).
```ini
[mypy]
plugins = mypy_dataklasses.plugin
```

## Local Development
### Running tests
1. Install [tox](https://tox.wiki/)
2. Run tox - `tox`
