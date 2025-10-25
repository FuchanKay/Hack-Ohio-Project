import os
print("Current working directory:", os.getcwd())

import pandas as pd
import  io
import pypsa

# Linear powerflow .lpf() is an approximation of full powerflow. It may make be useful if have convergence issues
USE_LPF = False


def check_pf(info):
    converged = info.converged.any().any()
    max_error = info.error.max().max()
    print(f"Sim converged: {converged}")
    print(f"Max error: {max_error:.2e}")

    if ~converged:
        raise Exception("Sim didn't convert - results are garbage. Change to lpf()")
    
network = pypsa.Network()
network.import_from_csv_folder('/example_csv')
if USE_LPF:
    network.lpf() 
else:
    info = network.pf() # Full powerflow
    check_pf(info)
    
network = pypsa.Network()
network.import_from_csv_folder('/example_csv')
if USE_LPF:
    network.lpf()
else:
    info = network.pf() # Full powerflow
    check_pf(info)
    
network.plot.map(bus_sizes=5e-5,)