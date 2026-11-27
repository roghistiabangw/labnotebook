# === Stage 27: Календарная сетка ===
# Project: LabNotebook
from calendar import monthcalendar


def render_month_grid(year, month):
    """Render a measurement month as a text grid of days and samples."""
    header = f"{year} - {month:02d}".center(14)
    separator = "-" * (len(header) + 2)
    lines = [header, separator]
    for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        lines.append(f"  {weekday}".ljust(14) + "  " + " ".join(["-"] * 4))
    lines.append("-" * (len(lines[-1]) + 2))
    grid = monthcalendar(year, month)
    day_index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for week in grid:
        row = []
        for day in week:
            if day == 0:
                row.append("   ")
            else:
                row.append(f"{day:02d}")
        lines.append("  " + "  ".join(row))
    return "\n".join(lines)


def format_measurement(day, sample, value, unit):
    """Format a single measurement into a grid cell."""
    return f"{day:02d}  {sample:5s}  {value:8.2f} {unit}"


def build_month_report(year, month, measurements):
    """Build a monthly report from a list of measurement records."""
    grid = render_month_grid(year, month)
    lines = [grid, "", "Measurements:"]
    for record in measurements:
        lines.append("  " + format_measurement(
            record["day"], record["sample"],
            record["value"], record["unit"]))
    return "\n".join(lines)
