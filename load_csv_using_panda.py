#This is a module to use panda to load csv files
import pandas as pd
import os

def load_data(file_name_with_path):
	return pd.read_csv(file_name_with_path)

#if file path and file name are needed to be fed separately 
#use the below function
#def load_data(file_path, file_name):
#	csv_path = os.path.join(file_path, file_name)
#	return pd.read_csv(csv_path)


