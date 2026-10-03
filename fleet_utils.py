# fleet_utils.py
# Shared helpers for fleet calculations.
# Dead code removed; km-to-miles constant corrected (was accidentally the inverse).

MILES_PER_KM: float = 0.621371


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a number as a whole-number percentage string."""
    return f"{int(value)}%"
