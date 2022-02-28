"""
This file is example design parallel to bmi_main.py -> main file
"""
# load library
from bmi_lib import *

# set variables
height_column='HeightCm' # height column name in json file
weight_column='WeightKg' # weight column name in json file
input_json='input.json' # json file path

# main
if __name__=='__main__':
    start = time.time()
    print("Running example design ...")
    # reading input json file by height and weight columns
    data=read_file(input_json,height_column,weight_column)
    
    # generate bmi_repo -> dataframe having columns =[BMI_category,	BMI_range_upper	,BMI_range_lower,	Risk]
    bmi_repo=create_bmi_repo()
    
    # Update data with calculated BMI, category and risk
    data=final_data(data,height_column,weight_column,bmi_repo)
    
    # get counts
    count_by_bmi_category=get_count_by_column(data,'BMI_cat')
    count_by_bmi_risk=get_count_by_column(data,'BMI_risk')
    
    # print output counts
    print('\n count_by_bmi_category: \n\n',get_pretty_table(count_by_bmi_category,by='category'))
    print('\n count_by_bmi_risk: \n\n',get_pretty_table(count_by_bmi_risk,by='risk'))
    
    print("\n Successfully ran example design")
    end = time.time()
    
    # print total execution time
    print(f'\n Execution time: {round(end - start,3)} seconds\n')