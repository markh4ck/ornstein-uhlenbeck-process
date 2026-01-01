# Ornstein–Uhlenbeck Stochastic Process (Python)

![Ornstein–Uhlenbeck Process Simulation](assets/ou_process.png)

This repository provides a complete and modular implementation of the **Ornstein–Uhlenbeck (OU) stochastic process** developed in Python. The Ornstein–Uhlenbeck process is a mean-reverting continuous-time stochastic process widely used in physics, quantitative finance, neuroscience, and stochastic modeling.

The implementation prioritizes **mathematical correctness**, **clarity**, and **reproducibility**, making it suitable for both educational and academic use.

---

## Mathematical Background

The Ornstein–Uhlenbeck process is defined by the stochastic differential equation:

\[
dX_t = \theta(\mu - X_t)\,dt + \sigma\,dW_t
\]

where:

- **μ** is the long-term mean  
- **θ > 0** is the rate of mean reversion  
- **σ > 0** is the volatility parameter  
- **Wₜ** is a standard Wiener process (Brownian motion)

This process models systems that fluctuate randomly while exhibiting a tendency to revert toward an equilibrium state.

---

## Features

- Numerical simulation of the Ornstein–Uhlenbeck process  
- Discrete-time approximation of the SDE  
- Fully configurable parameters:
  - Mean reversion strength  
  - Long-term mean  
  - Volatility  
  - Time step  
  - Initial condition  
- Visualization of stochastic trajectories  
- Clean and extensible Python codebase  

---

## Educational Explanation (Video)

A **conceptual and intuitive explanation** of the Ornstein–Uhlenbeck process, including its physical and mathematical interpretation, is available on my YouTube channel:

▶️ **YouTube:** [markaliaga](https://www.youtube.com/@markaliaga)

The video is intended to complement this repository by bridging theory and implementation.

---

## Intended Audience

This project is suitable for:

- Students studying stochastic processes or stochastic calculus  
- Researchers requiring a reference OU implementation  
- Quantitative finance practitioners (mean-reverting models)  
- Physicists and engineers modeling noisy dynamical systems  

---

## License

This project is provided for educational and research purposes.
