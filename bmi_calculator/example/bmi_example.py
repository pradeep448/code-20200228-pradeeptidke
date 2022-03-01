"""
This file is example design parallel to bmi_main.py -> main file
"""
# for accessing library
import sys
# adding library folder to the system path
sys.path.insert(0, '../lib')

# load library
from bmi_lib import *


# main
if __name__=='__main__':
    
    print("Running example design ...")
    # logging.info('Run Example started')
    # example design function
    status=bmi_example()
    
    if status==True:
        print("\n Successfully ran example design")
        # logging.info('Run Example completed')
    else:
        print("\n Example design failed")
        # logging.error('Run Example failed')
