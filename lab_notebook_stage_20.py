# === Stage 20: История изменений ===
# Project: LabNotebook
class ChangeRecord:
    def __init__(self, field, value, date):
        self.field = field
        self.value = value
        self.date = date

    def as_dict(self):
        return {"field": self.field, "value": self.value, "date": self.date}

    def __repr__(self):
        return "ChangeRecord(field={!r}, value={!r}, date={!r})".format(
            self.field, self.value, self.date
        )


class Experiment:
    def __init__(self, name, sample, date, responsible):
        self.name = name
        self.sample = sample
        self.date = date
        self.responsible = responsible
        self.change_history = []

    def set_name(self, value):
        self.name = value
        self.change_history.append(ChangeRecord("name", value, self.date))

    def set_sample(self, value):
        self.sample = value
        self.change_history.append(ChangeRecord("sample", value, self.date))

    def set_date(self, value):
        self.date = value
        self.change_history.append(ChangeRecord("date", value, self.date))

    def set_responsible(self, value):
        self.responsible = value
        self.change_history.append(ChangeRecord("responsible", value, self.date))

    def add_change(self, field, value, date):
        self.change_history.append(ChangeRecord(field, value, date))

    def get_change_history(self):
        return self.change_history

    def as_dict(self):
        return {
            "name": self.name,
            "sample": self.sample,
            "date": self.date,
            "responsible": self.responsible,
            "change_history": self.change_history,
        }

    def __repr__(self):
        return "Experiment(name={!r}, sample={!r}, date={!r}, responsible={!r})".format(
            self.name, self.sample, self.date, self.responsible
        )


def load_experiment_history(data):
    experiment = Experiment(
        data["name"], data["sample"], data["date"], data["responsible"]
    )
    for record in data.get("change_history", []):
        experiment.change_history.append(
            ChangeRecord(record["field"], record["value"], record["date"])
        )
    return experiment


def save_experiment_history(experiment):
    return experiment.as_dict()
