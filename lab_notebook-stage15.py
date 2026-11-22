# === Stage 15: Слияние записей ===
# Project: LabNotebook
from collections import defaultdict


def merge_experiments(experiments, fields):
    """Merge two experiment records, choosing a winner for each field.

    Args:
        experiments: iterable of experiment records (dicts).
        fields: iterable of field names to merge.

    Returns:
        A new record containing the merged values. For each field, the
        value from the first experiment wins unless it is empty or missing,
        in which case the second experiment's value is used.

    Raises:
        ValueError: if fewer than two experiment records are provided.
    """
    list_experiments = list(experiments)
    if len(list_experiments) < 2:
        raise ValueError("merge_experiments requires at least two experiment records")

    record = {}
    for field in fields:
        first_value = list_experiments[0].get(field)
        second_value = list_experiments[1].get(field)
        if first_value is None or first_value == "":
            record[field] = second_value
        else:
            record[field] = first_value
    return record


def merge_all_experiments(experiments, fields):
    """Merge a collection of experiment records into a single record.

    For each field, the first non-empty value across the records wins.

    Args:
        experiments: iterable of experiment records (dicts).
        fields: iterable of field names to merge.

    Returns:
        A new record containing the merged values.

    Raises:
        ValueError: if no experiment records are provided.
    """
    list_experiments = list(experiments)
    if not list_experiments:
        raise ValueError("merge_all_experiments requires at least one experiment record")

    winners = defaultdict(str)
    for record in list_experiments:
        for field in fields:
            value = record.get(field)
            if value is not None and value != "":
                winners[field] = value
    return dict(winners)
