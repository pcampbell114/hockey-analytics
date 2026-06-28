"""
Regularized Adjusted Plus-Minus (RAPM) for hockey skaters.

Methodology:
- Build a design matrix where each row is a "stint" (continuous period
  with the same players on ice) and columns are player indicator variables
  (+1 for home player, -1 for away player)
- Target variable: goals or xG differential during the stint
- Ridge regression regularizes toward zero (average player)
- Coefficients become player ratings adjusted for teammates/opponents

References:
- Macdonald (2011) "A Regression-Based Adjusted Plus-Minus Statistic for NHL Players"
  https://doi.org/10.2202/1559-0410.1323
- Gramacy, Jensen & Taddy (2013) "Estimating Player Contribution in Hockey with Regularization"
  https://doi.org/10.1515/jqas-2012-0001
- Evolving Hockey WAR methodology: https://evolving-hockey.com/about/
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from scipy.sparse import csr_matrix
from typing import Tuple


class HockeyRAPM:
    """
    Ridge-regression based Adjusted Plus-Minus for NHL skaters.

    Target variable options:
    - "goal_differential": most direct, but noisiest
    - "xg_differential": more stable, recommended starting point
    - "corsi_differential": largest sample, least direct
    """

    def __init__(self, alpha: float = 2500.0, target: str = "xg_differential"):
        """
        Args:
            alpha: Ridge regularization strength. Higher = more shrinkage toward 0.
                   Typical hockey values: 1000-5000 depending on target variable.
            target: Column name for the regression target in the stints DataFrame.
        """
        self.alpha = alpha
        self.target = target
        self.model = Ridge(alpha=alpha, fit_intercept=False)
        self.player_index_ = None
        self.ratings_ = None

    def build_design_matrix(
        self,
        stints: pd.DataFrame,
        home_cols: list,
        away_cols: list
    ) -> Tuple[csr_matrix, np.ndarray]:
        """
        Build sparse design matrix from stint data.
        Each row = one stint.
        Columns = player indicators: +1 if home team player, -1 if away team player.

        Args:
            stints: DataFrame where each row is a stint with player ID columns
            home_cols: Column names containing home team player IDs
            away_cols: Column names containing away team player IDs

        Returns:
            X: sparse design matrix (n_stints x n_players)
            y: target variable array
        """
        # TODO: implement sparse matrix construction
        # Steps:
        # 1. Collect all unique player IDs
        # 2. Map player IDs to column indices
        # 3. For each stint, set +1 for home players, -1 for away players
        # 4. Weight rows by stint duration (in seconds or minutes)
        raise NotImplementedError

    def fit(self, stints: pd.DataFrame) -> "HockeyRAPM":
        """
        Fit RAPM model on stint data.

        Args:
            stints: DataFrame with player columns and target column
        Returns:
            self
        """
        # TODO: call build_design_matrix, then self.model.fit(X, y)
        raise NotImplementedError

    def get_ratings(self) -> pd.DataFrame:
        """Return player ratings sorted by rating descending."""
        if self.ratings_ is None:
            raise RuntimeError("Model not fitted yet. Call fit() first.")
        return self.ratings_.sort_values("rating", ascending=False)
