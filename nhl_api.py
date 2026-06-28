"""
NHL Stats API ingestion utilities.
Base URL: https://statsapi.web.nhl.com/api/v1/
"""

import requests
import pandas as pd

BASE_URL = "https://statsapi.web.nhl.com/api/v1"


def get_schedule(season: str, game_type: str = "R") -> pd.DataFrame:
    """
    Fetch schedule for a given season.
    Args:
        season: e.g. "20232024"
        game_type: "R" for regular season, "P" for playoffs
    Returns:
        DataFrame of games with game_id, date, home, away
    """
    url = f"{BASE_URL}/schedule"
    params = {"season": season, "gameType": game_type}
    response = requests.get(url, params=params)
    response.raise_for_status()
    # TODO: parse response into DataFrame
    raise NotImplementedError


def get_play_by_play(game_id: int) -> pd.DataFrame:
    """
    Fetch full play-by-play for a single game.
    Args:
        game_id: NHL game ID (e.g. 2023020001)
    Returns:
        DataFrame of events with time, type, coordinates, players
    """
    url = f"{BASE_URL}/game/{game_id}/feed/live"
    response = requests.get(url)
    response.raise_for_status()
    # TODO: parse allPlays into structured DataFrame
    raise NotImplementedError


def get_shifts(game_id: int) -> pd.DataFrame:
    """
    Fetch shift data for a game (who was on ice when).
    Args:
        game_id: NHL game ID
    Returns:
        DataFrame of shifts with player_id, team, start_time, end_time
    """
    url = f"https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId={game_id}"
    response = requests.get(url)
    response.raise_for_status()
    # TODO: parse into DataFrame
    raise NotImplementedError
