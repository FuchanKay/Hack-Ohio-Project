import matplotlib.pyplot as plt
import pypsa

USE_LPF = False

def check_pf(info):
    converged = info.converged.any().any()
    max_error = info.error.max().max()
    print(f"Sim converged: {converged}")
    print(f"Max error: {max_error:.2e}")

    if not converged:
        raise Exception("Simulation didn’t converge — try .lpf() instead")

# Import the network
network = pypsa.Network()
network.import_from_csv_folder('example_csv')

# Run power flow
if USE_LPF:
    network.lpf()
else:
    info = network.pf()  # Full nonlinear AC power flow
    check_pf(info)

# ✅ Plot the network
plt.figure(figsize=(8, 6))
network.plot(bus_sizes=5e-5, title="Network")
plt.show()  

