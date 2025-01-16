"""Simple python based script to do statistical analysis"""
import os,functions
from pyenvvariables import data_directory
print("""This is a program written in python that implements methods to calculate descriptive statistics, confidence intervals, or perform hypothesis testing.\nNote this program doesn't create any graphs but will produce useful numerical output.""")
def main():
    """See if data directory exists"""
    if os.path.exists(data_directory) is True:
            print("Data directory exists")
    else:
        os.mkdir('data')
        print("Data directory created")

    """See if data directory is empty"""
    if os.listdir(data_directory):
        print("Directory has data")
    else:
        print("Directory has no data")
    functions.selection()

main()
