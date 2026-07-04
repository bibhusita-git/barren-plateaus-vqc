"""
Week 1: Reproducing the Barren Plateau phenomenon
Based on: McClean, Boixo, Smelyanskiy, Babbush, Neven (2018)
"Barren plateaus in quantum neural network training landscapes"
Nature Communications 9, 4812

GOAL:
For a random parameterized quantum circuit (hardware-efficient ansatz),
show that the variance of the gradient of a global cost function
w.r.t. a single parameter shrinks exponentially as the number of
qubits increases.
"""

import pennylane as qml
from pennylane import numpy as np   # PennyLane's numpy wrapper supports requires_grad
import matplotlib.pyplot as plt

np.random.seed(42)


def random_hardware_efficient_circuit(params, wires, depth):
    """
    A generic 'hardware-efficient' ansatz: alternating layers of
    random single-qubit rotations and a ring of entangling CNOTs.
    """
    n = len(wires)
    idx = 0
    for d in range(depth):
        for w in wires:
            qml.RX(params[idx], wires=w); idx += 1
            qml.RY(params[idx], wires=w); idx += 1
            qml.RZ(params[idx], wires=w); idx += 1
        for w in range(n - 1):
            qml.CNOT(wires=[wires[w], wires[w + 1]])
        qml.CNOT(wires=[wires[-1], wires[0]])  # close the ring
    return


def global_cost_observable(wires):
    """
    Global cost: <Z_1 Z_2 ... Z_n>.
    """
    obs = qml.PauliZ(wires[0])
    for w in wires[1:]:
        obs = obs @ qml.PauliZ(w)
    return obs


def build_qnode(n_qubits, depth):
    dev = qml.device("default.qubit", wires=n_qubits)
    wires = list(range(n_qubits))

    @qml.qnode(dev, diff_method="backprop")
    def circuit(params):
        random_hardware_efficient_circuit(params, wires, depth)
        return qml.expval(global_cost_observable(wires))

    n_params = n_qubits * depth * 3
    return circuit, n_params


def measure_gradient_variance(n_qubits, depth, n_samples=200):
    circuit, n_params = build_qnode(n_qubits, depth)
    grad_fn = qml.grad(circuit)

    gradients = []
    for _ in range(n_samples):
        params = np.random.uniform(0, 2 * np.pi, n_params, requires_grad=True)
        grad = grad_fn(params)
        gradients.append(grad[0])

    gradients = np.array(gradients)
    return np.var(gradients), gradients


def run_experiment(qubit_range, depth=6, n_samples=200):
    variances = []
    print(f"{'qubits':>8} | {'grad variance':>15} | {'n_samples':>10}")
    print("-" * 40)
    for n in qubit_range:
        var, _ = measure_gradient_variance(n, depth, n_samples)
        variances.append(var)
        print(f"{n:>8} | {var:>15.3e} | {n_samples:>10}")
    return np.array(variances)


def plot_results(qubit_range, variances, save_path="barren_plateau_week1.png"):
    plt.figure(figsize=(7, 5))
    plt.semilogy(qubit_range, variances, "o-", linewidth=2, markersize=8)
    plt.xlabel("Number of qubits (n)")
    plt.ylabel("Variance of ∂C/∂θ₁  (log scale)")
    plt.title("Barren Plateau: Gradient Variance vs Qubit Count\n(global cost, random hardware-efficient ansatz)")
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"\nPlot saved to {save_path}")

    log_var = np.log(variances)
    slope, intercept = np.polyfit(qubit_range, log_var, 1)
    print(f"\nLinear fit to log(variance) vs n:")
    print(f"  slope = {slope:.4f}  (expect roughly ln(1/2) ≈ -0.693 per qubit for ideal 2-design)")


if __name__ == "__main__":
    qubit_range = [2, 4, 6, 8]
    depth = 4
    n_samples = 50

    variances = run_experiment(qubit_range, depth=depth, n_samples=n_samples)
    plot_results(qubit_range, variances)