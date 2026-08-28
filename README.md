# Operational Flexibility Index for Public Hospitals

## Project title

**Operational Flexibility as an Economic Mechanism for Public Hospital Resource Allocation in MENA Health Systems: A Reproducible Numerical Illustration**

## Researcher

**Dr. Mohannad Mahmoud Alarqan**

## Project status

This repository documents the reproducible numerical illustration associated with the article:

> *Operational Flexibility as an Economic Mechanism for Public Hospital Resource Allocation in MENA Health Systems: Developing an Index to Assess Efficiency and Cost Implications under Uncertainty*

Based on the DergiPark status information made available in the conversation, the manuscript status is **accepted / ready for an issue** in the *Journal of Health Systems and Policies* with DOI: **10.52675/jhesp.1945352**.

This repository does **not** include the full manuscript, journal correspondence, reviewer reports, or submission-system screenshots.

## Healthcare, economic, and managerial problem

Public hospitals in MENA health systems face pressure from constrained budgets, changing demand, staffing pressure, patient-flow problems, and uneven capacity. Policy responses often focus on expanding capacity, increasing budgets, or comparing hospitals using utilization indicators. However, these responses may overlook whether existing resources can be reallocated internally when demand changes.

This project treats **operational flexibility** as an internal economic capability: the ability of a public hospital to reallocate beds, staff, patient-flow capacity, and operational resources under uncertainty.

## Project objectives

The repository demonstrates how to:

1. construct a transparent Operational Flexibility Index (OFI);
2. normalize indicators measured on different scales;
3. apply optimal-reference scoring for bed occupancy;
4. aggregate dimension scores into a composite index;
5. test sensitivity to alternative weighting assumptions;
6. interpret OFI alongside reported illustrative DEA scores without making causal claims.

## Health-economic, operational, and policy relevance

The OFI is designed as a diagnostic decision-support tool. It may help hospital managers and policymakers distinguish between:

- insufficient resources;
- inefficient use of existing resources;
- weak internal resource adaptability.

This distinction matters because each problem implies a different policy response. A capacity shortage may require investment, while weak adaptability may require improved bed management, discharge coordination, staff redeployment, scheduling, internal governance, or information systems.

## Data sources

### Data used in this repository

The analysis uses a **simulated dataset of 15 hypothetical hospitals**. The dataset is included in:

```text
data/raw/simulated_hospitals_ofi_data.csv
```

The simulated data are used only to demonstrate the OFI pipeline. They do **not** describe real hospitals, countries, patients, or health systems.

### Official sources for future empirical applications

No official empirical dataset is analyzed in this repository. Future empirical applications could draw on official and administrative sources such as:

- World Health Organization Global Health Observatory: https://www.who.int/data/gho
- World Bank Health, Nutrition and Population statistics: https://databank.worldbank.org/source/health-nutrition-and-population-statistics
- WHO Regional Office for the Eastern Mediterranean data and country profiles: https://www.emro.who.int
- National Ministry of Health statistical reports, hospital annual reports, and administrative datasets, subject to access, quality, and comparability.

## Analytical methodology

The repository implements the OFI pipeline using Python.

### Indicators in the simulated dataset

- Bed occupancy rate (BOR, %)
- Average length of stay (ALOS)
- Bed turnover
- Staff-to-bed ratio
- Demand absorption score
- Cost-output ratio

### OFI dimensions

1. Bed-capacity responsiveness
2. Patient-flow adaptability
3. Workforce-resource flexibility
4. Demand-uncertainty absorption
5. Cost-adaptability

### Normalization and scoring

- Higher-is-better indicators use min-max normalization.
- ALOS uses inverse min-max normalization because lower values are treated as better in the illustration.
- Bed occupancy uses an optimal-reference logic around 80%, because very low occupancy may indicate underuse while very high occupancy may indicate congestion.

### Weighting

The baseline OFI uses equal weights across the five dimensions. Sensitivity analysis tests:

- equal weights;
- resource-allocation weights;
- cost-pressure weights.

### DEA component

The accessible conversation materials included reported illustrative DEA scores, but did **not** include the underlying DEA input/output matrix. Therefore, this repository does **not** recompute DEA scores. It includes the reported illustrative DEA comparison table and flags the interpretation limitation caused by many tied VRS DEA scores.

## Repository structure

```text
operational-flexibility-index-jhesp/
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── CHANGELOG.md
├── REPOSITORY_AUDIT.md
├── .gitignore
├── scripts/
│   ├── 01_construct_ofi.py
│   ├── 02_sensitivity_analysis.py
│   ├── 03_dea_comparison_from_reported_scores.py
│   ├── 04_make_figures.py
│   └── run_all.py
├── data/
│   ├── raw/
│   │   └── simulated_hospitals_ofi_data.csv
│   └── processed/
│       ├── ofi_dimension_scores_reported.csv
│       ├── ofi_sensitivity_reported.csv
│       └── reported_illustrative_dea_scores.csv
├── outputs/
│   ├── final_tables/
│   └── figures/
└── documentation/
    ├── methodology.md
    ├── data_dictionary.md
    ├── data_sources.md
    ├── limitations.md
    └── reproducibility_notes.md
```

## How to reproduce the results

### 1. Clone or download the repository

```bash
git clone <repository-url>
cd operational-flexibility-index-jhesp
```

### 2. Create and activate a Python environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the complete workflow

```bash
python scripts/run_all.py
```

The workflow generates:

```text
outputs/final_tables/table_ofi_results.csv
outputs/final_tables/table_sensitivity_results.csv
outputs/final_tables/table_dea_comparison_reported_scores.csv
outputs/figures/ofi_ranking_simulated_hospitals.png
outputs/figures/ofi_weighting_sensitivity.png
outputs/figures/ofi_vs_reported_vrs_dea.png
outputs/verification_ofi.json
outputs/verification_sensitivity.json
outputs/verification_dea_comparison.json
```

## Key findings from the numerical illustration

These findings apply only to the simulated data:

- H4, H11, H13, and H8 have the highest OFI values under the baseline equal-weight specification.
- H7 and H12 remain at the lower end of the OFI distribution.
- The ranking pattern is stable under the two alternative weighting schemes used in the illustration.
- The reported illustrative DEA comparison should be interpreted cautiously because many VRS DEA scores are tied at 1.000.
- The OFI should be interpreted as a complementary diagnostic measure, not as a causal estimate and not as a substitute for technical efficiency analysis.

## Methodological and data limitations

- The dataset is simulated and does not represent real hospitals.
- The OFI has not been empirically validated using hospital-level administrative data in this repository.
- Equal weighting is a transparent baseline, not a validated final weighting model.
- Min-max normalization is sensitive to outliers.
- Bed occupancy scoring uses an 80% reference point for illustration only.
- DEA scores are reported from accessible manuscript tables but are not independently recomputed because the DEA input/output matrix was not available.
- No causal inference is attempted.
- No patient-level, confidential, or clinical quality outcome data are analyzed.

## Recommended citation

Alarqan, M. M. (2026). *Operational Flexibility Index for Public Hospitals: Reproducible Numerical Illustration* [Computer software and dataset]. GitHub. Associated article: *Operational Flexibility as an Economic Mechanism for Public Hospital Resource Allocation in MENA Health Systems: Developing an Index to Assess Efficiency and Cost Implications under Uncertainty*. Journal of Health Systems and Policies. https://doi.org/10.52675/jhesp.1945352

## License

The code is released under the MIT License. The simulated dataset is provided for reproducibility and educational use. This license does not apply to third-party data, journal materials, or publisher-owned content not included in this repository.
