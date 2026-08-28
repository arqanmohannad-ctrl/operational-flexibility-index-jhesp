"""Construct the Operational Flexibility Index (OFI).

This script reproduces the OFI dimension scores and baseline OFI ranking from
an illustrative, simulated 15-hospital dataset. It does not use real hospital,
patient-level, or confidential data.
"""
from __future__ import annotations

from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "simulated_hospitals_ofi_data.csv"
REPORTED = ROOT / "data" / "processed" / "ofi_dimension_scores_reported.csv"
OUT_PROCESSED = ROOT / "data" / "processed" / "ofi_dimension_scores_computed.csv"
OUT_TABLE = ROOT / "outputs" / "final_tables" / "table_ofi_results.csv"
OUT_VERIFY = ROOT / "outputs" / "verification_ofi.json"


def min_max(series: pd.Series) -> pd.Series:
    """Min-max normalize so that higher values are better."""
    denominator = series.max() - series.min()
    if denominator == 0:
        return pd.Series(np.nan, index=series.index)
    return (series - series.min()) / denominator


def inverse_min_max(series: pd.Series) -> pd.Series:
    """Min-max normalize so that lower values are better."""
    return 1 - min_max(series)


def bor_optimal_score(series: pd.Series, reference: float = 80.0) -> pd.Series:
    """Score bed occupancy rate using an optimal-reference logic.

    A hospital receives the highest score when its bed occupancy rate is closest
    to the reference value. In this numerical illustration, the reference is 80%.
    Scores are scaled by the largest absolute deviation in the sample and clipped
    to the 0-1 range.
    """
    max_dev = (series - reference).abs().max()
    if max_dev == 0:
        return pd.Series(1.0, index=series.index)
    return (1 - (series - reference).abs() / max_dev).clip(lower=0, upper=1)


def construct_ofi(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate OFI dimension scores and equal-weight OFI."""
    out = pd.DataFrame({"Hospital": df["Hospital"]})
    out["Bed_capacity"] = bor_optimal_score(df["BOR_percent"])
    alos_score = inverse_min_max(df["ALOS"])
    turnover_score = min_max(df["Bed_turnover"])
    out["Patient_flow"] = (alos_score + turnover_score) / 2
    out["Workforce"] = min_max(df["Staff_to_bed_ratio"])
    out["Demand_absorption"] = min_max(df["Demand_absorption_score"])
    out["Cost_adaptability"] = min_max(df["Cost_output_ratio"])
    dimensions = [
        "Bed_capacity",
        "Patient_flow",
        "Workforce",
        "Demand_absorption",
        "Cost_adaptability",
    ]
    out["OFI"] = out[dimensions].mean(axis=1)
    out = out.sort_values("OFI", ascending=False).reset_index(drop=True)
    out["Rank"] = range(1, len(out) + 1)
    return out


def verify_against_reported(computed: pd.DataFrame) -> dict:
    """Compare rounded computed values to reported manuscript values."""
    reported = pd.read_csv(REPORTED)
    merged = computed.merge(reported, on="Hospital", suffixes=("_computed", "_reported"))
    columns = [
        "Bed_capacity",
        "Patient_flow",
        "Workforce",
        "Demand_absorption",
        "Cost_adaptability",
        "OFI",
    ]
    results = {"tolerance": 0.001, "columns_checked": columns, "checks": {}}
    max_abs_diff = 0.0
    all_within = True
    for col in columns:
        diff = (merged[f"{col}_computed"].round(3) - merged[f"{col}_reported"].round(3)).abs()
        max_diff = float(diff.max())
        within = bool((diff <= 0.001).all())
        results["checks"][col] = {"max_abs_diff_rounded": max_diff, "within_tolerance": within}
        max_abs_diff = max(max_abs_diff, max_diff)
        all_within = all_within and within
    rank_match = bool((merged["Rank_computed"] == merged["Rank_reported"]).all())
    results["rank_match"] = rank_match
    results["all_numeric_values_match_when_rounded_to_3_decimals"] = all_within
    results["overall_verified"] = bool(all_within and rank_match)
    results["max_abs_diff_rounded"] = max_abs_diff
    return results


def main() -> None:
    df = pd.read_csv(RAW)
    computed = construct_ofi(df)
    # Save full precision for audit, and rounded table for sharing.
    computed.to_csv(OUT_PROCESSED, index=False)
    rounded = computed.copy()
    for col in [c for c in rounded.columns if c != "Hospital" and c != "Rank"]:
        rounded[col] = rounded[col].round(3)
    rounded.to_csv(OUT_TABLE, index=False)
    verification = verify_against_reported(computed)
    OUT_VERIFY.write_text(json.dumps(verification, indent=2), encoding="utf-8")
    print(json.dumps(verification, indent=2))


if __name__ == "__main__":
    main()
