# Generic Python Project

This template can be used as a starting point for building distributable Python packages. It includes a Makefile with targets to build a wheel and a reproducible Python virtual environment based on miniconda. To learn more about packaging in Python see the [Python Packaging User Guide](https://packaging.python.org/).

## Build

```bash
$ make
```
Running `make` in this directory will build the default target "build". The chain of dependencies for the default target includes targets that retrieve a miniconda installation script for Linux and creates a stand-alone miniconda environment with the required dependencies. The name of the miniconda environment is `miniconda3` and can be activated as normal using `source miniconda3/bin/activate` and deactivated using `conda deactivate`. The build target runs `python -m build` which collects the required files and packages in `src` and generates an install wheel under `dist`. 

To start from scratch run clean:
```bash
$ make clean
```

## Installation

After running build, you can install the default package by running

```
miniconda3/bin/python -m pip install dist/hello-0.1.0-py3-none-any.whl
```

## Testing

An example test is in `tests/test_hello.py`. This test uses `pytest` to test the `greet` function. You can read more about using `pytest` at the [PyTest Documentation](https://docs.pytest.org/). To run all tests just use:

```
miniconda3/bin/python -m pytest
```

