# Methodology

## Overview

This repository implements a reproducible numerical illustration of the Operational Flexibility Index (OFI) for public hospitals. The illustration uses simulated data for 15 hypothetical hospitals and demonstrates how the index can be calculated and interpreted.

## Conceptual definition

Operational flexibility is defined here as the internal economic capability of a public hospital to reallocate beds, staff, patient-flow capacity, and operational resources under uncertainty.

## Dimensions

The OFI includes five dimensions:

1. **Bed-capacity responsiveness**: the ability to maintain balanced use of bed capacity without persistent underuse or congestion.
2. **Patient-flow adaptability**: the ability to move patients efficiently through admission, inpatient care, and discharge.
3. **Workforce-resource flexibility**: the alignment of staff resources with changing service needs.
4. **Demand-uncertainty absorption**: the ability to maintain activity under changing demand pressure.
5. **Cost-adaptability**: the ability to maintain output without disproportionate cost pressure.

## Indicator scoring

### Bed-capacity responsiveness

Bed occupancy is scored around an illustrative 80% reference value:

```text
Bed_capacity_score = 1 - abs(BOR - 80) / max(abs(BOR - 80))
```

The score is clipped to the 0-1 interval. This is an optimal-reference score, not a higher-is-better score.

### Patient-flow adaptability

Patient-flow adaptability is calculated as the average of:

- inverse min-max normalized ALOS;
- min-max normalized bed turnover.

### Workforce-resource flexibility

Workforce-resource flexibility is calculated using min-max normalized staff-to-bed ratio.

### Demand-uncertainty absorption

Demand absorption is calculated using min-max normalized demand absorption score.

### Cost-adaptability

Cost-adaptability is calculated using min-max normalized cost-output ratio in the illustrative dataset.

## Baseline OFI

The baseline OFI uses equal weights:

```text
OFI = 0.20 * Bed_capacity
    + 0.20 * Patient_flow
    + 0.20 * Workforce
    + 0.20 * Demand_absorption
    + 0.20 * Cost_adaptability
```

## Sensitivity analysis

The repository tests three weighting assumptions:

| Scheme | Bed capacity | Patient flow | Workforce | Demand absorption | Cost-adaptability |
|---|---:|---:|---:|---:|---:|
| Equal weights | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 |
| Resource-allocation weights | 0.25 | 0.25 | 0.20 | 0.15 | 0.15 |
| Cost-pressure weights | 0.15 | 0.15 | 0.15 | 0.20 | 0.35 |

## DEA comparison

The repository includes reported illustrative DEA scores from accessible manuscript tables. It does not recompute DEA because the underlying DEA input/output matrix was not available. The DEA comparison is therefore a documented reported-output comparison, not an independently estimated DEA model.

## Interpretation

The OFI is a diagnostic index. It is not a causal model, not a measure of clinical quality, and not a substitute for technical efficiency analysis.
