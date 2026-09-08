"""Pre-flight check for the F4Enix workshop.

Run it from the workshop root:

    python check_setup.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

EXPECTED_DATA = [
    "iter_1d/ITER_1D.i",
    "iter_1d/outp",
    "iter_1d/mctal",
    "iter_1d/meshtal",
    "iter_1d/iter1D.stl",
    "sphere/Sphere.i",
    "sphere/filler.i",
    "ww/ww_simple_cart",
    "extra/meshtal_cuv",
    "extra/meshtal_transform",
    "extra/transforms.i",
    "extra/test_lp_u.o",
    "extra/test_lp_u.i",
    "fispact/FLUXESS1",
    "fispact/inp_fispact.i",
    "fispact/testSS.out",
]

REQUIRED_MODULES = [
    "f4enix",
    "numpy",
    "pandas",
    "matplotlib",
    "pyvista",
]

# Only needed by notebooks 03, 04 and 05; a missing one is a warning, not a failure.
OPTIONAL_MODULES = {
    "openpyxl": "writing the QA report to .xlsx (notebook 03)",
    "docx": "building the Word atlas (notebook 04)",
    "pypact": "reading FISPACT-II output files (notebook 05)",
}


def _ok(msg: str) -> None:
    print(f"  [ OK ] {msg}")


def _fail(msg: str) -> None:
    print(f"  [FAIL] {msg}")


def _warn(msg: str) -> None:
    print(f"  [WARN] {msg}")


def main() -> int:
    failures = 0

    print("\nPython")
    print(f"  {sys.version}")
    if sys.version_info < (3, 11):
        _fail("Python 3.11 or newer is required")
        failures += 1
    else:
        _ok(f"version {sys.version_info.major}.{sys.version_info.minor}")

    print("\nRequired packages")
    for name in REQUIRED_MODULES:
        try:
            mod = __import__(name)
        except ImportError as exc:
            _fail(f"{name}: {exc}")
            failures += 1
            continue
        version = getattr(mod, "__version__", "?")
        _ok(f"{name} {version}")

    print("\nOptional packages")
    for name, why in OPTIONAL_MODULES.items():
        try:
            __import__(name)
        except ImportError:
            _warn(f"{name} missing - needed for {why}")
        else:
            _ok(name)

    print("\nF4Enix nuclear data (bundled, no xsdir needed)")
    try:
        from f4enix.input.libmanager import LibManager

        libman = LibManager()
        libs = libman.libraries.get("mcnp", [])
        _ok(
            f"LibManager built, default library '{libman.defaultlib}', {len(libs)} MCNP libraries"
        )
    except Exception as exc:  # noqa: BLE001 - report anything that goes wrong
        _fail(f"could not build a LibManager: {type(exc).__name__}: {exc}")
        failures += 1

    print("\nWorkshop data files")
    missing = [rel for rel in EXPECTED_DATA if not (DATA / rel).is_file()]
    for rel in missing:
        _fail(f"missing data/{rel}")
    failures += len(missing)
    if not missing:
        _ok(f"all {len(EXPECTED_DATA)} data files present")

    print("\nOutput folder")
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    probe = out / ".write_test"
    try:
        probe.write_text("ok", encoding="utf-8")
        probe.unlink()
        _ok(f"{out} is writable")
    except OSError as exc:
        _fail(f"cannot write into {out}: {exc}")
        failures += 1

    print()
    if failures:
        print(
            f"{failures} CHECK(S) FAILED - see the Troubleshooting section of README.md"
        )
        return 1
    print("ALL CHECKS PASSED - you are ready for the workshop")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
