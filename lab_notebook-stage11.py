# === Stage 11: Группировка ===
# Project: LabNotebook
def group_experiments_by_sample(experiments):
    """Group experiments by the 'sample' field and count each group."""
    grouped = {}
    for experiment in experiments:
        sample = experiment["sample"]
        if sample in grouped:
            grouped[sample]["count"] += 1
        else:
            grouped[sample] = {"sample": sample, "count": 1}
    return grouped


def group_experiments_by_sample_sorted(experiments):
    """Group experiments by 'sample' and return sorted by sample name."""
    grouped = group_experiments_by_sample(experiments)
    return dict(sorted(grouped.items()))


def summarize_experiment_counts(experiments):
    """Summarize total experiments and per-sample counts."""
    grouped = group_experiments_by_sample(experiments)
    total = sum(count for count in grouped.values())
    return {"total": total, "by_sample": grouped}


if __name__ == "__main__":
    demo = [
        {"name": "Titration A", "sample": "NaCl", "date": "2024-01-01", "owner": "Alice"},
        {"name": "Titration B", "sample": "KBr", "date": "2024-01-02", "owner": "Bob"},
        {"name": "Titration C", "sample": "NaCl", "date": "2024-01-03", "owner": "Alice"},
    ]
    result = summarize_experiment_counts(demo)
    print(result)
