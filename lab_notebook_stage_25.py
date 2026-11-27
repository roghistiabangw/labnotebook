# === Stage 25: Топ записей ===
# Project: LabNotebook
def top_n_records(records, field, n):
    """Return the top N records sorted by a numeric field in descending order.

    Args:
        records: iterable of dict-like records.
        field:   name of the numeric field to rank by.
        n:       number of top records to return.

    Returns:
        A list of records sorted from highest to lowest field value.
    """
    if n <= 0:
        return []
    return sorted(records, key=lambda rec: rec.get(field, 0), reverse=True)[:n]


def top_n_by_quantity(records, n):
    """Return the top N experiments by sample quantity.

    Example:
        >>> samples = [
        ...     {"name": "A", "quantity": 10},
        ...     {"name": "B", "quantity": 30},
        ...     {"name": "C", "quantity": 20},
        ... ]
        >>> [r["name"] for r in top_n_by_quantity(samples, 2)]
        ['B', 'C']
    """
    return top_n_records(records, "quantity", n)


def top_n_by_date(records, n):
    """Return the N most recent experiments by date.

    Dates are expected as ISO 8601 strings (e.g. "2024-05-01").

    Example:
        >>> dates = [
        ...     {"name": "A", "date": "2024-05-01"},
        ...     {"name": "B", "date": "2024-06-15"},
        ...     {"name": "C", "date": "2024-04-10"},
        ... ]
        >>> [r["name"] for r in top_n_by_date(dates, 2)]
        ['B', 'A']
    """
    return top_n_records(records, "date", n)
