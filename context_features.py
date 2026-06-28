"""
Contextual feature engineering for player evaluation.

Key context variables to encode:
- Score state (leading, tied, trailing)
- Zone starts (offensive/defensive/neutral zone faceoff)
- Game strength (5v5, PP, PK, 4v4, 3v3)
- Quality of competition (opponent ratings)
- Quality of teammates (linemate ratings)
"""

import pandas as pd
import numpy as np


def encode_score_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode score differential into buckets.
    Buckets: trailing 2+, trailing 1, tied, leading 1, leading 2+
    Players behave very differently when trailing vs leading (score effects).
    """
    raise NotImplementedError


def encode_zone_starts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute offensive zone start % (OZS%) per player per season.
    Players with high OZS% have easier time generating offense — must adjust for this.
    """
    raise NotImplementedError


def encode_strength_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode game strength: 5v5, 5v4 (PP), 4v5 (PK), 4v4, 3v3, etc.
    Most evaluation focuses on 5v5 to isolate even-strength play.
    """
    raise NotImplementedError


def compute_quality_of_competition(
    shifts: pd.DataFrame,
    player_ratings: pd.DataFrame
) -> pd.DataFrame:
    """
    For each player, compute the average rating of opponents faced.
    Requires an existing rating estimate (iterative process in RAPM).
    """
    raise NotImplementedError
