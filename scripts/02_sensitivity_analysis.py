"""Run OFI weighting sensitivity analysis.

The weighting schemes reproduce the sensitivity table available in the revised
manuscript materials:
- equal weights
- resource-allocation weights
- cost-pressure weights
"""
from __future__ import annotations

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DIMS = ROOT / "data" / "processed" / "ofi_dimension_scores_computed.csv"
REPORTED = ROOT / "data" / "processed" / "ofi_sensitivity_reported.csv"
OUT_TABLE = ROOT / "outputs" / "final_tables" / "table_sensitivity_results.csv"
OUT_VERIFY = ROOT / "outputs" / "verification_sensitivity.json"

DIMENSIONS = [
    "Bed_capacity",
    "Patient_flow",
    "Workforce",
    "Demand_absorption",
    "Cost_adaptability",
]

WEIGHTING_SCHEMES = {
    "OFI_equal_weights": {
        "Bed_capacity": 0.20,
        "Patient_flow": 0.20,
        "Workforce": 0.20,
        "Demand_absorption": 0.20,
        "Cost_adaptability": 0.20,
    },
    "OFI_resource_allocation_weights": {
        "Bed_capacity": 0.25,
        "Patient_flow": 0.25,
        "Workforce": 0.20,
        "Demand_absorption": 0.15,
        "Cost_adaptability": 0.15,
    },
    "OFI_cost_pressure_weights": {
        "Bed_capacity": 0.15,
        "Patient_flow": 0.15,
        "Workforce": 0.15,
        "Demand_absorption": 0.20,
        "Cost_adaptability": 0.35,
    },
}


def weighted_score(df: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    total = sum(weights.values())
    if abs(total - 1.0) > 1e-9:
        raise ValueError(f"Weights must sum to 1. Current sum: {total}")
    score = 0
    for col, weight in weights.items():
        score = score + weight * df[col]
    return score


def main() -> None:
    dims = pd.read_csv(DIMS)
    result = pd.DataFrame({"Hospital": dims["Hospital"]})
    for name, weights in WEIGHTING_SCHEMES.items():
        result[name] = weighted_score(dims, weights)
    result = result.sort_values("OFI_equal_weights", ascending=False).reset_index(drop=True)

    # Descriptive Spearman correlations across the three illustrative weighting schemes.
    corr_resource = result["OFI_equal_weights"].corr(result["OFI_resource_allocation_weights"], method="spearman")
    corr_cost = result["OFI_equal_weights"].corr(result["OFI_cost_pressure_weights"], method="spearman")

    rounded = result.copy()
    for col in rounded.columns[1:]:
        rounded[col] = rounded[col].round(3)
    rounded.to_csv(OUT_TABLE, index=False)

    reported = pd.read_csv(REPORTED)
    merged = rounded.merge(reported, on="Hospital", suffixes=("_computed", "_reported"))
    cols = ["OFI_equal_weights", "OFI_resource_allocation_weights", "OFI_cost_pressure_weights"]
    checks = {}
    all_within = True
    for col in cols:
        diff = (merged[f"{col}_computed"] - merged[f"{col}_reported"]).abs()
        checks[col] = {"max_abs_diff_rounded": float(diff.max()), "within_tolerance": bool((diff <= 0.001).all())}
        all_within = all_within and bool((diff <= 0.001).all())

    verification = {
        "weighting_schemes": WEIGHTING_SCHEMES,
        "spearman_equal_vs_resource_allocation": round(float(corr_resource), 3),
        "spearman_equal_vs_cost_pressure": round(float(corr_cost), 3),
        "checks": checks,
        "overall_verified": bool(all_within),
        "note": "Spearman correlations are descriptive for the weighting-sensitivity illustration, not inferential evidence.",
    }
    OUT_VERIFY.write_text(json.dumps(verification, indent=2), encoding="utf-8")
    print(json.dumps(verification, indent=2))


if __name__ == "__main__":
    main()
