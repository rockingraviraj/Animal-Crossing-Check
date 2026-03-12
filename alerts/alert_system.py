import os

def trigger_alert(confidence, threshold=0.8):
    if confidence > threshold:
        print("ALERT! Animal Crossing Detected!")
        os.system("echo '\a'")
        return True
    return False