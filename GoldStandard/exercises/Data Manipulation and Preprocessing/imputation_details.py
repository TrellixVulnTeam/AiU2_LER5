import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from missingpy import KNNImputer

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def load_input_data_from_file(input_file_path):
    dataset = pd.read_csv(input_file_path)
    print("dataset size: [", dataset.shape[0], 'rows,', dataset.shape[1], 'columns]')
    return dataset

def count_missing_cells(dataset):
    print ("Column name \t\t #missing_cells")
    return dataset.isnull().sum()

def find_mean(dataset, col_name):
    return round(dataset[col_name].mean(), 1)

def find_mode(dataset, col_name):
    return dataset[col_name].mode()[0]

def fill_missing_cells (dataset, col_name, method):
    if method == 'mean':
        cell_value_to_fill = find_mean(dataset, col_name)
        print ('Mean value of ' + col_name + ': ' + str(cell_value_to_fill))
    elif method == 'mode':
        cell_value_to_fill = find_mode(dataset, col_name)
        print('Mode value of ' + col_name + ': ' + str(cell_value_to_fill))
    else:
        print("Unknown imputation method")

    dataset[col_name] = dataset[col_name].fillna(cell_value_to_fill)

def imputate_using_knn(dataset):
    knn_impu = KNNImputer(n_neighbors=3, weights="uniform")
    result = knn_impu.fit_transform(dataset)
    result = pd.DataFrame(result)
    result.columns = ["CRIM", "ZN", "INDUS", "CHAS", "INDUS", "RM", "AGE", "DIS", "RAD", "TAX", "PT", "B", "LSTAT", "MV"]
    return result

