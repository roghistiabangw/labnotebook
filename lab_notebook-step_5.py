# === Stage 5: Удаление и восстановление ===
# Project: LabNotebook
import uuid
from datetime import datetime


class SoftDeleteExperiment:
    def __init__(self, experiment_id):
        self.experiment_id = experiment_id
        self.deleted_at = None
        self.restored_at = None

    def mark_deleted(self):
        self.deleted_at = datetime.now().isoformat()
        self.restored_at = None

    def restore(self):
        if self.deleted_at is None:
            raise ValueError("Experiment is not deleted")
        self.deleted_at = None
        self.restored_at = datetime.now().isoformat()


def delete_experiment(experiments_store, experiment_id):
    for experiment in experiments_store:
        if experiment["id"] == experiment_id:
            experiment["deleted"] = True
            experiment["deleted_at"] = datetime.now().isoformat()
            experiment["restored_at"] = None
            return True
    return False


def restore_experiment(experiments_store, experiment_id):
    for experiment in experiments_store:
        if experiment["id"] == experiment_id and experiment.get("deleted"):
            experiment["deleted"] = False
            experiment["deleted_at"] = None
            experiment["restored_at"] = datetime.now().isoformat()
            return True
    return False


def is_experiment_active(experiment):
    return not experiment.get("deleted", False)


def get_deleted_experiments(experiments_store):
    return [exp for exp in experiments_store if exp.get("deleted")]


def get_active_experiments(experiments_store):
    return [exp for exp in experiments_store if not exp.get("deleted", False)]


def create_experiment(sample_id, name, responsible):
    experiment_id = str(uuid.uuid4())
    experiment = {
        "id": experiment_id,
        "sample_id": sample_id,
        "name": name,
        "responsible": responsible,
        "created_at": datetime.now().isoformat(),
        "deleted": False,
        "deleted_at": None,
        "restored_at": None,
    }
    return experiment


if __name__ == "__main__":
    store = []
    sample_id = "S-001"

    experiment = create_experiment(sample_id, "pH measurement", "dr.ivanov")
    store.append(experiment)
    print("Created experiment:", experiment["id"])

    deleted = delete_experiment(store, experiment["id"])
    print("Deleted:", deleted)
    print("Is active:", is_experiment_active(experiment))

    restored = restore_experiment(store, experiment["id"])
    print("Restored:", restored)
    print("Is active:", is_experiment_active(experiment))
    print("Active count:", len(get_active_experiments(store)))
    print("Deleted count:", len(get_deleted_experiments(store)))
