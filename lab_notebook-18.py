# === Stage 18: Статусы записей ===
# Project: LabNotebook
VALID_TRANSITIONS = {
    "draft": {"pending_review", "archived"},
    "pending_review": {"approved", "rejected", "archived"},
    "approved": {"completed", "superseded", "archived"},
    "completed": {"archived"},
    "superseded": {"archived"},
    "archived": set(),
}

LIFECYCLE_STATUSES = ("draft", "pending_review", "approved", "completed", "superseded", "archived")


def is_valid_transition(current_status, target_status):
    return target_status in VALID_TRANSITIONS.get(current_status, set())


def transition_experiment(experiment, target_status):
    current_status = experiment["status"]
    if not is_valid_transition(current_status, target_status):
        raise ValueError(
            f"Invalid transition from '{current_status}' to '{target_status}'"
        )
    experiment["status"] = target_status
    return experiment


def get_status_path(status):
    path = []
    current = status
    while current in VALID_TRANSITIONS:
        path.append(current)
        if current == "draft":
            break
        current = "pending_review" if current == "draft" else "approved"
    return path


def get_status_description(status):
    descriptions = {
        "draft": "Draft experiment, initial record",
        "pending_review": "Awaiting review by responsible person",
        "approved": "Approved and ready for measurement",
        "completed": "All measurements finished",
        "superseded": "Replaced by a newer experiment",
        "archived": "Retired from active use",
    }
    return descriptions.get(status, "Unknown status")
