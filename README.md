# Parametric Curve Fitting — Finding Unknown Variables (θ, M, X)

## Overview

This repository contains the implementation and explanation for optimizing the unknown parameters (θ, M, X) of a given nonlinear parametric equation using **L1 distance minimization**. The optimization is performed using a global method, **Differential Evolution**, from the SciPy library.

The goal is to minimize the L1 distance between the predicted curve points and the observed data points provided in `xy_data.csv`.

---

## Problem Definition

The parametric equations are given as:

[
\begin{aligned}
x(t) &= t \cos(\theta) - e^{M|t|} \sin(0.3t) \sin(\theta) + X \
y(t) &= 42 + t \sin(\theta) + e^{M|t|} \sin(0.3t) \cos(\theta)
\end{aligned}
]

### Given Parameter Ranges:

[
0^\circ < \theta < 50^\circ, \quad -0.05 < M < 0.05, \quad 0 < X < 100, \quad 6 < t < 60
]

The objective is to minimize the L1 distance between the predicted and observed data points:

[
J(\theta, M, X) = \frac{1}{N} \sum_{i=1}^{N} (|x_i - x(t_i)| + |y_i - y(t_i)|)
]

---

## Approach

1. **Data Preparation:**

   * The dataset `xy_data.csv` contains observed `(x, y)` points. Since the parameter `t` is not provided, it is assumed to be **uniformly spaced between 6 and 60**.
   * This assumption ensures every observed point corresponds to a unique, evenly distributed parameter `t_i`, preserving the sequential nature of the data. Uniform sampling avoids bias and provides equal weighting during optimization.

2. **Objective Function:**

   * The L1 (mean absolute) error between observed and predicted values is minimized to make the fit robust to outliers.

3. **Optimization Technique:**

   * **Differential Evolution (DE)** is employed for its robustness in non-convex, nonlinear search spaces.
   * Parameter bounds are strictly enforced within the defined limits.

4. **Output:**

   * Optimized constants for (θ, M, X)
   * Minimum L1 distance

---

## Results

| Parameter             | Symbol | Optimized Value      | Units                |
| --------------------- | ------ | -------------------- | -------------------- |
| Angle                 | θ      | 0.4907588562032585   | radians (≈ 28.1184°) |
| Exponential term      | M      | 0.021388998216425134 | —                    |
| Shift                 | X      | 54.89766111277908    | —                    |
| Minimized L1 Distance | —      | 25.243396552276867   | —                    |

All parameters are within their given constraints.

---

## Final Equation (for Submission)

LaTeX format:

[
\left(
t\cos(0.4907588562032585) - e^{0.021388998216425134|t|}\sin(0.3t)\sin(0.4907588562032585) + 54.89766111277908,
42 + t\sin(0.4907588562032585) + e^{0.021388998216425134|t|}\sin(0.3t)\cos(0.4907588562032585)
\right)
]

Plain text (Desmos compatible):

```
(t*cos(0.4907588562032585) - e^(0.021388998216425134*abs(t))*sin(0.3*t)*sin(0.4907588562032585) + 54.89766111277908,
 42 + t*sin(0.4907588562032585) + e^(0.021388998216425134*abs(t))*sin(0.3*t)*cos(0.4907588562032585))
```

---

## Desmos Visualization

Interactive Desmos graph of the optimized curve:
👉 [View Parametric Curve on Desmos](https://www.desmos.com/calculator/j5kjrx2oht)

---

## Repository Contents

* `parametric_fit.py` : Python script implementing the optimization.
* `xy_data.csv` : Input dataset (x, y coordinates).
* `fitted_points.csv` : Output file with predicted points for verification.
* `README.md` : This documentation.

---

## How to Run Locally

1. Install dependencies:

   ```bash
   pip install numpy pandas scipy matplotlib
   ```
2. Run the script:

   ```bash
   python parametric_fit.py
   ```
3. Output:

   * Optimized values (θ, M, X)
   * Minimum L1 distance
   * `fitted_points.csv` with sample predicted points

---

## Interpretation

* θ controls the **orientation** of the curve.
* M defines the **growth or decay rate** of the oscillations.
* X applies a **horizontal shift**.
* The low L1 distance (~25.24) confirms the optimized curve closely fits the dataset.

---

## Citation

> Differential Evolution algorithm implementation from SciPy: `scipy.optimize.differential_evolution`.
> Reference: Virtanen, P. & Gommers, Ralf & Oliphant, T.E. & Haberland, M. & Reddy, T. & Cournapeau, D. & Burovski, E. & Peterson, Pearu & Weckesser, W. & Bright, Jonathan & Walt, S.J. & Brett, Matthew & Wilson, J. & Millman, K.J. & Mayorov, N. & Nelson, A.R.J. & Jones, E. & Kern, R. & Larson, E. & SciPy, Contributors. (2020). Author Correction: SciPy 1.0: fundamental algorithms for scientific computing in Python (Nature Methods, (2020), 17, 3, (261-272), 10.1038/s41592-019-0686-2). 
