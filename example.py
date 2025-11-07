import pandas as pd
import numpy as np
from scipy.optimize import differential_evolution

# ==============================
# Load Data
# ==============================
data = pd.read_csv("C:/Users/kusha/Downloads/xy_data.csv")
x_data, y_data = data['x'].values, data['y'].values
N = len(x_data)

# Create corresponding t values (uniform sampling from 6 to 60)
t_values = np.linspace(6, 60, N)

# ==============================
# Define Parametric Equations
# ==============================
def curve(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# ==============================
# Define L1 Loss (Mean Absolute Error)
# ==============================
def objective(params):
    theta, M, X = params
    x_pred, y_pred = curve(t_values, theta, M, X)
    return np.mean(np.abs(x_data - x_pred) + np.abs(y_data - y_pred))

# ==============================
# Parameter Bounds
# ==============================
bounds = [
    (0, np.deg2rad(50)),  # theta in radians
    (-0.05, 0.05),        # M
    (0, 100)              # X
]

# ==============================
# Optimization
# ==============================

result = differential_evolution(objective, bounds, tol=1e-6, maxiter=2000, polish=True)

theta_opt, M_opt, X_opt = result.x
min_L1 = result.fun
theta_deg = np.rad2deg(theta_opt)

# ==============================
# Display Results
# ==============================
print("\n✅ Optimization Results:")
print(f"Theta (radians): {theta_opt:.6f}")
print(f"Theta (degrees): {theta_deg:.3f}°")
print(f"M: {M_opt:.6f}")
print(f"X: {X_opt:.6f}")
print(f"Minimum L1 Distance: {min_L1:.6f}")

# ==============================
# Generate Sample Points for Verification
# ==============================
t_sample = np.linspace(6, 60, 10)
x_pred, y_pred = curve(t_sample, theta_opt, M_opt, X_opt)
df_out = pd.DataFrame({'t': t_sample, 'x_pred': x_pred, 'y_pred': y_pred})
df_out.to_csv("C:/Users/kusha/Downloads/fitted_points.csv", index=False)