"""Run the complete reproducibility workflow for this repository."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    ROOT / "scripts" / "01_construct_ofi.py",
    ROOT / "scripts" / "02_sensitivity_analysis.py",
    ROOT / "scripts" / "03_dea_comparison_from_reported_scores.py",
    ROOT / "scripts" / "04_make_figures.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n--- Running {script.name} ---")
        subprocess.run([sys.executable, str(script)], check=True, cwd=ROOT)
    print("\nWorkflow completed successfully.")


if __name__ == "__main__":
    main()
