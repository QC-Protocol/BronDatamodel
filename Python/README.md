# Installation

Create a virtual environment with the tool of your choice, but here we use `virtualenv` and `pip`. Installing the `pybron` package is straightforward:

```
python -m venv .venv
. ./venv/bin/activate
pip install .
```

The second may depends on your operating system, check the [documentation](https://docs.python.org/3/library/venv.html) for details

# Usage

In the activated venv you can now use the package for reading bron formatted files.
The basic usage is:

```
from pybron.bronv3 import loadbronv3
data = loadbronv3("../../ExampleData/2024-09-16b Testdata Provincie Utrecht (export).bron2")
```

Viewing the GLD data for example:
```
data.GLD[0].Adm
data.GLD[0].Source[1].Measurements
```

All the fields of model can be found in `pybron.schema.BRONTypes.py`
