# === Stage 24: Скользящее среднее ===
# Project: LabNotebook
import statistics


def moving_average(values, window):
    """Return a list of sliding-window means over a numeric series.

    Each output element is the mean of up to ``window`` trailing values
    ending at the corresponding position. The first ``window - 1`` results
    cover fewer than ``window`` values (a warm-up ramp).
    """
    if window < 1:
        raise ValueError("window must be a positive integer")

    averages = []
    current_sum = 0.0
    current_count = 0

    for value in values:
        current_sum += value
        current_count += 1
        if current_count > window:
            current_sum -= values[current_count - window - 1]
            current_count -= 1
        averages.append(current_sum / current_count)

    return averages


def moving_average_from_measurements(measurements, window):
    """Compute a sliding mean over the numeric indicator of experiments.

    Each measurement must expose a numeric indicator accessible through the
    ``indicator`` attribute or the ``value`` attribute. The result is a list
    aligned with the input measurements; the first ``window - 1`` entries are
    partial averages.
    """
    values = [measurement.indicator if hasattr(measurement, "indicator")
              else measurement.value for measurement in measurements]
    return moving_average(values, window)


def smooth_experiment_series(experiments, window):
    """Smooth the numeric indicator of a list of experiments.

    Returns a dictionary keyed by experiment title with the corresponding
    list of sliding-window averages. Experiments without a numeric indicator
    are skipped.
    """
    smoothed = {}
    for experiment in experiments:
        if not hasattr(experiment, "indicator") and not hasattr(experiment, "value"):
            continue
        title = getattr(experiment, "title", getattr(experiment, "name", None))
        if title is None:
            continue
        if hasattr(experiment, "indicator"):
            values = [experiment.indicator]
        else:
            values = [experiment.value]
        smoothed[title] = moving_average(values, window)
    return smoothed


def rolling_window_statistics(values, window):
    """Return per-position means, minimums, and maximums for a numeric series.

    Each entry in the returned list is a tuple ``(mean, min, max)`` computed
    over the trailing ``window`` values ending at that position.
    """
    results = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        segment = values[start:i + 1]
        if not segment:
            continue
        results.append((statistics.fmean(segment),
                        min(segment),
                        max(segment)))
    return results
