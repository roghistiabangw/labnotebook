# === Stage 19: Смена статуса ===
# Project: LabNotebook
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class ExperimentStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    CONCLUDED = "concluded"
    ARCHIVED = "archived"
    REJECTED = "rejected"


@dataclass
class Experiment:
    title: str
    sample: str
    date: date
    owner: str
    status: ExperimentStatus = ExperimentStatus.DRAFT
    notes: list = field(default_factory=list)


_TRANSITIONS = {
    ExperimentStatus.DRAFT: {ExperimentStatus.ACTIVE, ExperimentStatus.REJECTED},
    ExperimentStatus.ACTIVE: {ExperimentStatus.CONCLUDED, ExperimentStatus.ARCHIVED, ExperimentStatus.REJECTED},
    ExperimentStatus.CONCLUDED: {ExperimentStatus.ARCHIVED},
    ExperimentStatus.ARCHIVED: set(),
    ExperimentStatus.REJECTED: {ExperimentStatus.DRAFT},
}


class ExperimentStateError(ValueError):
    pass


def change_experiment_status(
    experiment: Experiment,
    new_status: ExperimentStatus,
    reason: str,
) -> Experiment:
    if new_status is None:
        raise ExperimentStateError("New status must not be None")
    if not isinstance(reason, str) or not reason.strip():
        raise ExperimentStateError("Reason must be a non-empty string")
    if not experiment or experiment.status is None:
        raise ExperimentStateError("Experiment must exist and have a current status")
    if new_status not in _TRANSITIONS[experiment.status]:
        raise ExperimentStateError(
            f"Transition from {experiment.status.value!r} to {new_status.value!r} is not allowed"
        )
    experiment.status = new_status
    experiment.notes.append(f"status={new_status.value} reason={reason}")
    return experiment


def allowed_transitions(experiment: Experiment) -> set:
    return set(_TRANSITIONS.get(experiment.status, set()))
