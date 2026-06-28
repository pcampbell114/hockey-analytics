# Hockey Player & Goalie Evaluation Framework

A research project to develop improved player and goalie evaluation metrics in hockey, addressing known shortcomings of existing statistics like xG and GSAx.

## Project Goals

- Build a contextually-adjusted player evaluation model (RAPM-style + ML extensions)
- Develop a goalie evaluation metric that stabilizes faster than GSAx and incorporates richer shot features
- Produce uncertainty-quantified player ratings per season
- Validate against existing metrics on year-over-year stability and team outcome prediction

## Repository Structure

```
hockey-analytics/
├── data/
│   ├── raw/              # Unmodified source data (NHL API, MoneyPuck, etc.)
│   ├── processed/        # Cleaned, feature-engineered datasets
│   └── external/         # Third-party reference data (Hockey Reference, etc.)
├── notebooks/
│   ├── 01_exploration/   # EDA, data quality checks, visualization
│   ├── 02_modeling/      # Model development and experimentation
│   └── 03_evaluation/    # Metric validation, stability analysis
├── src/
│   ├── data/             # Data ingestion and cleaning scripts
│   ├── features/         # Feature engineering pipeline
│   ├── models/           # Model definitions (RAPM, XGBoost, neural nets)
│   ├── evaluation/       # Validation, stability, and comparison utilities
│   └── visualization/    # Plotting and reporting utilities
├── reports/
│   └── figures/          # Output charts and tables
├── tests/                # Unit tests
├── docs/                 # Literature notes, methodology write-ups
├── requirements.txt
├── .gitignore
└── README.md
```

## Methodology Overview

### Skater Evaluation
1. **Baseline**: RAPM (Regularized Adjusted Plus-Minus) via ridge regression
2. **Extension**: XGBoost / neural net with richer contextual features
3. **Context controls**: zone starts, score state, strength, quality of competition/teammates

### Goalie Evaluation
1. **Baseline**: GSAx replication for benchmarking
2. **Extension**: Incorporate pre-shot sequence context, traffic, shot velocity (where available)
3. **Goal**: Faster stabilization than current GSAx (~5 seasons → target ~2–3)

### Validation Framework
- Year-over-year correlation (repeatability / signal isolation)
- Predictive validity: does the metric predict future team goal differential?
- Contract value correlation (external validation)
- Comparison to existing public metrics (Evolving Hockey WAR, MoneyPuck)

## Data Sources

| Source | What It Provides | Access |
|--------|-----------------|--------|
| NHL Stats API | Play-by-play, shifts, rosters | Free, no key |
| MoneyPuck | Shot-level data, xG, advanced stats CSVs | Free download |
| Hockey Reference | Historical stats, career data | Free (scrape carefully) |
| Evolving Hockey | WAR, RAPM, xG | Partial free |
| Stathletes Big Data Cup | Tracking data | Free (competition) |

## Setup

```bash
git clone https://github.com/yourusername/hockey-analytics.git
cd hockey-analytics
pip install -r requirements.txt
```

## References & Literature

See `docs/literature_review.md` for annotated bibliography.

## Status

🚧 Active development — pre-alpha
