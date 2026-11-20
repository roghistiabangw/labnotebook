# === Stage 9: Фильтрация записей ===
# Project: LabNotebook
from datetime import date


def filter_experiments(experiments, sample=None, date_start=None, date_end=None):
    results = []
    for experiment in experiments:
        if sample is not None and experiment.get("sample") != sample:
            continue
        experiment_date = experiment.get("date")
        if date_start is not None and experiment_date < date_start:
            continue
        if date_end is not None and experiment_date > date_end:
            continue
        results.append(experiment)
    return results


def filter_by_sample(experiments, sample):
    return filter_experiments(experiments, sample=sample)


def filter_by_date_range(experiments, date_start, date_end):
    return filter_experiments(experiments, date_start=date_start, date_end=date_end)


def filter_by_sample_and_date(experiments, sample, date_start, date_end):
    return filter_experiments(
        experiments, sample=sample, date_start=date_start, date_end=date_end
    )


def main():
    sample_data = [
        {
            "id": 1,
            "name": "Iron Oxide Reduction",
            "sample": "Iron Ore A",
            "date": date(2024, 1, 15),
            "responsible": "Alice",
        },
        {
            "id": 2,
            "name": "Copper Plating",
            "sample": "Copper Sheet B",
            "date": date(2024, 2, 20),
            "responsible": "Bob",
        },
        {
            "id": 3,
            "name": "Iron Oxide Testing",
            "sample": "Iron Ore A",
            "date": date(2024, 3, 10),
            "responsible": "Carol",
        },
    ]

    filtered_by_sample = filter_by_sample(sample_data, "Iron Ore A")
    for exp in filtered_by_sample:
        print(f"{exp['name']} - {exp['sample']} - {exp['date']}")

    filtered_by_date = filter_by_date_range(
        sample_data, date(2024, 1, 1), date(2024, 2, 28)
    )
    for exp in filtered_by_date:
        print(f"{exp['name']} - {exp['sample']} - {exp['date']}")

    filtered_combined = filter_by_sample_and_date(
        sample_data, "Iron Ore A", date(2024, 1, 1), date(2024, 12, 31)
    )
    for exp in filtered_combined:
        print(f"{exp['name']} - {exp['sample']} - {exp['date']}")


if __name__ == "__main__":
    main()
