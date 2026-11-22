# === Stage 14: Поиск дубликатов ===
# Project: LabNotebook
def normalize_experiment(experiment):
    """Return a normalized key for an experiment record."""
    title = experiment.get("title", "")
    sample = experiment.get("sample", "")
    responsible = experiment.get("responsible", "")
    normalized_title = " ".join(title.split()).lower().strip()
    normalized_sample = " ".join(sample.split()).lower().strip()
    normalized_responsible = " ".join(responsible.split()).lower().strip()
    return (normalized_title, normalized_sample, normalized_responsible)


def find_duplicate_experiments(experiments):
    """Find experiments that are duplicates based on normalized field values."""
    groups = {}
    for experiment in experiments:
        key = normalize_experiment(experiment)
        groups.setdefault(key, []).append(experiment)
    duplicates = [
        group
        for group in groups.values()
        if len(group) > 1
    ]
    return duplicates


if __name__ == "__main__":
    sample_data = [
        {"title": "Water Sample", "sample": "River A", "responsible": "Smith"},
        {"title": "water sample", "sample": "river a", "responsible": "smith"},
        {"title": "Soil Analysis", "sample": "Field B", "responsible": "Jones"},
    ]
    dup_groups = find_duplicate_experiments(sample_data)
    for group in dup_groups:
        print(group)
