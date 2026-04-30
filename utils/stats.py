# utils/stats.py

stats = {
    "No Animal": 0,
    "Small": 0,
    "Medium": 0,
    "Large": 0
}


def update_stats(prediction):

    if prediction == 0:
        stats["No Animal"] += 1

    elif prediction == 1:
        stats["Small"] += 1

    elif prediction == 2:
        stats["Medium"] += 1

    else:
        stats["Large"] += 1

    return stats


def get_stats():
    return stats