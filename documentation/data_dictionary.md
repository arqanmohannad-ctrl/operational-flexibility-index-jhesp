# Data dictionary

## `data/raw/simulated_hospitals_ofi_data.csv`

| Variable | Type | Description | Interpretation in this illustration |
|---|---|---|---|
| `Hospital` | string | Hypothetical hospital identifier | H1-H15; no real hospital is represented |
| `BOR_percent` | numeric | Bed occupancy rate (%) | Scored against an illustrative 80% reference value |
| `ALOS` | numeric | Average length of stay | Lower values are treated as better for patient-flow adaptability in the illustration |
| `Bed_turnover` | numeric | Bed turnover | Higher values are treated as better |
| `Staff_to_bed_ratio` | numeric | Staff-to-bed ratio | Higher values are treated as better within the simulation |
| `Demand_absorption_score` | numeric | Simulated demand absorption score | Higher values are treated as better |
| `Cost_output_ratio` | numeric | Simulated cost-output ratio | Higher values are treated as better within the index logic used in the accessible manuscript table |

## `data/processed/ofi_dimension_scores_reported.csv`

Reference dimension scores and OFI values transcribed from the accessible revised manuscript materials.

## `data/processed/ofi_sensitivity_reported.csv`

Reference sensitivity-analysis outputs transcribed from the accessible revised manuscript materials.

## `data/processed/reported_illustrative_dea_scores.csv`

Reported illustrative DEA comparison scores transcribed from the accessible revised manuscript materials. These are not independently recomputed in this repository.
