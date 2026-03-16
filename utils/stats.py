stats = {
    "no_animal":0,
    "small":0,
    "medium":0,
    "large":0
}

def update_stats(prediction):

    if prediction == 0:
        stats["no_animal"] += 1

    elif prediction == 1:
        stats["small"] += 1

    elif prediction == 2:
        stats["medium"] += 1

    else:
        stats["large"] += 1

    return stats
