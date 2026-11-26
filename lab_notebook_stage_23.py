# === Stage 23: Месячный отчёт ===
# Project: LabNotebook
from datetime import datetime

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def _month_index(month_name):
    return MONTHS.index(month_name)


def _days_in_month(year, month):
    return (
        datetime(year, month + 1, 1) - datetime(year, month, 1)
    ).days


def monthly_report(experiments, measurements, reference_month):
    """Build a monthly report with summary indicators and month-over-month comparison."""
    ref_year, ref_month = reference_month.year, reference_month.month
    current_month = datetime(ref_year, ref_month, 1)
    previous_month = current_month - datetime.timedelta(days=1)
    prev_year, prev_month = previous_month.year, previous_month.month

    def month_key(year, month):
        return (year, month)

    current_key = month_key(ref_year, ref_month)
    previous_key = month_key(prev_year, prev_month)

    def filter_by_month(experiments_list, key):
        return [
            e for e in experiments_list
            if e["date"]["year"] == key[0] and e["date"]["month"] == key[1]
        ]

    def filter_measurements_by_month(measurements_list, key):
        return [
            m for m in measurements_list
            if m["date"]["year"] == key[0] and m["date"]["month"] == key[1]
        ]

    current_experiments = filter_by_month(experiments, current_key)
    previous_experiments = filter_by_month(experiments, previous_key)
    current_measurements = filter_measurements_by_month(measurements, current_key)
    previous_measurements = filter_measurements_by_month(measurements, previous_key)

    def average(values):
        return sum(values) / len(values) if values else 0.0

    current_avg = average(m["value"] for m in current_measurements)
    previous_avg = average(m["value"] for m in previous_measurements)

    def change(current_value, previous_value):
        if previous_value == 0:
            return 0.0
        return (current_value - previous_value) / previous_value * 100.0

    trend = "up" if current_avg >= previous_avg else "down"

    return {
        "report_month": MONTHS[_month_index(MONTHS[ref_month - 1])],
        "reference_month": reference_month.strftime("%Y-%m"),
        "experiments_count": len(current_experiments),
        "measurements_count": len(current_measurements),
        "average_value": round(current_avg, 2),
        "samples": sorted({e["sample"] for e in current_experiments}),
        "responsible": sorted({e["responsible"] for e in current_experiments}),
        "average_change": round(change(current_avg, previous_avg), 2),
        "trend": trend,
        "previous_month": MONTHS[_month_index(MONTHS[prev_month - 1])],
        "previous_average_value": round(previous_avg, 2),
    }
