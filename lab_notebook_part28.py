# === Stage 28: Статистика измерений ===
# Project: LabNotebook
from statistics import mean, pstdev, stdev


def average_and_spread(values):
    """Return the mean and a spread descriptor for a list of measurements.

    The spread is the sample standard deviation when at least two values
    are provided, otherwise it falls back to the population standard
    deviation, and to zero for a single value.
    """
    if not values:
        return None, None

    avg = mean(values)
    spread = pstdev(values) if len(values) > 1 else stdev(values) if len(values) == 1 else 0.0
    return avg, spread


def summarize_experiment(experiment, measurements):
    """Summarize an experiment with its measurements.

    The experiment is a mapping with a 'name', a 'sample', a 'date', and an
    'owner' key. The measurements are a list of numbers collected for that
    experiment. This function computes the average and the spread of the
    measurements and returns a compact summary dictionary.
    """
    if not measurements:
        return {
            'name': experiment.get('name'),
            'sample': experiment.get('sample'),
            'date': experiment.get('date'),
            'owner': experiment.get('owner'),
            'count': 0,
            'average': None,
            'spread': None,
        }

    avg, spread = average_and_spread(measurements)
    return {
        'name': experiment.get('name'),
        'sample': experiment.get('sample'),
        'date': experiment.get('date'),
        'owner': experiment.get('owner'),
        'count': len(measurements),
        'average': avg,
        'spread': spread,
    }


if __name__ == '__main__':
    demo_experiment = {
        'name': 'Electrolysis of water',
        'sample': 'Tap water with a few drops of salt',
        'date': '2024-05-14',
        'owner': 'Lab Analyst',
        'measurements': [1.10, 1.12, 1.08, 1.11, 1.09],
    }
    print(summarize_experiment(demo_experiment, demo_experiment['measurements']))
