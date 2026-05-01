from datetime import datetime

history = []

def save_detection(status):

    history.insert(0, {
        "status": status,
        "time": datetime.now().strftime("%H:%M:%S")
    })


def get_history():

    return history[:10]