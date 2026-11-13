# F4Enix hands-on workshop

A training on [F4Enix](https://f4enix.readthedocs.io/en/latest/): a Python API to read,
build and post-process MCNP models.

The training consists of five notebooks in [`notebooks/`](notebooks).

Everything runs **offline**. You never need to run MCNP, and you do not need a nuclear data
library (`xsdir`) installed: all the MCNP files used during the session are already in
[`data/`](data), and F4Enix ships with a default set of nuclear data.

## Agenda

| # | Notebook | Topic | Time |
|---|----------|-------|------|
| 00 | `00_setup_and_python_refresher.ipynb` | Check your install, minimum Python/pandas needed | ~5 min |
| 01 | `01_reading_and_editing_an_mcnp_input.ipynb` | Read a model, inspect cells/surfaces, carve out a sub-model, merge universes | ~30 min |
| 02 | `02_materials_tallies_and_run_settings.ipynb` | Materials, library translation, densities, tallies, NPS, void check | ~30 min |
| 03 | `03_parsing_outp_and_mctal.ipynb` | Is the run trustworthy? Warnings, tables, statistical checks, lost particles, tally results | ~30 min |
| 04 | `04_mesh_tallies_and_weight_windows.ipynb` | Mesh tallies to VTK, merging and transforming meshes, weight windows and GVR | ~30 min |
| 05 | `05_fispact_activation_studies.ipynb` | FISPACT activation: spectrum, collapse/condense and inventory inputs; dose, decay heat, activity and pathways from the output | ~25 min |
| 06 | `06_d1suned_study.ipynb` | set up a complete d1suned study | ~45 min |

Many of the notebooks ends with one or two exercises. Solutions are in [`solutions/`](solutions) —
try the exercise first!

Have a look also at the [F4Enix introduction](F4Enix_introduction.html) slides to get a feeling on why you should learn how to use F4Enix.

## Setup

You need Python 3.11+, the ``f4enix`` and the ``ipykernel`` package.

```powershell
# create and activate an environment (conda example)
conda create -n f4enix_workshop python=3.12
conda activate f4enix_workshop

# install the requirements
pip install f4enix ipykernel
```

Then check everything is in place:

```powershell
python check_setup.py
```

You should see a version number for F4Enix and `ALL CHECKS PASSED`.

Now you are ready to move to the [first notebook](notebooks/00_setup_and_python_refresher.ipynb).

## Troubleshooting

**`ModuleNotFoundError: No module named 'f4enix'`**
The notebook is using a different kernel than the environment you installed into.
In Jupyter: *Kernel ▸ Change Kernel* and pick the `f4enix_workshop` environment.

**`FileNotFoundError` on a file in `data/`**
Start Jupyter from the `f4enix_workshop` folder. The notebooks use paths relative to their own
location (`../data`), so they must be opened from `notebooks/`.

**A 3-D plot window opens and the notebook hangs**
Close the PyVista window. The notebook resumes immediately.

**Nothing appears when plotting**
Make sure `%matplotlib inline` (present in the first cell of each notebook) has been executed.

## Useful links

* [F4Enix documentation](https://f4enix.readthedocs.io/en/latest/)
* [F4Enix API reference](https://f4enix.readthedocs.io/en/latest/api.html)
* [F4Enix on GitHub](https://github.com/Fusion4Energy/F4Enix)
