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


def display_outliers(data, ignore_col, num_cat):

    col_name = []
    col_lower_limit = []
    col_upper_limit = []

    for col in num_cat:
    
        if col not in ignore_col:
            lower_limit = int(data["{}".format(col)].mean() - 3 * data["{}".format(col)].std())
            upper_limit = int(data["{}".format(col)].mean() + 3 * data["{}".format(col)].std())

            col_name.append(col)
            col_lower_limit.append(lower_limit)
            col_upper_limit.append(upper_limit)
            

    dt = {
        "Columns": col_name,
        "Lower Limit": col_lower_limit,
        "Upper Limit": col_upper_limit
    }

    data = pd.DataFrame(dt)

    return data
