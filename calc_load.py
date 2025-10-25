import pypsa
import numpy as np

def get_scale(csv_name):
    
    network = pypsa.Network()
    network.import_from_csv_folder("csv")
    info = network.pf()
    
    pload_total = network.loads['p_set'].sum().round(0)
    #print(f"Total load in network {pload_total}")
    
    pgen_total = network.generators['p_set'].sum().round(0)
    #print(f"Total load in network {pgen_total}")
    
    x = np.arange(24)
    f = 1/24
    offset = 1
    A = 0.1
    C = 2*np.pi/2
    y = A * np.sin(2*np.pi * f * x + C) + offset
    
    return y
    
def calc_load(line_name, hour):
    network = pypsa.Network()
    network.import_from_csv_folder("csv")
    info = network.pf() 
    
    line_index = int(line_name[1]) 
    load_array = network.loads['p_set']
    load = load_array[line_index]
    #print(f"Load on {line_name}: {load}")
    
    scale = get_scale("csv")[hour]
    #print(f"Scaling load by {scale}")
    #print(load * scale)
    
    return load * scale
    
    

    
    