"""Execute every workshop notebook to check that it still runs end to end.

Trainer tool, not part of the exercises. From the workshop root:

    pytest test_workshop_notebooks.py

The student notebooks contain unsolved exercises, so only their cells up to the
first exercise are meaningful; the solution notebooks are executed in full.
"""

from __future__ import annotations

from pathlib import Path

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = Path(__file__).resolve().parent

SOLUTIONS = sorted((ROOT / "solutions").glob("*.ipynb"))
STANDALONE = [ROOT / "notebooks" / "00_setup_and_python_refresher.ipynb"]
ALL_NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb")) + SOLUTIONS


def _execute(path: Path) -> None:
    nb = nbformat.read(path, as_version=4)
    ep = ExecutePreprocessor(kernel_name="python3", timeout=900)
    ep.preprocess(nb, {"metadata": {"path": str(path.parent)}})


@pytest.mark.parametrize("path", ALL_NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_is_valid(path: Path) -> None:
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    assert nb.cells, f"{path.name} has no cells"


@pytest.mark.parametrize("path", STANDALONE + SOLUTIONS, ids=lambda p: p.name)
def test_notebook_runs(path: Path) -> None:
    _execute(path)
