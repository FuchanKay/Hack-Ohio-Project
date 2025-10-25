import pypsa
def calc_load_and_gen(csv_name):
    network = pypsa.Network()
    network.import_from_csv_folder(csv_name)
    info = network.pf()
    
    pload_total = network.loads['p_set'].sum().round(0)
    print(f"Total load in network {pload_total}")