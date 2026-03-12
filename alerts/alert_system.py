def generate_alert(prediction):

    if prediction == 0:
        return "No Animal Detected"

    if prediction == 1:
        return "⚠ Small Animal Detected"

    if prediction == 2:
        return "⚠ Medium Animal Crossing"

    if prediction == 3:
        return "⚠ Large Animal Crossing - Slow Down"