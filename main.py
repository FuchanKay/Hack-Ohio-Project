# import calc_load
# import os

# path_name = os.path.basename("example_csv/loads.csv")
# calc_load.calc_load_and_gen(path_name)
# print("end")
import pypsa
import requests

network = pypsa.Network()
network.import_from_csv_folder("example_csv")
info = network.pf()
    
pload_total = network.loads['p_set'].sum().round(0)
print(f"Total load in network {pload_total}")

api_url = ""

