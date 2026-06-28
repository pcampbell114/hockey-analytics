"""
Metric stability and validation utilities.

Year-over-year (YoY) correlation is the primary signal test:
- High YoY r = the metric is measuring a repeatable player skill
- Low YoY r = the metric is mostly noise/luck

Key validation targets:
1. YoY correlation — does the metric repeat for the same player?
2. Predictive validity — does season T metric predict season T+1 team outcomes?
3. Contract correlation — does the metric track with market valuation (AAV)?
4. Comparison to existing public metrics (xG, GSAx, Evolving Hockey WAR)
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Tuple, List


def year_over_year_correlation(
    ratings: pd.DataFrame,
    player_col: str = "player_id",
    season_col: str = "season",
    metric_col: str = "rating",
) -> Tuple[float, float]:
    """
    Compute year-over-year Pearson r for a player metric.

    Args:
        ratings: DataFrame with one row per player per season
        player_col: Column identifying the player
        season_col: Column identifying the season
        metric_col: Column containing the metric to test

    Returns:
        (r, p_value) — Pearson correlation and p-value
    """
    df = ratings.sort_values([player_col, season_col]).copy()
    df["prev_rating"] = df.groupby(player_col)[metric_col].shift(1)
    valid = df.dropna(subset=["prev_rating"])
    r, p = stats.pearsonr(valid[metric_col], valid["prev_rating"])
    return float(r), float(p)


def stability_by_sample_size(
    ratings: pd.DataFrame,
    metric_col: str,
    sample_col: str = "toi_minutes",
    bins: int = 5
) -> pd.DataFrame:
    """
    Compute YoY stability within sample size bins.
    Useful for understanding how quickly a metric stabilizes.

    Args:
        ratings: Player-season ratings DataFrame
        metric_col: Metric to evaluate
        sample_col: Column representing sample size (e.g. TOI)
        bins: Number of sample size bins

    Returns:
        DataFrame with bin label, mean sample size, YoY r per bin
    """
    # TODO: implement
    raise NotImplementedError


def compare_metrics(
    metrics_df: pd.DataFrame,
    metric_cols: List[str],
    outcome_col: str = "team_goal_differential"
) -> pd.DataFrame:
    """
    Compare predictive validity of multiple metrics against a team outcome.

    Args:
        metrics_df: DataFrame with metrics and outcome column
        metric_cols: List of metric column names to compare
        outcome_col: Column representing the outcome to predict

    Returns:
        DataFrame sorted by r² with columns: metric, r, r_squared, p_value
    """
    results = []
    for col in metric_cols:
        valid = metrics_df[[col, outcome_col]].dropna()
        r, p = stats.pearsonr(valid[col], valid[outcome_col])
        results.append({
            "metric": col,
            "r": round(r, 4),
            "r_squared": round(r**2, 4),
            "p_value": round(p, 6),
            "n": len(valid)
        })
    return pd.DataFrame(results).sort_values("r_squared", ascending=False)


def split_half_reliability(
    events: pd.DataFrame,
    player_col: str,
    metric_fn,
    n_splits: int = 50
) -> float:
    """
    Split-half reliability test: randomly split a season's events in half,
    compute the metric on each half, correlate across players.
    Average over n_splits for a stable estimate.

    Args:
        events: Event-level DataFrame (e.g. shots, stints)
        player_col: Column identifying the player
        metric_fn: Function(events_subset) -> pd.Series indexed by player_id
        n_splits: Number of random splits

    Returns:
        Mean split-half Pearson r (Spearman-Brown corrected)
    """
    # TODO: implement
    raise NotImplementedError
