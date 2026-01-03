# Ornstein–Uhlenbeck Model for VIX (OU–VIX)

This repository implements an **Ornstein–Uhlenbeck (OU) mean-reverting stochastic model** applied to the **VIX (Volatility Index)**.  
The project combines **stochastic calculus**, **maximum likelihood estimation**, and **Monte Carlo simulation** to model and forecast volatility dynamics.

Author: **Marc Aliaga**

---

## 📌 Project Motivation

Financial volatility is well known to exhibit **mean-reverting behavior**.  
The VIX, in particular:

- Spikes during market stress
- Gradually reverts to a long-term average
- Does not behave like a geometric Brownian motion

The **Ornstein–Uhlenbeck process** is a natural mathematical framework to capture this behavior.

---

## 📐 Mathematical Model

We model the VIX using the stochastic differential equation:

\[
dX_t = \theta(\mu - X_t)\,dt + \sigma\,dW_t
\]

Where:
- \( X_t \) = VIX value at time \( t \)
- \( \mu \) = long-term mean
- \( \theta \) = speed of mean reversion
- \( \sigma \) = volatility of volatility
- \( W_t \) = standard Brownian motion

---

## 🧠 Methodology

1. **Data Collection**
   - Historical VIX data from Yahoo Finance (`^VIX`)
   - Daily frequency since 2012

2. **Parameter Estimation**
   - \( \mu \): sample mean
   - \( \theta, \sigma \): Maximum Likelihood Estimation (MLE)

3. **Optimization**
   - Negative log-likelihood minimization
   - `scipy.optimize.minimize`

4. **Simulation**
   - Exact OU solution
   - Monte Carlo paths for future VIX trajectories

---

## 📊 Outputs

- Estimated OU parameters
- Likelihood surface visualization
- Monte Carlo simulations
- Comparison between simulated and real VIX values

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- SciPy
- Matplotlib
- yFinance
- Jupyter / Google Colab

---

## ▶️ Video Explanations

📺 **Full Playlist – Finance & SDEs**  
👉 https://www.youtube.com/playlist?list=PLNwFFDTOL7s5ANo0IUVabq5dbmkgWVVlu

Videos include:
- Intuition behind mean reversion
- Connection between finance and stochastic calculus
- Ornstein–Uhlenbeck process explained
- Practical modeling of the VIX

---

## 🚀 How to Run

```bash
pip install numpy scipy matplotlib yfinance
