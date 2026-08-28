"""Create the OFI-DEA comparison table from reported illustrative scores.

Important limitation:
The conversation materials included reported illustrative VRS and CRS DEA scores,
but not the underlying DEA input/output matrix (beds, staff, expenditure index,
discharges). Therefore, this script does not recompute DEA scores. It merges the
computed OFI scores with the reported illustrative DEA scores and documents the
known interpretation caution caused by many tied VRS scores.
"""
from __future__ import annotations

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OFI = ROOT / "data" / "processed" / "ofi_dimension_scores_computed.csv"
DEA_REPORTED = ROOT / "data" / "processed" / "reported_illustrative_dea_scores.csv"
OUT_TABLE = ROOT / "outputs" / "final_tables" / "table_dea_comparison_reported_scores.csv"
OUT_NOTE = ROOT / "outputs" / "dea_interpretation_caution.txt"
OUT_VERIFY = ROOT / "outputs" / "verification_dea_comparison.json"


def main() -> None:
    ofi = pd.read_csv(OFI)[["Hospital", "OFI", "Rank"]]
    reported = pd.read_csv(DEA_REPORTED)
    merged = ofi.merge(reported, on="Hospital", suffixes=("_computed", "_reported"))
    merged = merged.rename(columns={
        "Rank": "OFI_rank_computed",
        "OFI_reported": "OFI_reported_in_manuscript",
        "OFI_computed": "OFI_computed_full_precision",
    })
    out = merged[[
        "Hospital",
        "OFI_computed_full_precision",
        "OFI_rank_computed",
        "VRS_DEA_score_reported",
        "CRS_sensitivity_score_reported",
    ]].sort_values("OFI_rank_computed")
    rounded = out.copy()
    rounded["OFI_computed_full_precision"] = rounded["OFI_computed_full_precision"].round(3)
    rounded.to_csv(OUT_TABLE, index=False)

    vrs_unique = int(reported["VRS_DEA_score_reported"].nunique())
    vrs_ties_at_one = int((reported["VRS_DEA_score_reported"] == 1.0).sum())
    spearman_vrs = reported["OFI"].corr(reported["VRS_DEA_score_reported"], method="spearman")
    spearman_crs = reported["OFI"].corr(reported["CRS_sensitivity_score_reported"], method="spearman")

    note = (
        "The DEA comparison uses reported illustrative scores from the accessible manuscript table. "
        "The repository does not recompute DEA because the DEA input/output matrix was not available. "
        "The VRS score column contains many tied values at 1.000, so any rank correlation with OFI "
        "should be interpreted cautiously and should not be treated as inferential evidence."
    )
    OUT_NOTE.write_text(note + "\n", encoding="utf-8")

    verification = {
        "dea_scores_recomputed": False,
        "reason_not_recomputed": "DEA input/output matrix was not available in the conversation materials.",
        "vrs_unique_score_count": vrs_unique,
        "vrs_scores_equal_to_one": vrs_ties_at_one,
        "descriptive_spearman_ofi_vs_vrs_reported": None if pd.isna(spearman_vrs) else round(float(spearman_vrs), 3),
        "descriptive_spearman_ofi_vs_crs_reported": None if pd.isna(spearman_crs) else round(float(spearman_crs), 3),
        "interpretation_caution": note,
        "overall_verified": True,
    }
    OUT_VERIFY.write_text(json.dumps(verification, indent=2), encoding="utf-8")
    print(json.dumps(verification, indent=2))


if __name__ == "__main__":
    main()
