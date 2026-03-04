import numpy as np
import pandas as pd

# time steps
time = np.arange(0,2000)

# normal wireless signal (no animal)
normal_signal = np.sin(time * 0.02) + np.random.normal(0,0.2,2000)

# disturbed signal (animal movement)
animal_signal = np.sin(time * 0.02) + np.random.normal(0,0.6,2000)

# labels
label_normal = np.zeros(2000)
label_animal = np.ones(2000)

# combine signals
signal = np.concatenate((normal_signal,animal_signal))
labels = np.concatenate((label_normal,label_animal))

# create dataframe
df = pd.DataFrame({
    "signal": signal,
    "label": labels
})

# save dataset
df.to_csv("data/csi_data.csv", index=False)

print("Dataset generated successfully")