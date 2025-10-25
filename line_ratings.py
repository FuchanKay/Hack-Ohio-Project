import pypsa
import pandas as pd

# will have temp, wind speed


# 
def get_conductor_info(line_number):
    network = pypsa.Network()
    network.import_from_csv_folder("csv")
    
    # gets name of conductor at specified line number
    conductor_name = network.lines['conductor'][line_number]
    
    # get array of data for specific conductor
    dataframe = pd.read_csv('tempcsv/conductor_library.csv')
    print(dataframe)
    conductor_info = dataframe.loc[conductor_name] #.loc is label-based indexing
    
    return conductor_info

# for conductor, can get info from conductor library
print(get_conductor_info(11))