# Reproducibility notes

## What is reproducible

The following components are reproducible from the files included in this repository:

- OFI dimension scoring from the simulated raw dataset;
- baseline equal-weight OFI calculation;
- OFI ranking;
- weighting-sensitivity analysis;
- repository visualizations;
- reported OFI-DEA comparison table using the available reported DEA scores.

## What is verified

The scripts compare computed OFI and sensitivity outputs against reference tables transcribed from the accessible revised manuscript materials. Verification files are written to:

```text
outputs/verification_ofi.json
outputs/verification_sensitivity.json
outputs/verification_dea_comparison.json
```

## What is not reproducible from available materials

The DEA efficiency scores are not independently reproducible here because the conversation materials did not include the DEA input/output matrix. The repository therefore does not present an independently estimated DEA model.

## How to rerun

Run:

```bash
python scripts/run_all.py
```

from the repository root.

## Software environment

The project uses Python with pandas, numpy, and matplotlib. Dependencies are listed in `requirements.txt`.
