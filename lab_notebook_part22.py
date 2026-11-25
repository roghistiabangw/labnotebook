# === Stage 22: Недельный отчёт ===
# Project: LabNotebook
def weekly_report(experiments, measurements):
    """Weekly report as a text table over experiments and measurements.

    experiments: list of dicts with 'name', 'sample', 'date', 'owner'.
    measurements: list of dicts with 'experiment', 'value', 'unit'.
    """
    if not experiments:
        return "No experiments in this week."

    headers = ["#", "Experiment", "Sample", "Date", "Owner"]
    rows = []
    for idx, exp in enumerate(experiments, start=1):
        rows.append([
            str(idx),
            exp.get("name", ""),
            exp.get("sample", ""),
            exp.get("date", ""),
            exp.get("owner", ""),
        ])

    meas_by_exp = {}
    for meas in measurements:
        meas_by_exp.setdefault(meas.get("experiment", ""), []).append(meas)

    for row in rows:
        exp_name = row[1]
        cells = list(row)
        for meas in meas_by_exp.get(exp_name, []):
            cells.append(f"{meas.get('value', '')} {meas.get('unit', '')}".strip())
        row.extend(cells)
        rows.append(row)

    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def fmt(cells):
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells))

    lines = [fmt(headers), "-" * sum(widths) + "--"]
    for row in rows:
        lines.append(fmt(row))
    return "\n".join(lines)


def build_weekly_report(experiments, measurements):
    """Build a weekly report string, grouping measurements by experiment."""
    return weekly_report(experiments, measurements)


if __name__ == "__main__":
    data = [
        {"name": "pH test", "sample": "A", "date": "2024-06-03", "owner": "Ana"},
        {"name": "pH test", "sample": "B", "date": "2024-06-03", "owner": "Ana"},
        {"name": "Viscosity", "sample": "C", "date": "2024-06-04", "owner": "Ben"},
    ]
    readings = [
        {"experiment": "pH test", "value": 7.2, "unit": "pH"},
        {"experiment": "pH test", "value": 6.8, "unit": "pH"},
        {"experiment": "Viscosity", "value": 1200, "unit": "cP"},
    ]
    print(build_weekly_report(data, readings))
