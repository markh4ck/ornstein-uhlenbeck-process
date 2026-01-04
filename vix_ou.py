# -*- coding: utf-8 -*-

import yfinance as yf
import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import minimize

# Dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
start_date = "2012-01-01"

# VIX data
vix_data_full = yf.download(
    "^VIX",
    start=start_date,
    end=yesterday + datetime.timedelta(days=1),
    progress=False
)
vix_data = vix_data_full["Close"]

# Estimate mu
x_values = vix_data.values.astype(float)
mu = np.mean(x_values)

plt.figure(figsize=(10, 6))
plt.plot(vix_data.index, x_values)
plt.axhline(mu, color="red", lw=1)
plt.grid()
plt.show()

# Negative log-likelihood
def negative_log_likelihood(params, x, dt):
    theta, sigma = params
    n = len(x)
    log_likelihood = 0.0

    for i in range(1, n):
        mean = mu + (x[i - 1] - mu) * np.exp(-theta * dt)
        variance = (sigma**2) / (2 * theta) * (1 - np.exp(-2 * theta * dt))
        log_likelihood += -norm.logpdf(x[i], loc=mean, scale=np.sqrt(variance))

    return log_likelihood

# Likelihood surface
theta_range = np.linspace(0.3, 1, 50)
sigma_range = np.linspace(0.3, 1, 50)
Theta, Sigma = np.meshgrid(theta_range, sigma_range)
Z = np.zeros_like(Theta)

for i in range(Theta.shape[0]):
    for j in range(Theta.shape[1]):
        try:
            Z[i, j] = negative_log_likelihood(
                (Theta[i, j], Sigma[i, j]),
                x_values[:50],
                1
            )
        except:
            Z[i, j] = np.nan

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(Theta, Sigma, Z, cmap="viridis")
ax.set_xlabel("theta")
ax.set_ylabel("sigma")
ax.set_zlabel("NLL")
ax.view_init(elev=30, azim=120)
plt.title("Negative Log-Likelihood Surface")
plt.show()

# MLE estimation
def mle_estimation(x):
    dt = 1.0
    initial_params = [0.5, np.std(x)]
    result = minimize(
        negative_log_likelihood,
        initial_params,
        args=(x, dt),
        bounds=[(1e-5, None), (1e-5, None)]
    )
    theta_mle, sigma_mle = result.x
    return theta_mle, sigma_mle

# OU Monte Carlo simulation
def simulate_ou_paths(x0, mu, theta, sigma, dt, horizon, n_paths):
    n_steps = int(horizon / dt)
    paths = np.zeros((n_steps + 1, n_paths))
    paths[0] = x0

    for t in range(1, n_steps + 1):
        mean = paths[t - 1] * np.exp(-theta * dt) + mu * (1 - np.exp(-theta * dt))
        variance = (sigma**2) / (2 * theta) * (1 - np.exp(-2 * theta * dt))
        std_dev = np.sqrt(variance)
        paths[t] = np.random.normal(mean, std_dev, size=n_paths)

    return paths

# Simulation parameters
start_index = 180
window_size = 30

training_window = vix_data.iloc[start_index:start_index + window_size].values.astype(float)
x0 = training_window[-1]

horizon = 7
dt = 1.0
n_paths = 20

future_values = vix_data.iloc[
    start_index + window_size - 1 : start_index + window_size + horizon
].values.astype(float)

theta_mle, sigma_mle = mle_estimation(training_window)

paths = simulate_ou_paths(
    x0,
    mu,
    theta_mle,
    sigma_mle,
    dt,
    horizon,
    n_paths
)

plt.figure(figsize=(10, 6))
plt.plot(paths, lw=1, alpha=0.7, color="grey")

mean_path = np.mean(paths, axis=1)
plt.plot(range(len(mean_path)), mean_path, lw=2, color="gold")

plt.axhline(x0, color="red", linestyle="--")
plt.plot(range(len(future_values)), future_values, lw=3, color="blue")

plt.title(f"VIX Monte Carlo Approximation ({horizon} days)")
plt.xlabel("Days")
plt.ylabel("Index Level")
plt.grid(True)
plt.show()
