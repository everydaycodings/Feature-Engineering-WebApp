import numpy as np
import pandas as pd

def data(data):

    data = pd.read_csv(data)

    return data

def describe(data):

    global num_category, str_category
    num_category = [feature for feature in data.columns if data[feature].dtypes != "O"]
    str_category = [feature for feature in data.columns if data[feature].dtypes == "O"]
    column_with_null_values = data.columns[data.isnull().any()]
    return data.describe(), data.shape, data.columns, num_category, str_category, data.isnull().sum(),data.dtypes.astype("str"), data.nunique(), str_category, column_with_null_values


def display_null_per(data, null_del_per):

    null_performer = []
    null_performer_per = []
    null_remove_column = []
    null_replace_column = []
    
    data_columns = data.columns.to_list()

    for col in data_columns:
        miss_value = float(data["{}".format(col)].isnull().mean() * 100)

        if miss_value > 0.0:
            null_performer.append(col)
            null_performer_per.append("{}%".format("%.2f"%miss_value))
        
        if miss_value > 0.0 and miss_value < null_del_per:
            null_replace_column.append(col)
        
        if miss_value >null_del_per:
            null_remove_column.append(col)
    
    data_raw = {
        "Columns": null_performer,
        "Percentage": null_performer_per
    }

    data = pd.DataFrame(data_raw)

    return data


