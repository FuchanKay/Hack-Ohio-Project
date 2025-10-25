import pypsa

network = pypsa.Network()
network.import_from_csv_folder("example_csv")
info = network.pf()
    
pload_total = network.loads['p_set'].sum().round(0)
print(f"Total load in network {pload_total}")