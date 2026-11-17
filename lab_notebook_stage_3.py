# === Stage 3: Хранилище в памяти ===
# Project: LabNotebook
from datetime import date


class Experiment:
    def __init__(self, identifier, title, sample, performed_by, when):
        self.identifier = identifier
        self.title = title
        self.sample = sample
        self.performed_by = performed_by
        self.when = when

    def __repr__(self):
        return (
            f"Experiment(identifier={self.identifier!r}, "
            f"title={self.title!r}, "
            f"sample={self.sample!r}, "
            f"performed_by={self.performed_by!r}, "
            f"when={self.when!r})"
        )


class ExperimentStore:
    def __init__(self):
        self._experiments = {}

    def add_experiment(self, experiment):
        if experiment.identifier in self._experiments:
            raise ValueError(
                f"Experiment {experiment.identifier!r} already exists"
            )
        self._experiments[experiment.identifier] = experiment

    def get_experiment(self, identifier):
        return self._experiments.get(identifier)

    def list_experiments(self):
        return list(self._experiments.values())


def new_experiment(identifier, title, sample, performed_by, when=None):
    return Experiment(
        identifier=identifier,
        title=title,
        sample=sample,
        performed_by=performed_by,
        when=when or date.today(),
    )


def demo():
    store = ExperimentStore()
    store.add_experiment(new_experiment("exp-001", "Boiling point check",
                                        "water", "Anna"))
    store.add_experiment(new_experiment("exp-002", "Density test",
                                        "aluminum", "Bob"))
    print(store.get_experiment("exp-001"))
    for exp in store.list_experiments():
        print(exp.title, "->", exp.performed_by)


if __name__ == "__main__":
    demo()
