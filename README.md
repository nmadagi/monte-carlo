# 🎲 Monte Carlo Simulation

> A Jupyter Notebook implementing Monte Carlo simulation for financial applications — including stock price path simulation using Geometric Brownian Motion (GBM) and option pricing.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

---

## 📌 Overview

Monte Carlo simulation is a core technique in quantitative finance, used to model uncertainty in asset prices, estimate option values, and stress-test portfolios. This notebook explores:

- **Stock price path simulation** using GBM
- **European option pricing** via Monte Carlo vs. Black-Scholes
- **Confidence intervals** for price estimates
- **Convergence analysis** — how accuracy improves with more simulations

---

## 🧮 Mathematical Foundation

The underlying asset follows **Geometric Brownian Motion (GBM)**:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

With exact discretization:

$$S_{t+\Delta t} = S_t \exp\left((\mu - \frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}\, Z\right)$$

where $Z \sim \mathcal{N}(0,1)$.

---

## 📊 Simulations Covered

| Simulation | Description |
|---|---|
| GBM Path Generation | Simulate thousands of possible future price paths |
| European Call Pricing | Monte Carlo vs. Black-Scholes closed-form |
| Confidence Intervals | 95% CI around estimated option prices |
| Convergence Study | Price estimate vs. number of simulations |
| Distribution of Payoffs | Histogram of terminal stock prices |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/nmadagi/monte-carlo.git
cd monte-carlo
```

### 2. Install dependencies
```bash
pip install numpy pandas matplotlib scipy jupyter
```

### 3. Launch the notebook
```bash
jupyter notebook
```

---

## 📦 Tech Stack

- **Python 3.10+**
- **NumPy** — Vectorized simulations
- **Pandas** — Results management
- **Matplotlib** — Path and distribution plots
- **SciPy** — Statistical functions (normal CDF for Black-Scholes)
- **Jupyter Notebook** — Interactive environment

---

## 💡 Key Takeaways

- More simulations → tighter confidence intervals (law of large numbers)
- Monte Carlo prices **converge** to Black-Scholes for European options
- GBM paths illustrate **log-normal** terminal price distributions
- Computationally expensive but highly flexible for exotic/path-dependent options

> 🔗 See also: [Quantitative Derivatives Monte Carlo Lab](https://github.com/nmadagi/quantitative-derivatives-monte-carlo-lab) for the advanced version of this work.

---

## 👤 Author

**Nitin Madagi** | [GitHub](https://github.com/nmadagi) | [Portfolio](https://nmadagi.github.io/portfolio)

## 📄 License

This project is licensed under the [MIT License](LICENSE).
