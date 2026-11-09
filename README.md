# F4Enix hands-on workshop

A roughly 2.5 hours training on [F4Enix](https://f4enix.readthedocs.io/en/latest/): a Python API to read,
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
| 04 | `04_mesh_tallies_plots_and_weight_windows.ipynb` | Mesh tallies to VTK, slice plots, Word atlas, weight windows and GVR | ~30 min |
| 05 | `05_fispact_activation_studies.ipynb` | FISPACT activation: spectrum, collapse/condense and inventory inputs; dose, decay heat, activity and pathways from the output | ~25 min |

Each notebook ends with one or two exercises. Solutions are in [`solutions/`](solutions) —
try the exercise first!

## The case study

All the notebooks work on the **same model**: `ITER_1D`, a simplified 1-D cylindrical
representation of the ITER tokamak. You will follow it through a realistic workflow:

```
ITER_1D.i  ──(01, 02)──►  modified input  ──(MCNP, already run for you)──►  outp / mctal / meshtal
                                                                                │
                                                                       (03, 04) ▼
                                                             QA report, spectra, VTK, atlas, GVR
                                                                                │
                                                                          (05)  ▼
                                                        FISPACT inputs, dose, decay heat, pathways
```

A couple of side files (a tiny sphere model, a CuV mesh tally, an output full of lost particles,
a FISPACT-II output) are used where the ITER_1D model does not show a given feature.

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

## Folder layout

```
f4enix_workshop/
  data/                 MCNP files used by the notebooks (read-only, do not edit)
    iter_1d/            the main case study: input, outp, mctal, meshtal, geometry STL
    sphere/             tiny model used for the universe/merge demo
    ww/                 an existing weight window file
    extra/              side files: CuV mesh, transformed mesh, lost-particle output
    fispact/            a FISPACT fluxes file, a FISPACT input and a FISPACT-II output
  notebooks/            the five workshop notebooks (+ notebook 00)
  solutions/            worked solutions to the exercises
  outputs/              everything the notebooks write ends up here
  check_setup.py        pre-flight check
  requirements.txt      Python dependencies
```

`outputs/` starts empty. You can delete its contents at any time and re-run the notebooks.

## Conventions used in the notebooks

* Every notebook is **independent**: it re-loads what it needs, so you can join late or redo
  one notebook without the others.
* Cells that would open a blocking 3-D window (`.plot()`) are **commented out**. Uncomment them
  only if you want to explore interactively — close the window to let the notebook continue.
* Exercises are marked **EXERCISE** and contain `# TODO` lines. The cell right after each
  exercise contains `assert` statements that tell you whether your answer is correct.

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
