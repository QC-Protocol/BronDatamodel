This readme assumes a command line with "Python" as the working directory.

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

# Tests

To run the tests or any other development work, install the `pybron` package with the `dev` dependencies:"

```
pip install -e .[dev]
```

Running the tests is then straigth forward:

```
pytest
```

All tests should pass. A change to the excel sheets that define the schema can cause issues, as the tests look for field names.

# Generate schemas

To generate an update of the pydantic schemas:
```
generate_bron_schemas pybron/schema
```

Make sure all tests all after (re)generating the schemas. If the schemas change it may be necessary to update the tests.

After an succesfull schema update commit the generated `BRON*.py` files for future convienence. Also do a version bump as this is likely to require change in software using this package.

