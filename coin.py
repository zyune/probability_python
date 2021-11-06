import numpy as np

# number of coin tossing in one experiment
n = 100
p = 0.5
# number of experiements
n_experiment = 5

h = np.random.binomial(n, p, n_experiment)
# Frequency of heads up in each trial
frequency = h/n

print(h)
print(frequency)
