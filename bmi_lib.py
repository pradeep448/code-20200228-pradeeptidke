"""
This is library file for BMI calculator app i.e, bmi_main.py
"""

#--------------------------------------------------------------------
# import libraries
#--------------------------------------------------------------------
import pandas as pd # data processing, file read
import logging # logging errors
import os # os tasks, check file existence
import sys # system tasks, exit
import time # calculate execution time
import tabulate # pretty print of BMI table

#--------------------------------------------------------------------
# Function definitions
#--------------------------------------------------------------------


"""
This function reads json file

args:
    file : json file path
    height_column: height column name in file
    weight_column: weight column name in file

return:
    pandas dataframe

"""
def read_file(file,height_column,weight_column):
    # check if file exists
    if os.path.exists(file):
        # return json data as pandas dataframe
        return pd.read_json(file)[[height_column,weight_column]]
    else:
        print(f'{file} does not exist')
        sys.exit()
        

#--------------------------------------------------------------------
"""
This function creates BMI repository to compare BMI values and fetch 
corresponding BMI category and risk

args:
    None
return:
    pandas dataframe
"""
def create_bmi_repo():
    bmi_repo={'BMI_category':['Underweight','Normal','Overweight','Moderately_obese','Severely_obese','Very_severely_obese'],
                'BMI_range_upper':[18.4,24.9,29.9,34.9,39.9,1000],
                'BMI_range_lower':[0,18.5,25,30,35,40],
                'Risk':["Malnutrition","Low","Enhanced","Medium","High","Very_high"]}
    return pd.DataFrame(bmi_repo)


#--------------------------------------------------------------------
"""
This function calculates BMI, its category and risk and saves them in
data as in columns BMI, BMI_cat, BMI_risk respectively.

args:
    data: json data read as dataframe
    height_column: height column name as in data
    weight_column: weight column name as in data
    bmi_repo: BMI repository created
return:
    updated data as dataframe
"""
def final_data(data,height_column,weight_column,bmi_repo):
    # calculate BMI
    data['BMI']=data[weight_column]/((data[height_column]/100)**2)
    # create BMI category & BMI risk columns
    data[['BMI_cat','BMI_risk']]=''
    # fill BMI category & BMI risk columns
    for i in data.index:
        bmi_curr=data.loc[i,'BMI']
        for j in bmi_repo.index:
            if (bmi_repo.loc[j,'BMI_range_upper']>bmi_curr) and  (bmi_repo.loc[j,'BMI_range_lower']<bmi_curr):
                data.loc[i,'BMI_cat']=bmi_repo.loc[j,'BMI_category']
                data.loc[i,'BMI_risk']=bmi_repo.loc[j,'Risk']
                break
    return data

#--------------------------------------------------------------------
"""
This functions returns count of people by column name i.e, BMI_catogory 
& BMI_risk

args:
    data: updated data as pd.Dataframe from final_data()
    column_name: column name by which count to be calculated
    
return:
    count as pd.Series
"""
def get_count_by_column(data,column_name):
     return data[column_name].value_counts()
#--------------------------------------------------------------------


"""
This functions return pretty formatted string of pd.Series

args:
    series: pd.Series to be converted to pretty string
    by: value to be counted 
        category: to count by BMI category 
        risk: to count by BMI risk 
            
    
return:
    pretty string 
"""

def get_pretty_table(series,by):
    return tabulate.tabulate(pd.DataFrame(series),headers=[f'BMI_{by}','Count'])

#--------------------------------------------------------------------