"""
Improved goalie evaluation model.

Goals over existing GSAx:
1. Richer shot-level features beyond location (angle, type, traffic, sequence context)
2. Explicitly account for defensive structure in front of the goalie
3. Faster stabilization — target ~2-3 seasons vs current ~5 for GSAx
4. Uncertainty estimates (bootstrap confidence intervals per goalie)

Approach:
- Train an improved xG model on shot-level features (ImprovedShotModel)
- GSAx = actual goals against - sum of predicted xG against
- Use bootstrap resampling for uncertainty quantification

References:
- Moneypuck goalie methodology: https://moneypuck.com/about.htm
- Evolving Hockey GSAx: https://evolving-hockey.com/about/
- Schuckers & Curro (2013) "Total Hockey Rating (THoR)"
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.calibration import CalibratedClassifierCV
from typing import Optional


# Features for the shot-level xG model
# Richer than location-only models used in standard GSAx
SHOT_FEATURES = [
    "shot_distance",        # distance from net in feet
    "shot_angle",           # angle from center of net in degrees
    "shot_type",            # wrist, slap, snap, backhand, tip, deflection
    "is_rush",              # was the shot generated off a rush? (binary)
    "is_rebound",           # is this a rebound attempt? (binary)
    "traffic",              # traffic in front of net (from tracking data if available)
    "score_state",          # score differential bucket at time of shot
    "strength_state",       # 5v5, PP, PK, etc.
    "time_since_last_event",# seconds since last play event (pace proxy)
    "last_event_type",      # what happened immediately before the shot
    "zone_entry_type",      # did the zone entry precede this? carry-in vs dump-in
]


class ImprovedShotModel:
    """
    Shot-level xG model with richer contextual features.
    Uses gradient boosting + isotonic calibration for well-calibrated probabilities.
    """

    def __init__(self):
        base = GradientBoostingClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=4,
            subsample=0.8,
            random_state=42
        )
        # Isotonic calibration corrects probability estimates
        self.model = CalibratedClassifierCV(base, cv=5, method="isotonic")
        self.feature_names_ = SHOT_FEATURES
        self.is_fitted_ = False

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "ImprovedShotModel":
        """
        Train the shot model.
        Args:
            X: Shot-level feature DataFrame
            y: Binary target — 1 if shot was a goal, 0 otherwise
        """
        self.model.fit(X[self.feature_names_], y)
        self.is_fitted_ = True
        return self

    def predict_xg(self, X: pd.DataFrame) -> np.ndarray:
        """Return predicted goal probability for each shot."""
        if not self.is_fitted_:
            raise RuntimeError("Model not fitted yet.")
        return self.model.predict_proba(X[self.feature_names_])[:, 1]


class GoalieEvaluator:
    """
    Compute GSAx-equivalent metric using ImprovedShotModel.
    Also produces bootstrap uncertainty estimates.
    """

    def __init__(self, shot_model: ImprovedShotModel):
        self.shot_model = shot_model

    def compute_gsax(
        self,
        shots_against: pd.DataFrame,
        min_shots: int = 500,
        n_bootstrap: int = 200
    ) -> pd.DataFrame:
        """
        Compute goals saved above expected per goalie per season.

        Args:
            shots_against: Shot-level DataFrame — must include:
                           goalie_id, season, goal (binary), + SHOT_FEATURES
            min_shots: Minimum shots faced to include goalie in output
            n_bootstrap: Number of bootstrap iterations for CI estimation

        Returns:
            DataFrame with columns:
                goalie_id, season, gsax, xg_against, goals_against,
                shots_faced, gsax_lower_95, gsax_upper_95
        """
        # TODO: implement
        # Steps:
        # 1. shots_against["xg"] = self.shot_model.predict_xg(shots_against)
        # 2. Group by goalie_id, season
        # 3. gsax = xg_against.sum() - goals_against.sum()
        # 4. Filter by min_shots
        # 5. Bootstrap resample to get CIs
        raise NotImplementedError
