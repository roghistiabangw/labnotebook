# === Stage 6: Связанная сущность ===
# Project: LabNotebook
import uuid
from datetime import date

class Measurement:
    """A single measurement record belonging to a lab experiment."""

    def __init__(self, value, unit, note=""):
        self.id = uuid.uuid4().hex
        self.value = value
        self.unit = unit
        self.note = note
        self.experiment_id = None

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "unit": self.unit,
            "note": self.note,
            "experiment_id": self.experiment_id,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            value=data.get("value"),
            unit=data.get("unit"),
            note=data.get("note", ""),
        )


def add_measurement(measurements, experiment_id, value, unit, note=""):
    """Append a new measurement record and return it.

    Args:
        measurements: list of Measurement objects (the collection to extend).
        experiment_id: identifier of the experiment this measurement belongs to.
        value: measured quantity.
        unit: unit of the measured quantity.
        note: optional free-text remark.

    Returns:
        The newly created Measurement object.
    """
    measurement = Measurement(value=value, unit=unit, note=note)
    measurement.experiment_id = experiment_id
    measurements.append(measurement)
    return measurement


def get_measurements_for_experiment(measurements, experiment_id):
    """Return all measurement records linked to a given experiment."""
    return [m for m in measurements if m.experiment_id == experiment_id]


def average_value(measurements, experiment_id, unit=None):
    """Compute the arithmetic mean of values for an experiment.

    Returns:
        A tuple (mean, unit) or (None, None) when there are no records.
    """
    records = get_measurements_for_experiment(measurements, experiment_id)
    if not records:
        return None, None
    total = sum(float(r.value) for r in records)
    return total / len(records), unit
