# Repository audit

Audit date: 2026-08-28

## Included

This repository includes a GitHub-ready reproducibility package for the Operational Flexibility Index (OFI) numerical illustration:

- `README.md` with project description, objectives, methodology, reproducibility instructions, status, and citation.
- `scripts/01_construct_ofi.py` to compute OFI dimension scores and rankings from the simulated dataset.
- `scripts/02_sensitivity_analysis.py` to reproduce the alternative weighting scenarios.
- `scripts/03_dea_comparison_from_reported_scores.py` to create the OFI-DEA comparison table from the reported illustrative DEA scores.
- `scripts/04_make_figures.py` to create repository visualizations.
- `scripts/run_all.py` to run the complete workflow.
- `data/raw/simulated_hospitals_ofi_data.csv` containing the hypothetical hospital dataset.
- `data/processed/` reference tables transcribed from accessible revised manuscript materials.
- `outputs/final_tables/` with reproducible CSV outputs.
- `outputs/figures/` with repository figures generated from the reproducible outputs.
- `documentation/` with methodology, data dictionary, data source notes, limitations, and reproducibility notes.
- `requirements.txt`, `LICENSE`, `CITATION.cff`, `.gitignore`, and `CHANGELOG.md`.
- `outputs/file_manifest_sha256.json` with file checksums.

## Excluded and why

The following materials were deliberately excluded:

- Full manuscript files: excluded to avoid sharing submitted or publisher-controlled manuscript content.
- Journal correspondence, reviewer reports, decision letters, and DergiPark screenshots: excluded because they are not necessary for reproducibility and may contain editorial or personal information.
- Submission-system links, login details, usernames, passwords, tokens, or access keys: excluded for security and privacy.
- Copyright transfer, ethics forms, conflict-of-interest forms, and other journal administrative files: excluded because they are journal-process documents, not reproducibility materials.
- Real hospital, patient, clinical, administrative, or financial datasets: none were made available for this project in a form that could be redistributed.
- DEA input/output matrix: excluded because it was not available in the conversation materials.

## Verified scripts and outputs

The full workflow was tested with:

```bash
python3 scripts/run_all.py
```

Verification results:

- `01_construct_ofi.py`: successfully reproduced the reported OFI dimension scores and rankings when rounded to three decimals. Output verification: `outputs/verification_ofi.json`.
- `02_sensitivity_analysis.py`: successfully reproduced the reported weighting-sensitivity table when rounded to three decimals. Output verification: `outputs/verification_sensitivity.json`.
- `03_dea_comparison_from_reported_scores.py`: successfully created the reported DEA comparison table and documented the limitation that DEA scores were not recomputed. Output verification: `outputs/verification_dea_comparison.json`.
- `04_make_figures.py`: successfully generated three repository figures in `outputs/figures/`.

## Important reproducibility caveat

The repository does not independently reproduce the DEA model. The accessible materials included reported VRS and CRS DEA scores, but did not include the DEA input/output matrix described in the manuscript text. Recomputing DEA from different proxy variables would have required inventing inputs or results, so it was not done.

## Materials still needed for a stronger repository

To make the repository a full independent computational supplement, the following materials would be needed:

1. The final accepted/production version of the article or final corrected table values, if they differ from the accessible revised manuscript materials.
2. The DEA input/output matrix used to create the illustrative DEA scores, including variables such as beds, staff, expenditure index, and discharges.
3. The exact final post-minor-revision response, if any table wording or DEA interpretation was changed after the accessible revised manuscript version.
4. Any original standalone analytical scripts, if they existed outside the manuscript-generation code.

## Public-sharing safety review

A text scan was performed for common sensitive patterns including email references, passwords, tokens, secrets, API keys, and private-key strings. No such content was found, except the protective pattern `secrets.*` in `.gitignore`.

The repository contains only simulated data and reproducibility code. It does not contain personal data, patient data, confidential data, journal correspondence, reviewer reports, screenshots, passwords, or manuscript files.

## Publication recommendation

The repository is technically safe to publish publicly from a data-privacy perspective. However, because the associated article has journal status "accepted / ready for an issue" and the full article page may still be in production, the recommended initial visibility is **Private**. After the article page is publicly available and publisher sharing conditions are checked, the repository can be made public as a computational supplement.
