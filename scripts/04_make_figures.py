"""Generate repository figures from reproducible outputs.

These figures are repository visualizations produced from the simulated OFI
outputs. They are not claimed to be journal production figures.
"""
from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_OFI = ROOT / "outputs" / "final_tables" / "table_ofi_results.csv"
TABLE_SENS = ROOT / "outputs" / "final_tables" / "table_sensitivity_results.csv"
TABLE_DEA = ROOT / "outputs" / "final_tables" / "table_dea_comparison_reported_scores.csv"
FIG_DIR = ROOT / "outputs" / "figures"


def save_ofi_ranking() -> None:
    df = pd.read_csv(TABLE_OFI).sort_values("OFI")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(df["Hospital"], df["OFI"])
    ax.set_xlabel("Operational Flexibility Index (OFI)")
    ax.set_ylabel("Hypothetical hospital")
    ax.set_title("OFI ranking for simulated hospitals")
    ax.set_xlim(0, 1)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ofi_ranking_simulated_hospitals.png", dpi=300)
    plt.close(fig)


def save_sensitivity_profile() -> None:
    df = pd.read_csv(TABLE_SENS)
    x = range(len(df))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x, df["OFI_equal_weights"], marker="o", label="Equal weights")
    ax.plot(x, df["OFI_resource_allocation_weights"], marker="o", label="Resource-allocation weights")
    ax.plot(x, df["OFI_cost_pressure_weights"], marker="o", label="Cost-pressure weights")
    ax.set_xticks(list(x))
    ax.set_xticklabels(df["Hospital"], rotation=45)
    ax.set_ylabel("OFI score")
    ax.set_xlabel("Hypothetical hospital ordered by baseline OFI")
    ax.set_title("OFI sensitivity under alternative weighting assumptions")
    ax.set_ylim(0, 1)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ofi_weighting_sensitivity.png", dpi=300)
    plt.close(fig)


def save_dea_scatter() -> None:
    df = pd.read_csv(TABLE_DEA)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(df["OFI_computed_full_precision"], df["VRS_DEA_score_reported"])
    ax.set_xlabel("OFI")
    ax.set_ylabel("Reported illustrative VRS DEA score")
    ax.set_title("OFI and reported VRS DEA scores\ninterpret cautiously because of tied DEA values")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ofi_vs_reported_vrs_dea.png", dpi=300)
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    save_ofi_ranking()
    save_sensitivity_profile()
    save_dea_scatter()
    print("Figures saved to", FIG_DIR)


if __name__ == "__main__":
    main()
