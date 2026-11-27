# === Stage 26: Текстовая гистограмма ===
# Project: LabNotebook
def render_date_histogram(records, width=60):
    if not records:
        return ""

    dates = [record["date"] for record in records]
    if not dates:
        return ""

    years = sorted({date.year for date in dates})
    if not years:
        return ""

    buckets = {year: [] for year in years}
    for date in dates:
        buckets[date.year].append(date)

    max_count = max(len(items) for items in buckets.values())
    if max_count == 0:
        return ""

    lines = []
    for year in years:
        items = buckets[year]
        count = len(items)
        bar = "#" * (int(round(width * count / max_count)))
        lines.append(f"{year}: {bar} ({count})")

    return "\n".join(lines)
