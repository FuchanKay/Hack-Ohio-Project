import pypsa
import pandas as pd
import ieee738
from ieee738 import Conductor
from ieee738 import ConductorParams

# will have temp, wind speed


# 
def get_conductor_info(csv_folder, line_number):
    network = pypsa.Network()
    network.import_from_csv_folder(csv_folder)
    
    # gets name of conductor at specified line number
    conductor_name = network.lines['conductor'][line_number]
    
    # get array of data for specific conductor
    dataframe = pd.read_csv('conductor_library.csv')
    conductor_info = dataframe.loc[conductor_name] #.loc is label-based indexing
    
    return conductor_info

# for conductor, can get info from conductor library