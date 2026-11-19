# === Stage 7: Связи между сущностями ===
# Project: LabNotebook
from datetime import date


def load_experiments(path):
    experiments = {}
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            key = parts[0]
            experiments[key] = {
                "id": key,
                "name": parts[1],
                "sample": parts[2],
                "date": parts[3],
                "owner": parts[4] if len(parts) > 4 else "",
            }
    return experiments


def load_measurements(path):
    measurements = {}
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            entry = {
                "id": parts[0],
                "experiment": parts[1],
                "value": parts[2],
                "unit": parts[3] if len(parts) > 3 else "",
            }
            measurements.setdefault(entry["experiment"], []).append(entry)
    return measurements


def get_measurements_for_experiment(measurements, experiment_id):
    return measurements.get(experiment_id, [])


def check_integrity(experiments, measurements):
    issues = []
    for experiment_id, experiment in experiments.items():
        if experiment_id not in measurements:
            issues.append(
                "Experiment {} has no measurements".format(experiment_id)
            )
        for entry in measurements.get(experiment_id, []):
            if entry["experiment"] != experiment_id:
                issues.append(
                    "Measurement {} belongs to experiment {} "
                    "but references {}".format(entry["id"], entry["experiment"],
                                               experiment_id)
                )
    return issues


def main():
    experiments = load_experiments("experiments.tsv")
    measurements = load_measurements("measurements.tsv")

    experiment_id = "EXP-001"
    results = get_measurements_for_experiment(measurements, experiment_id)
    print("Measurements for {}: {}".format(experiment_id, results))

    problems = check_integrity(experiments, measurements)
    if problems:
        print("Integrity problems found:")
        for problem in problems:
            print(" - {}".format(problem))
    else:
        print("All integrity checks passed.")


if __name__ == "__main__":
    main()
