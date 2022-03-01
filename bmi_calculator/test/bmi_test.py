"""
This script is used to test the app for different sized BMI datasets

Command format:
    
python bmi_test.py <input_json_file> <height_col_name> <weight_col_name>
"""

# for accessing library
import sys
# adding library folder to the system path
sys.path.insert(0, '../lib')

# load library
from bmi_lib import *

# creating command and args
my_parser = argparse.ArgumentParser('BMI App tester')
my_parser.add_argument('input_json_file', type=str,  help='input json file path')
my_parser.add_argument('height_col_name', type=str,  help='height column name in json file')
my_parser.add_argument('weight_col_name', type=str,  help='weight column name in json file')

args = my_parser.parse_args()


# main
if __name__=='__main__':
    
    print("Testing design ...")
    # logging.info('Test started')
    # using example function for testing
    status=bmi_example(input_json=args.input_json_file,height_column=args.height_col_name,
                       weight_column=args.weight_col_name)
    
    if status==True:
        print("\n Test completed Successfully")
        # logging.info('Run Example completed')
    else:
        print("\n Test failed")
        # logging.error('Run Example failed')
