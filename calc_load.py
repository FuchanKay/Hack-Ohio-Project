import pypsa
import numpy as np

def calc_total_load_gen(csv_name):
    
    network = pypsa.Network()
    network.import_from_csv_folder(csv_name)
    info = network.pf()
    
    pload_total = network.loads['p_set'].sum().round(0)
    print(f"Total load in network {pload_total}")
    
    pgen_total = network.generators['p_set'].sum().round(0)
    print(f"Total load in network {pgen_total}")
    
    x = np.arange(24)
    f = 1/24
    offset = 1
    A = 0.1
    C = 2*np.pi/2
    y = A * np.sin(2*np.pi * f * x + C) + offset
    
    print(y.round(3).tolist())
    
def calc_load_gen_by_hour(csv_name, line_name):
    network = pypsa.Network()
    network.import_from_csv_folder(csv_name)
    info = network.pf() 
    
    load_array = network.loads['p_set']
    load = load_array[int(line_name[1])]
    print(f"Load on {line_name}: {load}")