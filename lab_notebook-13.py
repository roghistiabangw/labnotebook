# === Stage 13: Быстрые фильтры ===
# Project: LabNotebook
from datetime import datetime, date


def _today():
    return date.today()


def _start_of_week(today):
    monday = today - timedelta(days=today.weekday())
    return monday


def is_today(experiment):
    return experiment["date"] == _today()


def is_this_week(experiment):
    start = _start_of_week(_today())
    return start <= experiment["date"] <= _today()


def is_overdue(experiment):
    return experiment["date"] < _today()


def filter_experiments(experiments, mode):
    """Return experiments matching one of the fast filters.

    mode must be 'today', 'this_week', or 'overdue'.
    """
    if mode == "today":
        return [e for e in experiments if is_today(e)]
    if mode == "this_week":
        return [e for e in experiments if is_this_week(e)]
    if mode == "overdue":
        return [e for e in experiments if is_overdue(e)]
    return []


def apply_fast_filters(experiments):
    """Return a dict of all three fast-filter results."""
    return {
        "today": [e for e in experiments if is_today(e)],
        "this_week": [e for e in experiments if is_this_week(e)],
        "overdue": [e for e in experiments if is_overdue(e)],
    }
