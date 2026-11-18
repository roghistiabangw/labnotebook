# === Stage 4: Редактирование записей ===
# Project: LabNotebook
ALLOWED_EXPERIMENT_FIELDS = ("id", "name", "sample", "date", "responsible")


def edit_experiment(experiments, experiment_id, updates):
    for experiment in experiments:
        if experiment["id"] == experiment_id:
            for field in updates:
                if field not in ALLOWED_EXPERIMENT_FIELDS:
                    raise ValueError(f"Field '{field}' is not allowed for editing experiment")
            for field, value in updates.items():
                experiment[field] = value
            return experiment
    return None


def validate_experiment(experiment):
    for field in ("name", "sample", "date", "responsible"):
        if field not in experiment:
            raise ValueError(f"Experiment is missing required field '{field}'")
        if not isinstance(experiment[field], str):
            raise ValueError(f"Field '{field}' must be a string")
    if not experiment["name"].strip():
        raise ValueError("Experiment name cannot be empty")
    if not experiment["sample"].strip():
        raise ValueError("Experiment sample cannot be empty")
    if not experiment["responsible"].strip():
        raise ValueError("Experiment responsible cannot be empty")
    try:
        datetime.datetime.strptime(experiment["date"], "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Date '{experiment['date']}' is not in the format YYYY-MM-DD")
    return True
