import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Data/replicator_data_2_100032_iter.csv")

data.columns=["time step", "number of clusters", "number of clusters with tokens", "number of cells", "number of particles", "number of tokens", "total internal energy", "total kinetic energy"]

plt.plot(data["time step"],data["number of clusters"])
plt.show()