"""Simple python based script to do statistical analysis"""
import os,analysis
from pyenvvariables import data_directory
print("""This is a package written in python that implements some basic statistical methods in the command line""")
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
    analysis.selection()

main()
