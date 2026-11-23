# === Stage 17: Избранное ===
# Project: LabNotebook
from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Set


@dataclass
class Experiment:
    title: str
    sample: str
    date: date
    owner: str
    is_favorite: bool = False


class LabNotebook:
    def __init__(self):
        self._experiments: List[Experiment] = []

    def add_experiment(self, title: str, sample: str, experiment_date: date, owner: str) -> Experiment:
        experiment = Experiment(title, sample, experiment_date, owner)
        self._experiments.append(experiment)
        return experiment

    def get_experiment(self, title: str) -> Experiment:
        for experiment in self._experiments:
            if experiment.title == title:
                return experiment
        raise KeyError(title)

    def toggle_favorite(self, title: str) -> None:
        experiment = self.get_experiment(title)
        experiment.is_favorite = not experiment.is_favorite

    def get_favorite_experiments(self) -> List[Experiment]:
        return [experiment for experiment in self._experiments if experiment.is_favorite]

    def remove_favorite(self, title: str) -> None:
        experiment = self.get_experiment(title)
        experiment.is_favorite = False

    def __len__(self) -> int:
        return len(self._experiments)
