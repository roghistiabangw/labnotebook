# === Stage 21: Просмотр истории ===
# Project: LabNotebook
from datetime import datetime


class ExperimentRecord:
    """A single laboratory experiment entry in the notebook."""

    def __init__(self, name, sample, date, owner):
        self.name = name
        self.sample = sample
        self.date = date
        self.owner = owner
        self.measurements = []

    def add_measurement(self, value, unit, note=""):
        self.measurements.append({"value": value, "unit": unit, "note": note})

    def as_dict(self):
        return {
            "name": self.name,
            "sample": self.sample,
            "date": self.date,
            "owner": self.owner,
            "measurements": self.measurements,
        }


def format_experiment_compact(record):
    """Render one experiment record as a compact history block."""
    lines = []
    header = f"[{record.date}] {record.owner} | {record.name}"
    lines.append(f"  {header}")
    lines.append(f"    sample: {record.sample}")
    if record.measurements:
        lines.append("    measurements:")
        for m in record.measurements:
            line = f"      - {m['value']}{m['unit']}"
            if m["note"]:
                line += f"  ({m['note']})"
            lines.append(line)
    else:
        lines.append("    measurements: -")
    return "\n".join(lines)


def print_experiment_history(record):
    print(format_experiment_compact(record))
