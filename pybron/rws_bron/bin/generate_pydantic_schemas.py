"""
Created on : Tuesday, 11th June 2024 3:39:01 pm
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Tuesday, 11th June 2024 3:39:01 pm
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from pathlib import Path
from typing import Optional

import click

from rws_bron.schema_generation import generate_schemas


@click.command
@click.argument(
    "target_directory",
    type=click.Path(exists=True, file_okay=False, writable=True, path_type=Path),
    required=False,
)
def main(target_directory: Optional[Path] = None):
    generate_schemas(target_directory)


if __name__ == "__main__":
    main()
